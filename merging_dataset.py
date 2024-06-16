import os
import pandas as pd

#Put your folder csse_covid_19_daily_reports_us location
directory = '/Users/munssa01/Downloads/COVID-19-master/csse_covid_19_data/csse_covid_19_daily_reports_us'

dataframes = []

for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(directory, filename)
        df = pd.read_csv(file_path)
        # Extract date from filename (filename is something like '2020-01-01.csv')
        date = os.path.splitext(filename)[0]  # Removes the file extension
        # Add a new column for the date
        df['date_1'] = date
        dataframes.append(df)

merged_df = pd.concat(dataframes, ignore_index=True)

merged_df.to_csv('merged_covid_data.csv', index=False)
