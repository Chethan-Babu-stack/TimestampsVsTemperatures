# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 17:39:03 2021

@author: Chethan
"""

# Importing necessary libraries
import pandas as pd


# Reading the required columns from csv file
df = pd.read_csv("C:/Users/Chethan/Desktop/Fraunhofer/temperatures.csv", usecols=[2,3])

# Preprocessing: Add a new column year to access data easily later
df['Year'] = df.apply(lambda x: str(int(x.Zeitstempel))[0:4], axis=1)

# Task: Find the hottest and coldest temperature values for every year and their time of occurrence.
# Store this information in a human-readable file (csv or other text file or graphic).
def lowHighTempPerYear(df):
    lowest_temp = 999
    highest_temp = -999
    
    for index, row in df.iterrows():
        temperature = row[1]
        
        if temperature < lowest_temp:
            lowest_temp = temperature
            lowest_timestamp = row[0]
        if temperature > highest_temp:
            highest_temp = temperature
            highest_timestamp = row[0]
            
    return [[int(lowest_timestamp), lowest_temp], [int(highest_timestamp), highest_temp]]

# Different years in the dataset
years = list(dict.fromkeys(df["Year"]))

least_temp_list = []
highest_temp_list = []

# Loop through year by year data and find coldest, hottest temperatures
for y in range(len(years)):
    df2 = df[df["Year"] == years[y]]
    l = lowHighTempPerYear(df2)
    least_temp_list.append(l[0])
    highest_temp_list.append(l[1])
    
    
# Creating two dataframes
least_temp_df = pd.DataFrame(least_temp_list, columns = ['Timestamp', 'LeastTemp'])
highest_temp_df = pd.DataFrame(highest_temp_list, columns = ['Timestamp', 'HighestTemp'])
        

# Saving the plot with Timestamp on x-axis 
plot = least_temp_df.plot(x='Timestamp', y='LeastTemp',marker='o', color='b')
fig = plot.get_figure()
fig.savefig('C:/Users/Chethan/Desktop/Fraunhofer/LowestTemperatureYearWise.png')

plot = highest_temp_df.plot(x='Timestamp', y='HighestTemp',marker='o', color='g')
fig = plot.get_figure()
fig.savefig('C:/Users/Chethan/Desktop/Fraunhofer/HighestTemperatureYearWise.png')


# Saving the results in excel
least_temp_df.to_csv('C:/Users/Chethan/Desktop/Fraunhofer/LowestTemperatureYearWise.csv', sep=',')
highest_temp_df.to_csv('C:/Users/Chethan/Desktop/Fraunhofer/HighestTemperatureYearWise.csv', sep=',')




