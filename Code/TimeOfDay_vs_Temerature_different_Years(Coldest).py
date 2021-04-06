# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 21:02:58 2021

@author: Chethan
"""
# Importing necessary libraries
# import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Reading the required columns from csv file
df = pd.read_csv("C:/Users/Chethan/Desktop/Fraunhofer/LowestTemperatureYearWise.csv", usecols=[1,2])

# Task: Plot the temperatures for the coldest days of each provided year onto the same axis, over time of day.
times = []
years = []
temperatures = []
for index, row in df.iterrows():
    timestamp = str(int(row[0]))
    timeOfTheDay = timestamp[8:10]
    year = timestamp[0:4]
    
    times.append(timeOfTheDay)
    years.append(year)
    temperatures.append(row[1])
    
fig, ax = plt.subplots()
ax.scatter(times, temperatures)

for i, txt in enumerate(years):
    ax.annotate(txt, (times[i], temperatures[i]))

ax.set_xlabel('Time of the Day')
ax.set_ylabel('Temperature')

plt.savefig('C:/Users/Chethan/Desktop/Fraunhofer/Time_Temperature_Cold.png', dpi=300)


