# CS-416_projdataset
Public dataset used for CS-416 Dashboard project(USA COVID-19 DASHBOARD)

The datasets used for CS-416 Dashboard projects are: 
1. merged_covid_data.csv: I have created this dataset using provided links from the project instruction.
   
Johns Hopkins University (World)- https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports_us                                            
This folder consists of statewise daily reports for every states of usa during pandemic.
I mergerd all the data to a single file(merged_covid_data.csv) using python code as follows. 


###################### CODE FOR MERGING ALL THE DATASETS TO A SINGLE DATASET #####################
import os
import pandas as pd

directory = '/Users/munssa01/Downloads/COVID-19-master/csse_covid_19_data/csse_covid_19_daily_reports_us'


dataframes = []

for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(directory, filename)
        df = pd.read_csv(file_path)
        # Extract date from filename (filename is something like '2020-01-01.csv')
        date = os.path.splitext(filename)[0]  # Removes the file extension
        # Add a new column for the date
        print(date)
        df['date_1'] = date
        # Append the DataFrame to the list
        dataframes.append(df)

merged_df = pd.concat(dataframes, ignore_index=True)

merged_df.to_csv('merged_covid_data.csv', index=False)

############################################################################################################

2. NH_CovidVaxAverages_20240526 : This public dataset is downloaded from https://data.cms.gov/provider-data/dataset/avax-cv19 website which shows statewise vaccination percentage as of 5/26/24.
