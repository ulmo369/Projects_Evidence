import os
import config as config
import pandas as pd
import DataUnderstandig.summary as summary_func
import shutil
import DataUnderstandig.plots as plots
from Utils import utils 
import numpy as np
# Decorator to calculate the execution time of a function



def summaryRedundanceCounts(path_folder, output_file_name):
    if not os.path.exists(path_folder):
        print("Error: path does not exist")
        return
    print("Creating "+output_file_name+" as output")
    print("Calculating redundance counts in "+path_folder)
    utils.calculate_time(summary_func.summary_redundance_counts)(
        path_folder, output_file_name)
    print("Redundance counts calculated")




def filterColumns(header):
    # Always include time that is in the first position
    columns_filter = [header[0]]
    print("Using "+header[0]+" column")
    for i in range(1, len(header), 2):
        print("Use "+header[i]+" ,discard "+header[i+1])
        columns_filter.append(header[i])
    return columns_filter
