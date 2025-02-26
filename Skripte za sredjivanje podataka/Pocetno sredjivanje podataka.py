# -*- coding: utf-8 -*-
"""
Created on Sat May 25 14:30:28 2024

@author: petro
"""

import pandas as pd
import numpy as np

recipes = pd.read_csv('C:/Users/petro/Desktop/SBP Projekat/HRANA/recipes.csv')
reviews = pd.read_csv('C:/Users/petro/Desktop/SBP Projekat/HRANA/reviews.csv')

#%% 
# Print column names and their data types
for column in recipes.columns:
    print(f"Column: {column}, Type: {recipes[column].dtype}")
    
#%%
# Print column names and their data types
for column in reviews.columns:
    print(f"Column: {column}, Type: {reviews[column].dtype}")
    
#%%

for column in reviews.columns:
    print(f"{column}")
    
#%%

for column in recipes.columns:
    print(f"{column}")
    
#%%
temp = recipes['RecipeCategory'].unique()

category_counts = recipes['RecipeCategory'].value_counts()

#%%

cook_times = recipes['CookTime'].unique()

#%%

reviewsss = recipes['ReviewCount'].unique()

#%%

recipe_servings = recipes['RecipeServings'].unique()

#%%
recipes['DatePublished'] = pd.to_datetime(recipes['DatePublished'], format='%Y-%m-%dT%H:%M:%SZ')
unique_years = recipes['DatePublished'].dt.year.unique()



#%%

temp = recipes.head(1)
print(temp.to_json())

#%%

temp = reviews.head(1)
print(temp.to_json())

#%%

# Calculate the percentage of null values for each column using a loop
for column in recipes.columns:
    null_percentage = recipes[column].isnull().mean() * 100
    print(f"Percentage of null values in column '{column}': {null_percentage:.10f}%")

#%%
# Calculate the number of null values in the CookTime column
null_count = recipes['CookTime'].isnull().sum()

# Calculate the total number of instances in the recipes DataFrame
total_count = len(recipes)

# Calculate the percentage of null values in the CookTime column
null_percentage = (null_count / total_count) * 100

# Print the results
print(f"Number of null values in 'CookTime' column: {null_count}")
print(f"Percentage of null values in 'CookTime' column: {null_percentage:.2f}%")

#%%

# Calculate the number of null values in the CookTime column
null_count = recipes['AggregatedRating'].isnull().sum()

# Calculate the total number of instances in the recipes DataFrame
total_count = len(recipes)

# Calculate the percentage of null values in the CookTime column
null_percentage = (null_count / total_count) * 100

# Print the results
print(f"Number of null values in 'AggregatedRating' column: {null_count}")
print(f"Percentage of null values in 'AggregatedRating' column: {null_percentage:.2f}%")

#%%

# Calculate the number of null values in the CookTime column
null_count = recipes['ReviewCount'].isnull().sum()

# Calculate the total number of instances in the recipes DataFrame
total_count = len(recipes)

# Calculate the percentage of null values in the CookTime column
null_percentage = (null_count / total_count) * 100

# Print the results
print(f"Number of null values in 'ReviewCount' column: {null_count}")
print(f"Percentage of null values in 'ReviewCount' column: {null_percentage:.2f}%")

#%%

# Calculate the number of null values in the CookTime column
null_count = recipes['RecipeServings'].isnull().sum()

# Calculate the total number of instances in the recipes DataFrame
total_count = len(recipes)

# Calculate the percentage of null values in the CookTime column
null_percentage = (null_count / total_count) * 100

# Print the results
print(f"Number of null values in 'RecipeServings' column: {null_count}")
print(f"Percentage of null values in 'RecipeServings' column: {null_percentage:.2f}%")

#%%

# Calculate the number of null values in the CookTime column
null_count = recipes['RecipeYield'].isnull().sum()

# Calculate the total number of instances in the recipes DataFrame
total_count = len(recipes)

# Calculate the percentage of null values in the CookTime column
null_percentage = (null_count / total_count) * 100

# Print the results
print(f"Number of null values in 'RecipeYield' column: {null_count}")
print(f"Percentage of null values in 'RecipeYield' column: {null_percentage:.2f}%")

#%%

recipes = recipes.drop(columns=['RecipeYield'])

#%%

recipes = recipes.dropna(subset=['RecipeIngredientQuantities'])

#%%

# Replace null values in the 'RecipeCategory' column with 'Unknown'
recipes['RecipeCategory'].fillna('Unknown', inplace=True)

#%%

recipes['CookTime'].fillna('PT3H35M', inplace=True)


#%%

print(recipes['AggregatedRating'].mean())

#%%

recipes['ReviewCount'].fillna(68, inplace=True)

#%%

recipes['RecipeServings'].fillna(5, inplace=True)

#%%


# Calculate the percentage of null values for each column using a loop
for column in reviews.columns:
    null_percentage = reviews[column].isnull().mean() * 100
    print(f"Percentage of null values in column '{column}': {null_percentage:.10f}%")

#%%

# Export DataFrame to a CSV file
recipes.to_csv('recipes_export.csv', index=False)

#%%

print(list(reviews.columns))

#%%

# Calculate the percentage of null values for each column using a loop
for column in reviews.columns:
    null_percentage = reviews[column].isnull().mean() * 100
    print(f"Percentage of null values in column '{column}': {null_percentage:.10f}%")















