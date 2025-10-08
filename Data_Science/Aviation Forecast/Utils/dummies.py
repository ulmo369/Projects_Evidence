import csv
import random
import os
import numpy as np
import config as config 
import shutil
from Utils import utils


def clearFolders():
    if (os.path.exists(config.TEST_PATH)):
        print("Deleting test_data folder")
        shutil.rmtree(config.TEST_PATH)
    if (os.path.exists(config.DUMMIES_PATH)):
        print("Deleting dummies_data folder")
        shutil.rmtree(config.DUMMIES_PATH)


    


def createTestFolder():
    utils.createFolder(config.TEST_PATH)  
    createData(config.NUM_TEST_FILES, config.SIZE_TEST_FILES, config.TEST_PATH)
    print("Test folder created successfully")
    


def createData(num_files, size_files, path):
    for i in range(num_files):
        name = 'example'+str(i)+'.csv'
        file_path = os.path.join(path, name)
        with open(file_path, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            header = config.HEADER
            csv_writer.writerow(header)
            data = createCsvData(random.randint(
                size_files*0.8, size_files*1.2))
            csv_writer.writerows(data)
            
target = 'target_boolean'
def createCsvData(size):
    header = config.HEADER
    cruice = random.choice([0, 1])
    data = []
    for i in range(size):
        newRegister = []
        for j in range(len(header)):
            if j == 0:
                newRegister.append(i)
            elif j < 4:
                newRegister.append(random.choice([0, 1]))
            elif j < 29:
                newRegister.append(random.gauss(5, 1))
            elif j < 31:
                if cruice == 1:
                    newRegister.append(random.choice([0, 1]))
                else:
                    newRegister.append(cruice)
            elif j < 36:
                newRegister.append(random.gauss(0, 1))
            else:
                newRegister.append(0)
        data.append(newRegister)
    return data



