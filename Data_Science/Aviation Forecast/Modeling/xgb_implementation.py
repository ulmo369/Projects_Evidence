import pandas as pd
from xgboost import XGBClassifier
import xgboost as xgb
import glob
import os
import config as config
from sklearn.metrics import balanced_accuracy_score
import dask.distributed
import dask.dataframe as dd
import matplotlib.pyplot as plt
import seaborn as sns
from Modeling import model_util

# Entrenamiento del modelo XGBoost agrupando archivos
def trainXGBModel(prepared_data_path, models_path):
    # Configuración de Dask
    with dask.distributed.LocalCluster(n_workers = 1) as cluster, dask.distributed.Client(cluster) as client:
        train_data_path = os.path.join(prepared_data_path, 'train')
        csv_folder_path = train_data_path + '/*.csv'

        model = xgb.Booster()
    
        params = { 
            'objective':'binary:logistic', 
            'n_estimators':200, 
            'max_depth':15, 
            'learning_rate':0.01,
            'scale_pos_weight':150,
            'use_label_encoder':False
                }

        print('Training start')
        file_list = []

        for i, file_name in enumerate(glob.glob(csv_folder_path)):
            file_list.append(file_name)
            
            if i > 200: # Detener entrenamiento por número de archivos
                break

        train_data = dd.read_csv(file_list)
        df_x_train = train_data.drop([config.BOOL_PREDICTION_VAR], axis = 1)
        df_y_train = train_data[config.BOOL_PREDICTION_VAR]
            
        train_matrix = xgb.dask.DaskDMatrix(client, df_x_train, df_y_train)

        result = xgb.dask.train(client, 
                                params, 
                                train_matrix, 
                                num_boost_round = 120, 
                                evals = [(train_matrix, 'train')])
        
        model = result['booster']
        history = result['history']
        history_df = pd.DataFrame(history['train'], columns = history['train'].keys())

        # Graficar el avance de función de pérdida
        plt.ylim(0, 1.0)
        sns.lineplot(data = history_df['logloss']).set_title('Model loss on training iterations')
        plt.show()
        
        print('Training ended, saving model')
        
        model.save_model(os.path.join(models_path, 'saved_model.h5'))
    
    print('Completed execution')

# Entrenamiento por iteraciones de Modelo, ajuste por archivo
def trainXGBModelIncremental(prepared_data_path, models_path):
    # Configuración de Dask
    with dask.distributed.LocalCluster() as cluster, dask.distributed.Client(cluster) as client:
        train_data_path = os.path.join(prepared_data_path, 'train')
        csv_folder_path = train_data_path + '/*.csv'

        model = xgb.Booster()
        # Parámetros de entrenamiento
        params = { 
            'objective':'binary:logistic', 
            'n_estimators':200, 
            'max_depth':15, 
            'learning_rate':0.01,
            'scale_pos_weight':150,
            'use_label_encoder':False
                }

        print('Training start')

        for i, file_name in enumerate(glob.glob(csv_folder_path)):
            df_train = dd.read_csv(file_name)
            df_x_train = df_train.drop([config.BOOL_PREDICTION_VAR], axis = 1)
            df_y_train = df_train[config.BOOL_PREDICTION_VAR]
            
            train_matrix = xgb.dask.DaskDMatrix(client, df_x_train, df_y_train)

            if i == 0:
                model = xgb.dask.train(client, 
                                    params, 
                                    train_matrix, 
                                    num_boost_round = 20, 
                                    evals = [(train_matrix, 'train')])['booster']
            else:
                model = xgb.dask.train(client, 
                                    params, 
                                    train_matrix, 
                                    num_boost_round = 20, 
                                    evals = [(train_matrix, 'train')],
                                    xgb_model = model)['booster']

            print(file_name)
            
            if i > 200: # Detener entrenamiento por número de archivos
                break
        
        print('Training ended, saving model')
        
        model.save_model(os.path.join(models_path, 'saved_model.h5'))
    
    print('Completed execution')

# Prueba de precisión del modelo
def testXGBModel(prepared_data_path, models_path):
    # Configuración de Dask
    with dask.distributed.LocalCluster() as cluster, dask.distributed.Client(cluster) as client:
        test_data_path = os.path.join(prepared_data_path, 'test')
        csv_folder_path = test_data_path + '/*.csv'

        model = xgb.Booster()
        model.load_model(os.path.join(models_path, 'saved_model.h5')) # Cargamos modelo

        print('Testing start')
        file_list = []

        for i, file_name in enumerate(glob.glob(csv_folder_path)):
            file_list.append(file_name)
            
            if i > 200: # Detener entrenamiento por número de archivos
                break
        
        test_data = dd.read_csv(file_list)
        df_x_test = test_data.drop([config.BOOL_PREDICTION_VAR], axis = 1)
        df_y_test = test_data[config.BOOL_PREDICTION_VAR]
            
        test_matrix = xgb.dask.DaskDMatrix(client, df_x_test)
        
        predictions = xgb.dask.predict(client, model, df_x_test)
        
        # Es necesario redondear la predicción para obtener el valor del label
        #predictions_df = pd.DataFrame(predictions.compute().round().astype(int), columns = [config.BOOL_PREDICTION_VAR])
        predictions_df = predictions.compute().round().astype(int).to_frame(name = config.BOOL_PREDICTION_VAR)

        print("Current Accuracy:", balanced_accuracy_score(df_y_test.compute(), predictions_df[config.BOOL_PREDICTION_VAR]))
        
        print('Testing ended')

    print('Completed execution')

# Generar los archivos de resultados sobre la ruta especificada
def generateXGBPredictions(new_test_data_path, models_path, results_path):
    # Configuración de Dask
    with dask.distributed.LocalCluster() as cluster, dask.distributed.Client(cluster) as client:
        csv_folder_path = new_test_data_path + '/*.csv'

        model = xgb.Booster()
        model.load_model(os.path.join(models_path, 'saved_model.h5')) # Cargamos modelo

        print('Generating predictions...')
        
        for file_name in glob.glob(csv_folder_path):
            test_data = dd.read_csv(file_name)
            df_x_test = model_util.dataCleaning(test_data)

            test_matrix = xgb.dask.DaskDMatrix(client, df_x_test)

            predictions = xgb.dask.predict(client, model, test_matrix)
            # Es necesario redondear la predicción para obtener el valor del label
            predictions_df = pd.DataFrame(predictions.compute().round().astype(int), columns = [config.BOOL_PREDICTION_VAR])

            model_util.savePredictionsFile(results_path, file_name, test_data.compute(), predictions_df)
        
        print('Predictions Generated')

    print('Completed execution')