import json
import os
import shutil
from random import shuffle

# Load the list of strings from the JSON file.
input_file = "list_substeps.json"
with open(input_file, "r", encoding="utf-8") as f:
    lines = json.load(f)

# Shuffle the list to mix the order of strings.
shuffle(lines)


def ensure_directory_exists(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)


# Define a function to split the list into chunks of 35 strings.
def chunk_list(input_list, chunk_size=35):
    for i in range(0, len(input_list), chunk_size):
        yield input_list[i : i + chunk_size]


# Define the output directory
output_dir = "list_substeps"

ensure_directory_exists(output_dir)

# Write each chunk to a new file.
for index, chunk in enumerate(chunk_list(lines)):
    start_index = index * 35 + 1
    end_index = start_index + len(chunk) - 1
    output_file = os.path.join(
        output_dir,
        f"list_substeps_{start_index:05d}-{end_index:05d}.json",  # Added formatting for leading zeroes
    )
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(chunk, f, indent=4)

print(
    "Splitting completed. The output files are located in the 'list_substeps' directory."
)
