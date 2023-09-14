import os
import subprocess
import json

# Specify the directory containing taxonomy JSON files
taxonomy_dir = "./taxonomy/taxonomy_categories"

# Iterate over the taxonomy files in the directory
for filename in os.listdir(taxonomy_dir):
    if filename.endswith(".json"):
        taxonomy_file_path = os.path.join(taxonomy_dir, filename)

        # Open the JSON file and load its contents
        with open(taxonomy_file_path, 'r') as json_file:
            data = json.load(json_file)

        # Extract the Category
        taxonomy_category = next(iter(data.keys()))  # Get the first (and only) key in the dictionary

        print(f"Updating taxonomy category: '{taxonomy_category}'")

        taxonomy_category_description = data[taxonomy_category]["Description"]

        # Call the main script with the taxonomy file as an argument
        subprocess.run(["python", "taxonomy_updater.py", taxonomy_file_path, taxonomy_category, taxonomy_category_description])
