from Utils import dummies, filter, utils
from DataUnderstandig import du, plots, summary
import functions as f
import config
from DataPreparation.preparedFolder import createDataPreparedFolder
from Modeling import model_util, xgb_implementation, neural_network_implementation, logistic_model, lstm_implementation

# Name of the file that will contain the summary of the files
ones_summary_file = "summary_ones.csv"
csv_names_filtered = "filtered.csv"
redundance_file = "redundance.csv"
descriptive_file = "descriptive.csv"
redundance_counts_file = "redundance_counts.csv"
ones_instances_file = "ones_instances.csv"

DATA_FOLDER_PATH = config.TEST_PATH
TEST_DATA_FOLDER_PATH = config.TEST_PATH
DATA_PREPARED_PATH = config.DATA_PREPARED_PATH
TEST_RESULTS_FOLDER_PATH = config.RESULTS_PATH
MODEL_PATH = config.MODEL_PATH


def main():
    # filter.restartFilter(DATA_FOLDER_PATH)
    # filter.AddFilterSizeOnes(ones_summary_file)
    # dummies.clearFolders()
    # dummies.createTestFolder()
    # summary.summary_count_ones(config.TEST_PATH, "s1.csv")
    # plots.plot_ones("summary_ones-copia.csv")
    # summary.summaryRedundance(DATA_FOLDER_PATH, redundance_file)
    # plots.plotRedundance(redundance_file)
    # summary.onlyOnesInstaces(DATA_FOLDER_PATH, ones_instances_file)
    # summary.generateDescriptiveCsv(config.CSV_PATH, ones_instances_file)
    # summary.summaryDescriptiveStats(DATA_FOLDER_PATH,descriptive_file)
    # plots.plot_descriptive(descriptive_file)# Required the AdadFilterSizeOnes before to this script
    # plots.plotFileColumnsVsTime(DATA_FOLDER_PATH, "example1.csv", [1, 3])
    # plots.plot_samplebyGroup(DATA_FOLDER_PATH, [5, 7], classes=["ones-big", "zeros-big"],number_of_samples=2)
    # plots.plotCorrelation(TEST_DATA_FOLDER_PATH)

    # model_util.createModelFolders()
    # xgb_implementation.trainXGBModel(DATA_PREPARED_PATH, MODEL_PATH)
    # xgb_implementation.testXGBModel(DATA_PREPARED_PATH, MODEL_PATH)
    # xgb_implementation.generateXGBPredictions(NEW_TEST_DATA_PATH, MODEL_PATH, TEST_RESULTS_FOLDER_PATH)
    # neural_network_implementation.trainTFModel(DATA_PREPARED_PATH, MODEL_PATH)
    # neural_network_implementation.testTFModel(DATA_PREPARED_PATH, MODEL_PATH)
    # neural_network_implementation.generateTFPredictions(NEW_TEST_DATA_PATH, MODEL_PATH, TEST_RESULTS_FOLDER_PATH)

    # FALTAN POR MIGRAR:
    # summary.summaryRedundanceCounts(DATA_FOLDER_PATH, redundance_counts_file)
    # plots.plotRedundanceCounts(redundance_counts_file)
    # createDataPreparedFolder(DATA_FOLDER_PATH, DATA_PREPARED_PATH)
    # logistic_model.create_logistic_model()
    # lstm_implementation.trainTFModel(DATA_PREPARED_PATH, MODEL_PATH)
    lstm_implementation.testTFModel(DATA_PREPARED_PATH, MODEL_PATH)

    pass


if __name__ == "__main__":
    main()
