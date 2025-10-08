import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os
import config as config
from Utils import filter as filter
# import dask.distributed
# import dask.dataframe as dd
import glob


def plot_ones(ones_csv, filter_name=None):
    path = config.CSV_PATH
    if not os.path.exists(path):
        print("Error: path does not exist")
        return
    print("Plotting ones from " + ones_csv + " in " + path)
    try:
        df = pd.read_csv(os.path.join(path, ones_csv))
        print("Read csv file successfully")
    except Exception as e:
        print("Error reading csv file: "+str(e))
        return

    if filter_name:
        filter = filter.getFilter(filter_name)
        print("Using filter", filter_name)
        df = df[df['name'].isin(filter)]
        print("Filter", filter_name, "applied")

    print(df.columns)
    plots_ones(df)
    print("Plot created")


def plots_ones(df):

    # Plot a histogram of weight ones
    print("Number of rows", df["rows"].sum())
    print("Number of ones", df["ones"].sum())
    print("Number of zeros", df["zeros"].sum())
    print("Percentage of ones", df["ones"].sum()/df["rows"].sum())
    df["contains_ones"] = df["ones"] > 0
    df["weightOnes"] = df["ones"] / df["rows"]
    # print(df.describe())

    # Plot a histogram of weight ones
    plt.figure(figsize=(8, 6))
    sns.histplot(df['weightOnes'])
    # Customize the plot (optional)
    plt.title('Histogram of weight ones')
    plt.xlabel('Weight ones')
    plt.ylabel('Frequency')
    # Show the plot
    plt.show()

    # Plot a histogram of weight ones vs num of rows
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x="weightOnes", y="rows", hue="contains_ones")
    # Customize the plot (optional)
    plt.title('Scatterplot of weight ones vs num of rows')
    plt.xlabel('Weight ones')
    plt.ylabel('Num of rows')
    # Show the plot
    plt.show()

    # plot line time vs row
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x="Final_time", y="rows")
    # Customize the plot (optional)
    plt.title('Lineplot of time vs rows')
    plt.xlabel('Time')
    plt.ylabel('Num of rows')
    # Show the plot
    plt.show()

    # plot zeros files distribution by rows size
    plt.figure(figsize=(8, 6))
    sns.histplot(df[df['contains_ones'] == False]['rows'])
    # Customize the plot (optional)
    plt.title('Histogram of zeros files distribution by rows size')
    plt.xlabel('Rows')
    plt.ylabel('Frequency')
    # Show the plot
    plt.show()

    # plot ones files distribution by rows size
    plt.figure(figsize=(8, 6))
    sns.histplot(df[df['contains_ones'] == True]['rows'])
    # Customize the plot (optional)
    plt.title('Histogram of ones files distribution by rows size')
    plt.xlabel('Rows')
    plt.ylabel('Frequency')
    # Show the plot
    plt.show()


def plotRedundance(redundance_csv):
    print("Plotting redundance from " +
          redundance_csv + " in " + config.CSV_PATH)
    df = pd.read_csv(os.path.join(config.CSV_PATH, redundance_csv))
    plot_redundance(df)
    print("Plot created")


def plot_redundance(df):
    # Plot error per pair of columns
    print("Original columns", df.columns)
    print("deleting columns", df.columns[[0, 1, 2, -1]])
    df_temp = df.drop(df.columns[[0, 1, 2, -1]], axis=1)

    plt.figure(figsize=(8, 6))
    sns.histplot(df['total_error'])
    # Customize the plot (optional)
    plt.title('Histogram of total error')
    plt.xlabel('Total error')
    plt.ylabel('Frequency')
    # Show the plot
    plt.show()

    print("Columns to plot pair of columns", df_temp.columns)
    df_temp = df_temp.describe().T
    df_temp["mean"]
    plt.figure(figsize=(8, 6))
    sns.barplot(x=df_temp.index, y=df_temp['mean'])
    plt.title('Erro per pair of column', fontsize=16)
    plt.xlabel('Columns', fontsize=14)
    plt.ylabel('Mean error', fontsize=14)
    plt.xticks(rotation=90)
    plt.show()

# Redundance counts


def plotRedundanceCounts(redundance_counts_csv):
    print("Plotting redundance counts from " +
          redundance_counts_csv + " in " + config.CSV_PATH)

    try:
        df = pd.read_csv(os.path.join(config.CSV_PATH, redundance_counts_csv))
        plot_redundance_counts(df)
        print("Plot created")
    except Exception as e:
        print("Error reading csv file: "+str(e))
        return

    print("Plot created")


