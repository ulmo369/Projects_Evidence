
from Utils import filter, dummies, utils
import pandas as pd
import os
import numpy as np


def dataCleaning(file_path):
    try:
        df = pd.read_csv(file_path)
        col = df.columns
        for i in range(2, len(col)+1, 2):
            df = df.drop(col[i], axis=1)

        df = df.drop(['time', 'col3_boolean', 'col19_float',
                     'col33_integer', 'col31_integer'], axis=1)
        return df
    except Exception as e:
        print("Error reading csv file: "+str(e))
        return


def createDataPreparedFolder(folder_path_source, folder_path_destination):
    print("Creating folder with prepared data in " + folder_path_destination)
    print("Original Data in " + folder_path_source)
    print("Number of files in the folder origin: " +
          str(len(os.listdir(folder_path_source))))

    utils.createFolder(folder_path_destination)
    utils.createFolder(os.path.join(folder_path_destination, "train"))
    utils.createFolder(os.path.join(folder_path_destination, "validation"))
    utils.createFolder(os.path.join(folder_path_destination, "test"))

    ones_files = filter.getFilter("ones-big")
    # Get the list of file per group and shuffle it. Dataset 95% ones, 4% zeros-small, 1% zeros-big
    zeros_big_files = filter.getFilter("zeros-big")
    zeros_small_files = filter.getFilter("zeros-small")

    percentage_zeros_small = 0.04
    percentage_zeros_big = 0.01
    percetafe_ones = 0.95
    number_of_one_files = len(ones_files)
    number_of_total_files = number_of_one_files*(1/percetafe_ones)
    number_of_zeros_small_files = number_of_total_files*percentage_zeros_small
    number_of_zeros_big_files = number_of_total_files*percentage_zeros_big
    print("Number of ones files: " + str(number_of_one_files))
    print("Number of zeros-small files: " + str(number_of_zeros_small_files))
    print("Number of zeros-big files: " + str(number_of_zeros_big_files))
    print("Total number of files: " + str(number_of_total_files))

    np.random.shuffle(zeros_big_files)
    np.random.shuffle(zeros_small_files)
    zeros_small_files = zeros_small_files[:int(
        len(ones_files)/(.95)*percentage_zeros_small)]
    zeros_big_files = zeros_big_files[:int(
        len(ones_files)/(.95)*percentage_zeros_big)]

    files = ones_files + zeros_small_files + zeros_big_files

    np.random.shuffle(files)
    percentege = [0.8, 0.1, 0.1]

    files_train = files[:int(len(files)*percentege[0])]
    files_validation = files[int(
        len(files)*percentege[0]):int(len(files)*(percentege[0]+percentege[1]))]
    files_test = files[int(len(files)*(percentege[0]+percentege[1])):]
    moveFilesToFolder(files_train, folder_path_source,
                      os.path.join(folder_path_destination, "train"))
    moveFilesToFolder(files_validation, folder_path_source,
                      os.path.join(folder_path_destination, "validation"))
    moveFilesToFolder(files_test, folder_path_source,
                      os.path.join(folder_path_destination, "test"))

    # Create the folders train, validation and test
    print("Folder prepared data created")
    print("Prepared Data in " + folder_path_destination)


def moveFilesToFolder(files, folder_path_source, folder_path_destination):

    # Copy each file from the source folder to the destination folder
    for file in files:
        current_source = os.path.join(folder_path_source, file)
        current_destination = os.path.join(folder_path_destination, file)
        df = dataCleaning(current_source)
        df.to_csv(current_destination, index=False)

        print(f"Number of files in the folder {folder_path_destination} : " + str(
            len(os.listdir(folder_path_destination))))
