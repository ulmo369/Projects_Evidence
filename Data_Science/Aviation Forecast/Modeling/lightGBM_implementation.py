import pandas as pd
import lightgbm as lgb
import glob
import os
import config as config
from sklearn.metrics import balanced_accuracy_score
import dask.distributed
import dask.dataframe as dd
import matplotlib.pyplot as plt
import seaborn as sns
from Modeling import model_util

# Entrenemos wiiii
def trainLightGBMModel(prepared_data_path, models_path):
    # Configuración de Dask
    with dask.distributed.LocalCluster(n_workers=1) as cluster, dask.distributed.Client(cluster) as client:
        train_data_path = os.path.join(prepared_data_path, 'train')
        csv_folder_path = train_data_path + '/*.csv'

        params = {
            'objective': 'binary',
            'metric': 'binary_logloss',
            'boosting_type': 'gbdt',
            'num_leaves': 31,
            'learning_rate': 0.01,
            'scale_pos_weight': 150
        }

        print('Training start')
        file_list = []

        for i, file_name in enumerate(glob.glob(csv_folder_path)):
            file_list.append(file_name)

            if i > 200:  # Detener entrenamiento por número de archivos
                break

        train_data = dd.read_csv(file_list)

        train_data = train_data.loc[train_data['col5_float'] > 17500] # Filtro de datos a predecir
        train_data_majority = train_data.loc[train_data[config.BOOL_PREDICTION_VAR] == 0].compute()
        train_data_minority = train_data.loc[train_data[config.BOOL_PREDICTION_VAR] == 1].compute()

        # Generar dataset balanceado
        train_data_majority = train_data_majority.sample(n = train_data_minority.shape[0], random_state = 2)
        train_data = pd.concat([train_data_majority, train_data_minority])

        df_x_train = train_data.drop([config.BOOL_PREDICTION_VAR], axis=1)
        df_y_train = train_data[config.BOOL_PREDICTION_VAR]

        train_matrix = lgb.Dataset(df_x_train.computed(), label=df_y_train.compute())

        
        result = lgb.train(params,
                            train_matrix,
                            valid_sets=[train_matrix])
        
        '''
        model = result['booster']
        history = result['history']
        history_df = pd.DataFrame(history['binary_logloss'], columns=['binary_logloss'])

        # Grafiquemos si es que no anda jalando
        plt.ylim(0, 1.0)
        sns.lineplot(data=history_df['binary_logloss']).set_title('Model loss on training iterations')
        plt.show()
        '''
        optimal_rounds = result.best_iteration or result.num_trees()

        final_model = lgb.train(params, train_matrix, num_boost_round=optimal_rounds)

        print('Training ended, saving model')

        final_model.save_model(os.path.join(models_path, 'saved_model.txt'))

    print('Completed execution')


# Ahora carguemos el modelo WIIIIIII
def testLightGBMModel(prepared_data_path, models_path):
    # Configuración de Dask
    with dask.distributed.LocalCluster() as cluster, dask.distributed.Client(cluster) as client:
        test_data_path = os.path.join(prepared_data_path, 'test')
        csv_folder_path = test_data_path + '/*.csv'

        model = lgb.Booster(model_file=os.path.join(models_path, 'saved_model.txt'))  # Cargamos modelo

        print('Testing start')
        file_list = []

        for i, file_name in enumerate(glob.glob(csv_folder_path)):
            file_list.append(file_name)

            if i > 200:  # Detener entrenamiento por número de archivos
                break

        test_data = dd.read_csv(file_list)
        df_x_test = test_data.drop([config.BOOL_PREDICTION_VAR], axis=1)
        df_y_test = test_data[config.BOOL_PREDICTION_VAR]

        predictions = model.predict(df_x_test.compute())

        #Cosas raras
        predictions_df = pd.DataFrame(predictions.round().astype(int), columns=[config.BOOL_PREDICTION_VAR])

        print("Current Accuracy:", balanced_accuracy_score(df_y_test.compute(), predictions_df[config.BOOL_PREDICTION_VAR]))

        print('Testing ended')

    print('Completed execution')
