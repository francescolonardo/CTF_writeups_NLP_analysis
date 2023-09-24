import os
import json
import sys
from tqdm import tqdm
from api_caller import update_taxonomy

# Function to process a single text file and update the taxonomy
def process_txt_file(txt_file, taxonomy, taxonomy_category, taxonomy_category_description):
    try:
        with open(txt_file, 'r', encoding='utf-8') as f:
            writeup = f.read()
            updated_taxonomy = update_taxonomy(writeup, taxonomy, taxonomy_category, taxonomy_category_description)
        return updated_taxonomy
    except Exception as e:
        # Print the error message along with the file name
        print(f"Error processing file '{txt_file}': {e}")
        sys.exit(1)  # Exit the script with a non-zero status code

# Check if a command-line argument (taxonomy file) is provided
if len(sys.argv) != 4:
    print("Usage: python main_script.py <taxonomy_file.json> <taxonomy_category> <taxonomy_category_description>")
    sys.exit(1)

# Get the taxonomy file path from the command-line argument
taxonomy_file = sys.argv[1]

# Get the taxonomy category from the command-line argument
taxonomy_category = sys.argv[2]

# Get the taxonomy category description from the command-line argument
taxonomy_category_description = sys.argv[3]


# Load the initial taxonomy from the specified JSON file
try:
    with open(taxonomy_file, 'r', encoding='utf-8') as t:
        initial_taxonomy = json.load(t)
except Exception as e:
    print(f"Error loading the taxonomy JSON file: {e}")
    initial_taxonomy = {}  # Set an empty taxonomy as a fallback

# Specify the folder containing .txt files
txt_folder = "./txt_writeups/"

# Get a list of .txt files in the folder
txt_files = []
for root, _, files in os.walk(txt_folder):
    for filename in files:
        if filename.endswith(".txt"):
            txt_files.append(os.path.join(root, filename))

# Print the number of .txt files in the folder
print(f"Number of .txt files in the folder: {len(txt_files)}")

# Initialize the progress bar
with tqdm(total=len(txt_files), desc="Processing Files") as pbar:
    # Iterate through .txt files in the folder and update the taxonomy

    updated_taxonomy = initial_taxonomy  # Initialize the updated taxonomy
    for txt_file in txt_files:
        updated_taxonomy = process_txt_file(txt_file, updated_taxonomy, taxonomy_category, taxonomy_category_description)
        pbar.update(1)  # Update the progress bar

# Save the final updated taxonomy back to the original JSON file
try:
    with open(taxonomy_file, 'w', encoding='utf-8') as t:
        json.dump(updated_taxonomy, t, indent=4)
except Exception as e:
    print(f"Error saving the taxonomy JSON file: {e}")
    sys.exit(1)  # Exit the script with a non-zero status code if there's an error

print(f"Updated taxonomy saved to '{taxonomy_file}' successfully.")
