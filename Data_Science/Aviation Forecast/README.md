# Stable Cruise Prediction

Currently all the function are called from functions.py.
The repo is moving into folder per step, we are working migrating the code to the new structure.
The content is the same. The new structure is the following.
You can find the migration in the branch "computer_version"


## Table of Contents
1. [Overview](#overview)
2. [Data Understanding](#data-understanding)
3. [Data Preparation](#data-preparation)
4. [Modeling](#modeling)
5. [Evaluation](#evaluation)
6. [Deployment](#deployment)

## Overview
The goal of this project is to predict the stable cruise boolean variable based on the given data. The data is provided by the client and is not publicly available.

Following the Crisp-DM process, the project is divided in steps, each one with its own folder.
In order to test the functions with example data, we created some dummies data and other functions that let us manage the read and write of the data. These scripts are in the folder utils.

## Utils
This folder contains the following files:
1. dummies.py: This file contains the functions to create dummies data.
    - createDummies: Create a folder with the dummies data. The options are the number of files and rows. It is configured in config.py.

2. filter.py: In order to classify the files in the dataset. The filter.json file contains which group of files are in the dataset. This file contains the functions to read and write the filter.json file.


## Data Understanding
In this link you can find the details of the data understanding process:
https://docs.google.com/document/d/1sCeNFC7ceV5MpCpQXj-qs-sVSyhwP80wJcnP_U90YZg/edit?usp=sharing

The data understanding folder contains the following files:
1. summary.py: This file contains summary functions. Given the original dataset, we can obtain the summary of the data. Each summary is saved in a CSV file.
    - createSummary: This is a lambda function that recibe how to obtain the information from a file and iterate over the files in the folder to obtain the summary of each file. All the summaries used this function.
    - summary_count_ones: Given the dataset. It returns the distribution of the independent variable (stable_cruise) in the dataset and the size of the elements in the dataset.
    - summaryRedundanceCounts: Given the dataset. It returns the count of redundancy errors in the dataset. The redundancy errors are the left value is missing, the right value is missing or values are different.
    - summaryRedundance: Given the dataset. It returns the sum of the different redundancy errors in the dataset per column.
    - summaryDescriptive: Given the dataset. It returns the descriptive statistics of each file in the dataset.

2. plots.py: This file contains plot functions. Given summaries files. It returns plots of the summaries.
The interpretation of the plots is in the data understanding document.


## Data Preparation
In this link you can find the details of the data preparation process:
https://docs.google.com/document/d/1gTptRf42mRRe2d5pii7ycZk7FVO3Z9nIiWFBvxkOgYw/edit

The data preparation folder contains the following files:
preparedFolder.py: This file contains the functions to prepare the dataset. Once we understand the data, we can prepare the dataset.
This file lets us select the files and columns to be used in the modeling step.

## Modeling
We decided to divide this phase into 2 iterations, in these links you can find the details of the modeling process:

Iteration 1: https://docs.google.com/document/d/1mJQWgEwbXbS11bey8kBaEKg_NRCIgQpQyORnIQdIN6o/edit?usp=sharing

Iteration 2: https://docs.google.com/document/d/1DAyFax38jVjqYTr_vy9zj4l-421du5zsPhbGTB25JuA/edit?usp=sharing


The modeling folder contains the following files:
1. model_util.py: This file contains additional functions to generate the files used for predictions.
   
2. SKlearn_implementation.py: This file contains an implementation of a Logistic Regression with SKlearn and uses 2 main functions.
    - trainModel: As the name says, it trains the model with these hyperparameters:
      - random_state=42
      - max_iter = 600
    - testModel: This test the model using the prepared data of preparedFolder.py.
   
3. lightGBM_implementation.py: This file contains an implementation of histogram-based decision trees using lightGBM and it uses 2 main functions.
    - trainModel: As the name says, it trains the model with these hyperparameters:
      - objective: binary
      - metric: binary_logloss
      - boosting_type: gbdt
      - num_leaves: 31
      - learning_rate: 0.01
      - scale_pos_weight: 150
    - testModel: This test the model using the prepared data of preparedFolder.py.
   
4. logistic_model.py: This file contains another implementation of a Logistic Regression with SKlearn and it uses 3 main functions. Is important to say that in the end this Model was deprecated due to the results and the summary of the model.
    - create_logistic_model: As the name says, it creates the logistic model but with normalization of MinMaxScaler.
    - getResults: This function get the results of
      - TruePositives
      - FalsePositives
      - TrueNegatives
      - FalseNegatives
      - BinaryAccuracy
      - Precision
      - Recall
    - getCorrelationMatrix: Here we check the correlations of our data
         
5. lstm_implementation.py: This file contains the implementation of a recurrent neural network using LTSM, it uses 4 main functions.
    - get_model: It creates the model with the 4 following layers:
      - LSTM: 50 neurons, return_sequences=True
      - LSTM: 50 neurons, return_sequences=False
      - Dense: 64 neurons, activation = 'relu'
      - Dense: 1 neurons, activation = 'sigmoid'
    - trainTFModel‎: This function trains the model with the grouped files
    - testModel: This test the model using the prepared data of preparedFolder.py
    - generateTFPredictions: This generates a file with all the predictions of the model

6. neural_network_implementation.py: This contains a Neural Network implementation and it uses 4 main functions.
    - get_model: It creates the model with the 4 following layers:
      - Dense: 128 neurons, activation = 'relu'
      - Dense: 512 neurons, activation = 'relu'
      - Dense: 128 neurons, activation = 'relu'
      - Dense: 1 neurons, activation = 'sigmoid'
    - trainTFModel‎: This function trains the model with the grouped files, applying filters to some columns
    - testModel: This test the model using the prepared data of preparedFolder.py, where another filter is applied and we check our result adding a confusion matrix.
    - generateTFPredictions: This generates a file with all the predictions of the model
 
7. xgb_implementation.py: This file contains the implementation of decision trees using XGBoost and it uses 3 main functions.
    - trainXGBModel: As the name says, it trains the model with these hyperparameters:
      - objective: binary:logistic
      - n_estimators: 200
      - max_depth: 200
      - learning_rate: 15
      - scale_pos_weight: 150
      - use_label_encoder: False
      - train_matrix
      - num_boost_round = 120
    - ‎testXGBModel‎: This test the model using the prepared data of preparedFolder.py.
    - generateXGBPredictions: This generates a file with all the predictions of the model

## Evaluation
In this link you can find the details of the evaluation process:
https://docs.google.com/document/d/1UvGI1kEqWPV786vF84P_FjX51_cmV9gMPs3KWMuEJ8c/edit?usp=sharing

As an evaluation criterion, we seek to achieve 85% balanced precision in the model tests. These are the results:

With XGBoost

| Modelo de predicción   | Accuracy | Balanced Accuracy    |
|------------------------|----------|----------------------|
| XGBoost 1.0.0          | 0.9659   | 0.688                |
| XGBoost 1.1.0          | 0.9746   | 0.630                |
| XGBoost 1.2.0          | 0.9651   | 0.6379               |


With Neuronal Networks

| Modelo de predicción   | Accuracy | Balanced Accuracy    |
|------------------------|----------|----------------------|
| Red Neuronal 1.0.0     | 0.9426   | 0.8327               |
| Red Neuronal 1.1.0     | 0.9812   | 0.8677               |
| Red Neuronal 1.2.0     | 0.9751   | 0.853                |

## Deployment

In this link you can find the details of the deployment process:
https://docs.google.com/document/d/1shSI7PvX1mMz2e9cCMQKz1vybCgAYKsHxFPSL1fV0NQ/edit?usp=sharing

This document explains in detail the final model selected, which will be delivered to our client.
