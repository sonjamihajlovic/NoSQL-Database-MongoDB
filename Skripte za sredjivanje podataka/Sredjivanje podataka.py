# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 15:58:12 2024

@author: petro
"""

#%%

import pandas as pd
import numpy as np



#%%

recipes = pd.read_csv('C:/Users/petro/Desktop/SBP Projekat/HRANA/recipes_export_sredjeno.csv')

#%%
reviews = pd.read_csv('C:/Users/petro/Desktop/SBP Projekat/HRANA/reviews.csv')

#%%

# Calculate the percentage of null values for each column using a loop
for column in recipes.columns:
    null_percentage = recipes[column].isnull().mean() * 100
    print(f"Percentage of null values in column '{column}': {null_percentage:.10f}%")
    
#%%

recipes = recipes.dropna(subset=['Keywords'])

#%%

print(len(recipes))

#%%

recipes['Images'] = recipes['Images'].replace('character(0)', '')

#%%

# Filter for rows where 'Images' is NaN
recipes_with_null_images = recipes[recipes['Images'].isnull()]

# Display the recipes with null images
print(recipes_with_null_images)

#%%

# Calculate the percentage of null values for each column using a loop
for column in reviews.columns:
    null_percentage = reviews[column].isnull().mean() * 100
    print(f"Percentage of null values in column '{column}': {null_percentage:.10f}%")
    
    
#%%
reviews = reviews.dropna(subset=['Review'])
    
#%%

# Export DataFrame to a CSV file
recipes.to_csv('recipes_neoptimizovano.csv', index=False)
    
#%%

# Export DataFrame to a CSV file
recipes.to_csv('recipes_neoptimizovano.csv', index=False)

#%%

# Export DataFrame to a CSV file
reviews.to_csv('reviews_neoptimizovano.csv', index=False)
    
    
#%%

print(reviews["Rating"].unique())
    
    
#%%
print(reviews.columns)
    
#%%

reviews = pd.read_csv('C:/Users/petro/Desktop/SBP Projekat/HRANA/reviews_neoptimizovano.csv')

#%%

reviewsss = recipes['RecipeIngredientParts'].unique()