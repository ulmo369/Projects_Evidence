import pandas as pd
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential, load_model
from keras.layers import Dense
import glob
import os
import config as config
from sklearn.metrics import accuracy_score, balanced_accuracy_score, precision_score, recall_score, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import seaborn as sns
from Modeling import model_util
import dask.distributed
import dask.dataframe as dd
import numpy as np

# Generar modelo de clasificación
def get_model(normalization_tensor, column_count):
  metrics = [
      keras.metrics.TruePositives(name='tp'),
      keras.metrics.FalsePositives(name='fp'),
      keras.metrics.TrueNegatives(name='tn'),
      keras.metrics.FalseNegatives(name='fn'), 
      keras.metrics.BinaryAccuracy(name='accuracy'),
      keras.metrics.Precision(name='precision'),
      keras.metrics.Recall(name='recall')
  ]
  
  normalization_layer = tf.keras.layers.Normalization(input_shape = [column_count,], axis=-1)
  normalization_layer.adapt(normalization_tensor)

  model = Sequential([
        normalization_layer,
        Dense(units = 128, activation = 'relu'),
        Dense(units = 512, activation = 'relu'),
        Dense(units = 128, activation = 'relu'),
        Dense(units = 1, activation = 'sigmoid')
    ])

  model.compile(optimizer = 'adam',
                  loss = 'binary_crossentropy',
                  metrics = metrics)
    
  return model

# Entrenamiento del modelo de red neuronal agrupando archivos
def trainTFModel(prepared_data_path, models_path):
    # Configuración de Dask
    with dask.distributed.LocalCluster(n_workers = 1) as cluster, dask.distributed.Client(cluster) as client:
        train_data_path = os.path.join(prepared_data_path, 'train')
        csv_folder_path = train_data_path + '/*.csv'
        
        print('Loading data files')
        file_list = []
        normalization_sample = []

        for i, file_name in enumerate(glob.glob(csv_folder_path)):
            file_list.append(file_name)

            if i == 0:
                normalization_sample = pd.read_csv(file_name)
                normalization_sample = normalization_sample.drop([config.BOOL_PREDICTION_VAR], axis = 1)

        train_data = dd.read_csv(file_list)
        train_data = train_data.loc[train_data['col5_float'] >= 18000] # Filtro de datos a predecir
        train_data_majority = train_data.loc[train_data[config.BOOL_PREDICTION_VAR] == 0].compute()
        train_data_minority = train_data.loc[train_data[config.BOOL_PREDICTION_VAR] == 1].compute()

        # Generar dataset balanceado
        train_data_majority = train_data_majority.sample(n = train_data_minority.shape[0], random_state = 2)

        # Aplicar filtros
        train_data_minority = train_data_minority[train_data_minority['col7_float'] > 200]
        train_data_minority = train_data_minority[train_data_minority['col11_float'] > -5]
        train_data_minority = train_data_minority[train_data_minority['col11_float'] < 5]
        train_data_minority = train_data_minority[train_data_minority['col17_float'] > 70]

        train_data = pd.concat([train_data_majority, train_data_minority])

        df_x_train = train_data.drop([config.BOOL_PREDICTION_VAR], axis = 1)
        df_y_train = train_data[config.BOOL_PREDICTION_VAR]

        print('Model Configuration')
        x_train_tensor = tf.convert_to_tensor(df_x_train)
        normalization_tensor = tf.convert_to_tensor(normalization_sample)

        model = get_model(x_train_tensor, len(df_x_train.columns))

        print('Training start')
            
        history = model.fit(x_train_tensor, df_y_train, epochs = 30, batch_size = 32)
        history_df = pd.DataFrame(history.history)

        # Graficar el avance de función de pérdida
        plt.ylim(0, 1.0)
        sns.lineplot(data = history_df['accuracy']).set_title('Model accuracy on training iterations')
        plt.show()
        
        print('Training ended, saving model')
        
        model.save(os.path.join(models_path, 'saved_model_tf.keras'))

    print('Completed execution')


# Prueba de precisión del modelo
def testTFModel(prepared_data_path, models_path):
    # Configuración de Dask
    with dask.distributed.LocalCluster(n_workers = 1) as cluster, dask.distributed.Client(cluster) as client:
        test_data_path = os.path.join(prepared_data_path, 'test')
        csv_folder_path = test_data_path + '/*.csv'
        
        print('Loading data files')
        file_list = []

        for i, file_name in enumerate(glob.glob(csv_folder_path)):
            file_list.append(file_name)

        test_data = dd.read_csv(file_list)
        test_data_df = test_data.compute().reset_index()
        test_data_filtered = test_data.loc[test_data['col5_float'] >= 18000] # Filtro de datos a predecir

        df_x_test_filtered = test_data_filtered.drop([config.BOOL_PREDICTION_VAR], axis = 1).compute()
        df_y_test = test_data_df[config.BOOL_PREDICTION_VAR]

        print('Model Configuration')
        x_test_tensor = tf.convert_to_tensor(df_x_test_filtered)
        model = load_model(os.path.join(models_path, 'saved_model_tf.keras'))

        print('Testing start')
        predicted_indexes = test_data_df[test_data_df['col5_float'] >= 18000].index
        predictions_df = pd.DataFrame(0, index = np.arange(test_data_df.shape[0]), columns = [config.BOOL_PREDICTION_VAR])

        predictions = model.predict(x_test_tensor).round().astype(int)
        predictions_df.iloc[predicted_indexes] = pd.DataFrame(predictions)

        cm = confusion_matrix(df_y_test, predictions_df[config.BOOL_PREDICTION_VAR], labels = [0, 1])
        cm_plot = ConfusionMatrixDisplay(confusion_matrix = cm, display_labels = [0, 1])
        cm_plot.plot()
        plt.show()

        print(cm)
        print('Accuracy:', accuracy_score(df_y_test, predictions_df))
        print('Balanced Accuracy:', balanced_accuracy_score(df_y_test, predictions_df))
        print('Precision:', precision_score(df_y_test, predictions_df))
        print('Recall:', recall_score(df_y_test, predictions_df))
        
        print('Testing ended')

    print('Completed execution')

# Generar los archivos de resultados sobre la ruta especificada
def generateTFPredictions(new_test_data_path, models_path, results_path):
    csv_folder_path = new_test_data_path + '/*.csv'

    model = load_model(os.path.join(models_path, 'saved_model_tf.keras')) # Cargamos modelo

    print('Generating predictions...')
    
    for file_name in glob.glob(csv_folder_path):
        test_data = pd.read_csv(file_name)
        df_x_test = model_util.dataCleaning(test_data)

        x_test_tensor = tf.convert_to_tensor(df_x_test)

        predictions = model.predict(x_test_tensor).round().astype(int)

        predictions_df = pd.DataFrame(predictions, columns = [config.BOOL_PREDICTION_VAR])

        model_util.savePredictionsFile(results_path, file_name, test_data, predictions_df)
    
    print('Predictions Generated')