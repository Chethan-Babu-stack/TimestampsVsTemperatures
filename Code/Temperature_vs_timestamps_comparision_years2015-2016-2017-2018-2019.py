# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 23:05:59 2021

@author: Chethan
"""


# Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Reading the required columns from csv file
df = pd.read_csv("C:/Users/Chethan/Desktop/Fraunhofer/temperatures.csv", usecols=[2,3])

# Preprocessing: Add a new column year to access data easily later
df['Year'] = df.apply(lambda x: str(int(x.Zeitstempel))[0:4], axis=1)

# Different years in the dataset
years = list(dict.fromkeys(df["Year"]))

# Exluding year 2020 as it doesnot have the complete year data
years = years[0:5]

temperatures = []
timestamps = []

# Taking the dataframs of 2015 as 2015 is not a leap year
df2 = df[df["Year"] == years[0]]

# Create a list of timestamps as reference (year 2015)
# Leap years will have one extra day which is not taken into consideration
timestamps = df2["Zeitstempel"].to_numpy()


def temperaturesList(df, year):
    year = int(year)
    if year%4 == 0:
        temps = df['Wert'].to_numpy()
        indices = [i for i in range(1416,1440)]
        temps_new = np.delete(temps, indices)
        return temps_new
    else:
        temps = df['Wert'].to_numpy()
        return temps
        

# Loop through year by year data to get a list of temperatures
# Leap years February 29th temperatures are removed
for y in range(len(years)):
    df2 = df[df["Year"] == years[y]]
    l = temperaturesList(df2, years[y])
    temperatures.append(l)
    
    
    
# Timestamps displaying is making the graph very cluttered. Using numeric values instead of timestamps
timepoints = [i for i in range(0,len(timestamps))]


# Plotting temperature changes over first 100 timepoints to compare different years timepoints
# Plotting all data makes graph cluttered
for y in range(len(years)):
    plt.plot(timepoints[0:100], temperatures[y][0:100], label = years[y], marker='o')
    
plt.legend()
plt.savefig('C:/Users/Chethan/Desktop/Fraunhofer/comparing_initial_100timestamps.png')

    