# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 21:30:01 2024

@author: petro
"""

import json
import pandas as pd

# Paths to the files
recipes_file_path = 'E:/SBP/novi_restructured.json'
reviews_file_path = 'C:/Users/petro/Desktop/SBP Projekat/HRANA/reviews_neoptimizovano.csv'
output_file_path = 'E:/SBP/merged_recipes.json'

# Read the reviews CSV file into a DataFrame
reviews_df = pd.read_csv(reviews_file_path)

# Convert reviews DataFrame to a dictionary keyed by RecipeId
reviews_dict = {}
for _, row in reviews_df.iterrows():
    review = row.to_dict()
    recipe_id = review.pop('RecipeId')
    if recipe_id not in reviews_dict:
        reviews_dict[recipe_id] = []
    reviews_dict[recipe_id].append(review)

# Read the recipes JSON file
with open(recipes_file_path, 'r', encoding='utf-8') as file:
    recipes = [json.loads(line) for line in file]

# Add the reviews to each recipe
for recipe in recipes:
    recipe_id = recipe['RecipeId']
    recipe['Reviews'] = reviews_dict.get(recipe_id, [])

# Save the merged data to a new JSON file
with open(output_file_path, 'w', encoding='utf-8') as file:
    for recipe in recipes:
        json.dump(recipe, file)
        file.write('\n')

print("Recipes and reviews have been successfully merged and saved to the new JSON file.")
