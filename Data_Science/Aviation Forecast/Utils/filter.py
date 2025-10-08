
import os
import json
import config as config
import json
import random
import pandas as pd
import config as config
# Function to read the JSON file


def read_dict():
    path = os.path.join(config.CSV_PATH, "filter_dict.json")
    with open(path, 'r') as file:
        data = json.load(file)
        return data


def write_json_file(data):
    path = os.path.join(config.CSV_PATH, "filter_dict.json")
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)


def deleteFilter(name_filter):
    dict_filter = read_dict()
    if name_filter not in dict_filter.keys():
        print("Error: Filter", name_filter, "does not exist")
        return
    del dict_filter[name_filter]
    write_json_file(dict_filter)


def getFilter(name_filter):
    dict_filter = read_dict()
    if name_filter not in dict_filter.keys():
        print("Error: Filter", name_filter, "does not exist")
        return
    return dict_filter[name_filter]


def addFilter(df, name_filter):
    dict_filter = read_dict()
    if name_filter in dict_filter.keys():
        print("Error: Filter", name_filter, "already exists")
        return
    dict_filter[name_filter] = df['name'].tolist()
    write_json_file(dict_filter)




"""def restartFilter(path_folder):
    dict_filter = {}
    dict_filter['all'] = os.listdir(path_folder)
    write_json_file(dict_filter)"""


def getRandomSample(filter_names_list, num_of_samples):
    samples = {}
    dict_filter = read_dict()

    for filter_name in filter_names_list:
        print(type(dict_filter[filter_name]))
        list_of_names = (dict_filter[filter_name])
        random.shuffle(list_of_names)
        print(type(list_of_names))

        if (len(list_of_names) < num_of_samples):
            print("The filter name" + filter_name +
                  "has less elements than num of samples required")
        samples[filter_name] = list_of_names[:num_of_samples]
    return samples

# Given the filters an the number of samples return a matrix [ [exp1_g1,exp1_g2,exp1_g3], [exp2_g1,exp2_g2,exp2_g3] ...]


def getRandomSampleList(filter_names_list, num_of_samples):
    dict_filter = read_dict()
    suffle_list = []

    for filter_name in filter_names_list:
        print("Filter name content")
        list_of_group = list(dict_filter[filter_name])
        random.shuffle(list_of_group)
        #print(list_of_group)
        suffle_list.append(list_of_group)
    files_list = []
    for i in range(num_of_samples):
        current_list = []
        for j in range(len(filter_names_list)):
            print("SHUFFLE LIST")
            print(type(suffle_list))
            #print(suffle_list)
            print(suffle_list[j][i])
            current_list.append(suffle_list[j][i])
        files_list.append(current_list)
    return files_list

# This funciton returns an objetct with subsamples of the filters


def restartFilter(folder_path):
    print("Restarting filter in "+folder_path)
    dict_filter = {}
    dict_filter['all'] = os.listdir(folder_path)
    write_json_file(dict_filter)
    print("Filter restarted")


def AddFilterOnes(csv_file):
    print("Adding filter of ones in from "+csv_file)
    try:
        df = pd.read_csv(os.path.join(config.CSV_PATH, csv_file))
    except Exception as e:
        print("Error reading csv file: "+str(e))
        return
    # Filter the ones
    df_temp = df[df['ones'] > 0]
    # Add the filter
    addFilter(df_temp, "onlyOnes")
    # Filter the zeros
    df_temp = df[df['ones'] == 0]
    addFilter(df_temp, "onlyZeros")
    # Filter the zeros


def AddFilterSizeOnes(ones_csv):
    print("Adding filter of ones-size in from "+ones_csv)
    try:
        df = pd.read_csv(os.path.join(config.CSV_PATH, ones_csv))
    except Exception as e:
        print("Error reading csv file: "+str(e))
        return
    # smallest_ones_file_size=df[df['ones']>0]['rows'].min()
    smallest_ones_file_size = df[df['ones'] > 0]['rows'].min()
    print("The smallest file with ones has the size of " +
          str(smallest_ones_file_size))
    filter_ones_big = df[(df['ones'] > 0) & (
        df['rows'] >= smallest_ones_file_size)]
    filter_ones_small = df[(df['ones'] > 0) & (
        df['rows'] < smallest_ones_file_size)]
    filter_zeros_big = df[(df['ones'] == 0) & (
        df['rows'] >= smallest_ones_file_size)]
    filter_zeros_small = df[(df['ones'] == 0) & (
        df['rows'] < smallest_ones_file_size)]
    print("one-big:" + str(filter_ones_big.shape[0]))
    print("one-small:" + str(filter_ones_small.shape[0]))
    print("zero-big:" + str(filter_zeros_big.shape[0]))
    print("zero-small:" + str(filter_zeros_small.shape[0]))
    print("Total"+str(filter_ones_big.shape[0]+filter_ones_small.shape[0] +
          filter_zeros_big.shape[0]+filter_zeros_small.shape[0]))
    addFilter(filter_ones_big, "ones-big")
    addFilter(filter_ones_small, "ones-small")
    addFilter(filter_zeros_big, "zeros-big")
    addFilter(filter_zeros_small, "zeros-small")
