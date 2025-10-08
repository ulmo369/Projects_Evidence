
import pandas as pd
# import tensorflow as tf
# from tensorflow import keras
# from keras.models import Sequential, load_model
# from keras.layers import Dense
import glob
import os
import config as config
# from sklearn.metrics import balanced_accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns

# from sklearn.utils import class_weight

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score
from sklearn.preprocessing import MinMaxScaler

"""
def getData(prepared_data_path):
  # Configuración de Dask
    with dask.distributed.LocalCluster(n_workers=1) as cluster, dask.distributed.Client(cluster) as client:
        train_data_path = os.path.join(prepared_data_path, 'train')
        csv_folder_path = train_data_path + '/*.csv'

        print('Loading data files')
        file_list = []
        normalization_sample = []

        for i, file_name in enumerate(glob.glob(csv_folder_path)):
            file_list.append(file_name)

            if i == 0:
                normalization_sample = pd.read_csv(file_name)
                normalization_sample = normalization_sample.drop(
                    [config.BOOL_PREDICTION_VAR], axis=1)

        train_data = dd.read_csv(file_list)
        # Filtro de datos a predecir
        train_data = train_data.loc[train_data['col5_float'] > 18000]
        train_data_majority = train_data.loc[train_data[config.BOOL_PREDICTION_VAR] == 0].compute(
        )
        train_data_minority = train_data.loc[train_data[config.BOOL_PREDICTION_VAR] == 1].compute(
        )

        # Generar dataset balanceado
        train_data_majority = train_data_majority.sample(
            n=train_data_minority.shape[0], random_state=2)
        train_data = pd.concat([train_data_majority, train_data_minority])
        return train_data
"""


def create_logistic_model():
    print('Creating logistic model')
    # df = getData(config.PREPARED_DATA_PATH)
    temp_path = os.path.join(config.PREPARED_DATA_PATH, 'train')
    list = os.listdir(temp_path)
    try:
        df = pd.read_csv(os.path.join(temp_path, list[0]))
        print(df.head())
    except Exception as e:
        print(e)

    X = df.drop(config.BOOL_PREDICTION_VAR, axis=1)
    y = df[config.BOOL_PREDICTION_VAR]

    #   the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    scaler = MinMaxScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    model = LogisticRegression()
    model.fit(X_train_scaled, y_train)

    # Make predictions
    y_pred = model.predict(X_test_scaled)

    # Evaluate the model
    # Additional metrics
    print(classification_report(y_test, y_pred))
    print(model.summary())
    getCorrelationMatrix(df)
    getResults(model, y_test, y_pred)
    print('Completed execution')
    return


def getResults(y_test, y_pred):
    print('Getting results')
    try:
        # Calculate TruePositives, FalsePositives, TrueNegatives, FalseNegatives
        conf_matrix = confusion_matrix(y_test, y_pred)
        tn, fp, fn, tp = conf_matrix.ravel()

        # Calculate BinaryAccuracy
        binary_accuracy = accuracy_score(y_test, y_pred)

        # Calculate Precision
        precision = precision_score(y_test, y_pred)

        # Calculate Recall
        recall = recall_score(y_test, y_pred)

        # Print the metrics
        print(f'TruePositives: {tp}')
        print(f'FalsePositives: {fp}')
        print(f'TrueNegatives: {tn}')
        print(f'FalseNegatives: {fn}')
        print(f'BinaryAccuracy: {binary_accuracy:.4f}')
        print(f'Precision: {precision:.4f}')
        print(f'Recall: {recall:.4f}')
    except Exception as e:
        print(e)
        print('Error getting results')


def getCorrelationMatrix(df):
    print('Generating correlation matrix')
    try:
        correlation_matrix = df.corr()
        # Set up the heatmap figure
        plt.figure(figsize=(20, 10))
        # Create heatmap using seaborn
        sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", center=0)
        # Show the plot
        plt.title("Matrix Correlation")
        plt.show()
        print('Correlation matrix generated')
    except Exception as e:
        print(e)
        print('Error generating correlation matrix')