def plot_redundance_counts(df):
    df_counts = df.groupby(['columns']).sum()

    # We get only errors caused by non-missing values
    df_counts['total_errors'] -= (df_counts['left_missing_errors'] +
                                  df_counts['right_missing_errors'])
    df_counts.rename(columns={"total_errors": "other_errors"}, inplace=True)

    sns.set(rc={'figure.figsize': (15, 5)})

    # Change datafreme format for barplot
    df_counts = pd.melt(df_counts.reset_index(), id_vars='columns',
                        var_name='error_type', value_name='error_count')

    sns.catplot(data=df_counts, x='columns', y='error_count',
                hue='error_type', kind='bar', height=2, aspect=4)

    plt.title('Error counts per pair of columns', fontsize=12)
    plt.xlabel('Columns', fontsize=2)
    plt.ylabel('Error counts', fontsize=8)
    plt.xticks(rotation=90)
    plt.show()


def plotInconsistenciesPer(df):

    # Selecciona la columna 'Porcentaje de Diferencia' para graficarla
    porcentaje_diferencia_columna = df['Porcentaje de Diferencia']

    # Crea un gráfico de barras para visualizar los porcentajes de diferencia
    plt.figure(figsize=(10, 6))
    porcentaje_diferencia_columna.plot(kind='bar', legend=False)
    plt.xlabel('No. Columnas')
    plt.ylabel('Diferencia')
    plt.title('Porcentaje de Diferencia entre Columnas')
    # Rota las etiquetas del eje x para mayor legibilidad
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_descriptive(descriptive_csv):
    print("Plotting inconsistencies from " +
          descriptive_csv + " in " + config.CSV_PATH)
    try:
        df = pd.read_csv(os.path.join(config.CSV_PATH, descriptive_csv))
    except Exception as e:
        print("Error reading csv file: "+str(e))
        return
    plotDescriptive(df)
    print("Plot created")


def plotDescriptive(df):
    df['class'] = ''
    filters = filter.read_dict()
    classes = ["ones-big", "ones-small", "zeros-big", "zeros-small"]
    for c in classes:
        df.loc[df['name'].isin(filters[c]), 'class'] = c

    df.set_index(['name', 'index'], inplace=True)

    variables = df.index.get_level_values('index').unique()
    n = len(variables)
    cols = 5
    rows = n // cols + (n % cols > 0)

    fig, axes = plt.subplots(rows, cols, figsize=(20, 5 * rows))

    for ax, var in zip(axes.ravel(), variables):
        data = df.loc[df.index.get_level_values('index') == var]

        sns.scatterplot(data=data, x='mean', y='std', hue='class',
                        palette='Set2', s=100, edgecolor='w', alpha=0.7, ax=ax)

        ax.set_title(f'Columna: {var}')
        ax.set_ylabel('Desviación Estándar')
        ax.set_xlabel('Media')
        ax.legend(title='Class', loc='upper left')

    for ax in axes.ravel()[n:]:
        ax.axis('off')

    plt.tight_layout()
    plt.show()


def plot_samplebyGroup(folder_path, columns_to_plot_wiht_time=[5, 6, 7], classes=["ones-big", "zeros-big"], number_of_samples=1):
    print("Plot of sample groups.\n Classes:")
    list_samples = filter.getRandomSampleList(classes, number_of_samples)
    print("list samples:", list_samples)
    for sample in list_samples:
        print(sample)
        plotSample(folder_path, classes, sample, columns_to_plot_wiht_time)

    # plotSample(folder_path,classes,file_lists,columns_to_plot_wiht_time)
    print("plots completed successfull")


def plotSample(folder_path, classes, file_list, columns_to_plot):
    print("Plotting sample", file_list)

    columns_index = list(set([int((e-1)/2) for e in columns_to_plot]))
    header = config.HEADER
    num_of_columns_to_plot = len(columns_to_plot)
    fig, axes = plt.subplots(num_of_columns_to_plot,
                             len(columns_index), figsize=(20, 10))
    # iteramos sobre las columnas que vamos a graficar
    for i in range(len(columns_index)):
        current_index_col = columns_index[i]
        column1 = header[current_index_col*2+1]
        column2 = header[current_index_col*2+2]
        column_time = header[0]
        print(column1)
        print(column2)
        print(column_time)
        # Flatten the axes for easy iteration
        # Get only the first file of each group
        for j in range(len(columns_index)):
            current_class = classes[j]
            current_file = file_list[j]
            print("Current class: " + current_class +
                  " current file: "+current_file)

            try:
                df = pd.read_csv(os.path.join(folder_path, current_file))
            except Exception as e:
                print("Error reading csv file: "+str(e))
                return
            print(str(i)+" , "+str(j))
            ax = axes[i, j]
            sns.lineplot(data=df, x=column_time,
                         y=column1, label=column1, ax=ax)
            sns.lineplot(data=df, x=column_time,
                         y=column2, label=column2, ax=ax)
            ax.set_title(current_class+" "+column1+"-"+column2+" vs time")
        # Adjusting the layout and showing the plot
    plt.tight_layout()
    plt.show()


