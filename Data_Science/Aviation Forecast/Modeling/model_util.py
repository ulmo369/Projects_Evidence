import pandas as pd
import glob
import os
import config as config

# Generar archivo de predicciones para un archivo específico
def savePredictionsFile(results_path, file_name, df_x, predictions_df):
    results_file_name = 'results_' + os.path.basename(file_name)

    # Ajustamos los nombres de las columnas
    results_df = df_x.rename(columns = {'col34_integer':'col36_integer', 
                              'col33_integer':'col35_integer',
                              'col32_integer':'col34_integer',
                              'col31_integer':'col33_integer',
                              'col30_integer':'col32_integer',
                              'col29_integer':'col31_integer'})
    
    results_df.insert(29, config.BOOL_PREDICTION_VAR, predictions_df[config.BOOL_PREDICTION_VAR])
    results_df.insert(30, config.BOOL_PREDICTION_VAR + '.1', predictions_df[config.BOOL_PREDICTION_VAR])
    
    results_df.to_csv(os.path.join(results_path, results_file_name), index = False)

# Operaciones realizadas como parte de Data Preparation
def dataCleaning(df):
    col = df.columns

    for i in range(2, len(col)+1, 2):
        df = df.drop(col[i], axis = 1)
            
    df = df.drop(['time', 'col3_boolean', 'col19_float', 'col33_integer', 'col31_integer'], axis = 1)
    return df


def createModelFolders():
    if (os.path.exists(config.MODEL_PATH)):
        print("models folder already exists")
    else:
        print("Creating models folder")
        os.mkdir(config.MODEL_PATH)

    if (os.path.exists(config.RESULTS_PATH)):
        print("results folder already exists")
    else:
        print("Creating results folder")
        os.mkdir(config.RESULTS_PATH)
    
