# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 11:03:34 2024

@author: Admin
"""
import json

# Function to process and restructure a recipe
def process_recipe(recipe):
    times = {
        'CookTime': recipe.pop('CookTime', None),
        'PrepTime': recipe.pop('PrepTime', None),
        'TotalTime': recipe.pop('TotalTime', None)
    }
    nutrition = {
        'Calories': recipe.pop('Calories', None),
        'FatContent': recipe.pop('FatContent', None),
        'SaturatedFatContent': recipe.pop('SaturatedFatContent', None),
        'CholesterolContent': recipe.pop('CholesterolContent', None),
        'SodiumContent': recipe.pop('SodiumContent', None),
        'CarbohydrateContent': recipe.pop('CarbohydrateContent', None),
        'FiberContent': recipe.pop('FiberContent', None),
        'SugarContent': recipe.pop('SugarContent', None),
        'ProteinContent': recipe.pop('ProteinContent', None)
    }
    recipe['Times'] = times
    recipe['Nutrition'] = nutrition
    recipe['Author'] = {'AuthorId': recipe.pop('AuthorId', None), 'AuthorName': recipe.pop('AuthorName', None)}
    recipe['RecipeIngredient'] = {'RecipeIngredientQuantities': recipe.pop('RecipeIngredientQuantities', None),
                                  'RecipeIngredientParts': recipe.pop('RecipeIngredientParts', None)}
    return recipe

# Function to process and write a bucket of recipes to the output file
def process_and_write_bucket(bucket, output_file):
    restructured_recipes = []
    for recipe in bucket:
        restructured_recipe = process_recipe(recipe)
        restructured_recipes.append(restructured_recipe)
    
    with open(output_file, 'a', encoding='utf-8') as file:
        for recipe in restructured_recipes:
            json.dump(recipe, file)
            file.write('\n')

# Function to read data in buckets from the input file
def read_in_buckets(file_path, bucket_size):
    with open(file_path, 'r', encoding='utf-8') as file:
        bucket = []
        for line in file:
            recipe = json.loads(line)
            bucket.append(recipe)
            if len(bucket) >= bucket_size:
                yield bucket
                bucket = []
        if bucket:
            yield bucket

# Input and output file paths
input_file = 'E:/SBP/novi.json'
output_file = 'E:/SBP/novi_restructured.json'

# Bucket size
bucket_size = 20000

# Read, process, and save data in batches
for bucket in read_in_buckets(input_file, bucket_size):
    process_and_write_bucket(bucket, output_file)

print("Podaci su uspešno prestrukturirani i sačuvani u novoj JSON datoteci korišćenjem baketiranja.")
