# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 18:07:57 2024

@author: petro
"""
import json
import os

def compute_fields(recipe):
    # Extract nutritional values from the Nutrition column
    nutrition = recipe.get("Nutrition", {})
    protein_content = float(nutrition.get("ProteinContent", 0))
    fat_content = float(nutrition.get("FatContent", 1))  # Avoid division by zero by defaulting to 1
    sugar_content = float(nutrition.get("SugarContent", 0))
    cholesterol_content = float(nutrition.get("CholesterolContent", 0))
    sodium_content = float(nutrition.get("SodiumContent", 0))

    # Compute ProteinToFatRatio and round to 2 decimals
    protein_to_fat_ratio = round(protein_content / fat_content, 2) if fat_content != 0 else 0.0
    recipe["ProteinToFatRatio"] = protein_to_fat_ratio

    # Compute IsHealthy field
    recipe["IsHealthy"] = not (sugar_content > 100 or fat_content > 200 or cholesterol_content > 100 or sodium_content > 4000)

    return recipe, protein_to_fat_ratio, recipe["IsHealthy"]

def process_recipes(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        recipes = [json.loads(line) for line in file]

    protein_to_fat_ratios = set()
    healthy_count = 0
    unhealthy_count = 0

    for i, recipe in enumerate(recipes):
        recipes[i], protein_to_fat_ratio, is_healthy = compute_fields(recipe)
        protein_to_fat_ratios.add(protein_to_fat_ratio)
        if is_healthy:
            healthy_count += 1
        else:
            unhealthy_count += 1

    # Save the modified recipes to a new JSON file
    with open(output_file, 'w', encoding='utf-8') as file:
        for recipe in recipes:
            json.dump(recipe, file)
            file.write('\n')

    # Print distinct values and counts
    print(f"Distinct ProteinToFatRatios: {sorted(protein_to_fat_ratios)}")
    print(f"Number of healthy recipes: {healthy_count}")
    print(f"Number of unhealthy recipes: {unhealthy_count}")

# Paths to the files
input_file_path = 'E:/SBP/merged_recipes.json'
output_file_path = 'E:/SBP/final_recipes.json'

# Process the recipes
process_recipes(input_file_path, output_file_path)
