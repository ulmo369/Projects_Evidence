import pandas as pd
import glob
import os
import config as config
from sklearn.metrics import balanced_accuracy_score
import dask.distributed
import dasg.dataframe as dd

import dask
import joblib
from dask_ml.model_selection import train_test_split
from dask_ml.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from dask_ml.model_selection import train_test_split as dask_ml_train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

def trainModel(prepared_data_path, models_path):
    #Configuración de Dask
    with dask.distributed.LocalCluster(n_workers=1) as cluster, dask.distributed.Client(cluster) as client:
        train_data_path = os.path.join(prepared_data_path, 'train')
        csv_folder_path = train_data_path + '/*.csv'

        model = LogisticRegression(random_state=42, max_iter = 600)

        print('Training start')
        file_list = []

        for i, file_name in enumerate(glob.glob(csv_folder_path)):
            file_list.append(file_name)

            if i > 200:
                break

        dfs = [dd.read_csv(file) for file in file_list]
        train_data = dd.read_csv(file_list)

        X = train_data.drop(config.BOOL_PREDICTION_VAR, axis=1)
        y = train_data[config.BOOL_PREDICTION_VAR]

        X_train = X.compute()
        y_train = y.compute()

        X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.15, random_state=42, shuffle=False)

        model.fit(X_train, y_train)

        predictions = model.predict(X_val)

        #-----
        X_train = X_train.sort_values(by = 'col1_boolean', ascending = True, ignore_index = True)

        d1 = X_train[:70400]
        d2 = X_train[-70400:]
        d = pd.concat([d1, d2], ignore_index=True)
        d = d.sample(frac=1, ignore_index=True)

        y_train = d['col1_boolean']
        X_train = d
        print(y_train.shape)
        print(X_train.shape)

        model.fit(X_train, y_train)
        #-----


        predictions = model.predict(X_val)

        print("Current model accuracy: ", balanced_accuracy_score(y_val, predictions))

        print('Training ended, saving model')

        matriz_confusion = confusion_matrix(y_val, predictions, labels=[0, 1])

        print(matriz_confusion)

        import seaborn as sns 
        mat = sns.heatmap(matriz_confusion, annot=True, fmt='.2f')
        plt.show()

        joblib.dump(model, os.path.join(models_path, 'saved_model.pkl'))

    print('Completed execution')

def testModel(prepared_data_path, models_path):
    #Configuración de Dask
    with dask.distributed.LocalCluster() as cluster, dask.distributed.Client(cluster) as client:
        test_data_path = os.path.join(prepared_data_path, 'test')
        csv_folder_path = test_data_path + '/*.csv'

        model = joblib.load(os.path.join(models_path, 'saved_model.pkl'))

        print('Testing start')
        file_list = []

        for i, file_name in enumerate(glob.glob(csv_folder_path)):
            file_list.append(file_name)

            if i > 200:
                break

        test_data = dd.read_csv(file_list)
        df_x_test = test_data.drop([config.BOOL_PREDICTION_VAR], axis = 1)
        df_y_test = test_data[config.BOOL_PREDICTION_VAR]

        X_test = df_x_test.compute()
        y_test = df_y_test.compute()

        predictions = model.predict(X_test)

        print("Current Accuracy:", balanced_accuracy_score(y_test, predictions))

        print('Testing ended')

    print('Completed execution')


# CURRENT BALANCED ACCURACY: 0.726498


