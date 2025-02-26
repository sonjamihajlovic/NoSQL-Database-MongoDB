# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 00:25:00 2024

@author: petro
"""
#%%
import pandas as pd
import re
import numpy as np
#%%
# Read the CSV file into a DataFrame
recipes = pd.read_csv('C:/Users/petro/Desktop/SBP Projekat/HRANA/recipes_export.csv')

#%%

print(recipes['PrepTime'].unique())

#%%

def convert_to_minutes(time_str):
    hours = 0
    minutes = 0
    match = re.match(r'PT(?:(\d+)H)?(?:(\d+)M)?', time_str)
    if match:
        if match.group(1):
            hours = int(match.group(1))
        if match.group(2):
            minutes = int(match.group(2))
    total_minutes = hours * 60 + minutes
    return total_minutes

# Apply the conversion function to the 'CookTime' column and update the column directly
recipes['PrepTime'] = recipes['PrepTime'].apply(convert_to_minutes)

#%%

# Convert values greater than 4320 to a random value between 120 and 2200
recipes['PrepTime'] = recipes['PrepTime'].apply(lambda x: np.random.randint(120, 2201) if x > 4320 else x)

#%%

# Convert values greater than 4320 to a random value between 120 and 2200
recipes['PrepTime'] = recipes['PrepTime'].apply(lambda x: np.random.randint(30, 600) if x > 1440 else x)

#%%

# Update 'TotalTime' as the sum of 'PrepTime' and 'CookTime'
recipes['TotalTime'] = recipes['PrepTime'] + recipes['CookTime']

#%%

#%%

# Export DataFrame to a CSV file
recipes.to_csv('recipes_export_sredjeno.csv', index=False)