def plotFileColumnsVsTime(folder_path, file_name="example1.csv", columns_to_plot=[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]):
    print("Ploting data of the file:" + file_name)
    print("plot the columns  " + str(columns_to_plot) + "Vs time")
    plotOneFile(folder_path, file_name, columns_to_plot)
    print("plots completed successfull")


def plotOneFile(folder_path, file_name, columns_to_plot):
    columns_index = list(set([int((e-1)/2) for e in columns_to_plot]))
    header = config.HEADER
    num_of_columns_to_plot = len(columns_index)
    num_col = 4
    fig, axes = plt.subplots(
        int((num_of_columns_to_plot-1)/num_col)+1, num_col, figsize=(20, 10))
    axes = axes.flatten()
    print("Creating plot of " +
          str(int((num_of_columns_to_plot-1)/num_col)+1)+" x "+str(num_col))
    # iteramos sobre las columnas que vamos a graficar
    for i in range(num_of_columns_to_plot):
        current_index_col = columns_index[i]
        column1 = header[current_index_col*2+1]
        column2 = header[current_index_col*2+2]
        column_time = header[0]
        print(column1)
        print(column2)
        print(column_time)
        # Flatten the axes for easy iteration
        # Get only the first file of each group
        try:
            df = pd.read_csv(os.path.join(folder_path, file_name))
        except Exception as e:
            print("Error reading csv file: "+str(e))
            return
        print(str(i))
        ax = axes[i]
        sns.lineplot(data=df, x=column_time, y=column1, label=column1, ax=ax)
        sns.lineplot(data=df, x=column_time, y=column2, label=column2, ax=ax)
        ax.set_title(column1+"-"+column2+" vs time")
        # Adjusting the layout and showing the plot
    plt.tight_layout()
    plt.show()


"""
def plotCorrelation(prepared_data_path):
    with dask.distributed.LocalCluster() as cluster, dask.distributed.Client(cluster) as client:
        csv_folder_path = prepared_data_path + '/*.csv'

        file_list = []

        for i, file_name in enumerate(glob.glob(csv_folder_path)):
            file_list.append(file_name)

        train_data = dd.read_csv(file_list)
        df_x_train = train_data.drop([config.BOOL_PREDICTION_VAR], axis=1)

        correlation_matrix = df_x_train.corr()

        # Graficamos la matriz de correlaciones
        plt.figure(figsize=(20, 16))
        sns.heatmap(correlation_matrix.compute(),
                    cmap="Blues", annot=True, fmt='.2f')
        plt.show()

    print('Completed execution')"""


def plot_histograms_ones_instances(ones_instances_csv):
    path = os.path.join(config.CSV_PATH, ones_instances_csv)
    print("Plotting ones instances histograms from " +
          ones_instances_csv + " in " + config.CSV_PATH)
    try:
        df = pd.read_csv(path)
    except Exception as e:
        print("Error reading csv file: "+str(e))
        return
    columns = df.columns
    columns = ["col1_boolean", "col5_float", "col7_float", "col11_float",
               "col17_float", "col21_float", "col25_float", "col35_integer"]
    df = df[columns]
    print(df.columns)
    plotHistograms(df)
    print("Plot created")


def plotHistograms(df):
    num_columns = len(df.columns)
    num_columns_per_row = 4

    # Calculate the number of rows needed
    num_rows = (num_columns + num_columns_per_row - 1) // num_columns_per_row

    # Create subplots
    fig, axes = plt.subplots(
        num_rows, num_columns_per_row, figsize=(15, 4 * num_rows))

    # Flatten the axes array to simplify indexing
    axes = axes.flatten()

    # Iterate through each column
    for i, column in enumerate(df.columns):
        # Plot the histogram
        sns.histplot(df[column], ax=axes[i])

        # Customize the plot (optional)
        axes[i].set_title('Histogram of ' + column)
        axes[i].set_xlabel('Value')
        axes[i].set_ylabel('Frequency')

    # Hide any empty subplots
    for j in range(num_columns, num_rows * num_columns_per_row):
        fig.delaxes(axes[j])

    # Adjust layout to prevent overlapping
    plt.tight_layout()

    # Show the plots
    plt.show()
