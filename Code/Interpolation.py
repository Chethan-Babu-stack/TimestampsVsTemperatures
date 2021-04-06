# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 21:23:18 2021

@author: Chethan
"""

# Importing necessary libraries
import pandas as pd

# Task: Convert the time steps of the temperature data to 15-minutes-intervals, using interpolation.

# Reading the required columns from csv file
df = pd.read_csv("C:/Users/Chethan/Desktop/Fraunhofer/temperatures.csv", usecols=[2,3])

timestamps = df['Zeitstempel'].to_numpy()
temperatures = df['Wert'].to_numpy()

timestamps2 = []
for i in range(len(timestamps)):
    timestamps2.append(timestamps[i])
    if i+1 < len(timestamps):
        timestamps2.append(int(timestamps[i]) + 15)
        timestamps2.append(int(timestamps[i]) + 30)
        timestamps2.append(int(timestamps[i]) + 45)
    
temperatures2 = []
for i in range(len(temperatures)):
    temperatures2.append(temperatures[i])
    if i+1 < len(temperatures):
        first = temperatures[i]
        last = temperatures[i+1]
        
        # Interpolation of temperatures
        mid = (first + last)/2
        quarter = (first + mid)/2
        threeQuarter = (mid + last)/2
        
        temperatures2.append(quarter)
        temperatures2.append(mid)
        temperatures2.append(threeQuarter)
        
# Creating a new dataframe for interpolated data
df2 = pd.DataFrame({'Timestamp': timestamps2, 'Temperature': temperatures2})

# Save the dataframe with interpolated data
df2.to_csv('C:/Users/Chethan/Desktop/Fraunhofer/InterpolatedTo15Mins.csv', sep=',')
