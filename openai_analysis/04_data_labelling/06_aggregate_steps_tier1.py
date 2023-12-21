import os
import json
from collections import defaultdict

# Placeholder for the directory to scan
scan_directory = "../data/dataset_writeups"  # TODO: Replace with your directory path


# Function to merge JSON content from all files into a single list of contents
def merge_json_contents(files):
    merged_content = []
    for file_path in files:
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
            # Append the content if it's a list, otherwise wrap it in a list
            merged_content.extend(data if isinstance(data, list) else [data])
    return merged_content


# Function to create JSON file with the merged content
def create_json_file(directory, base_name, content):
    file_name = f"{base_name}_tier1.json"
    file_path = os.path.join(directory, file_name)
    with open(file_path, "w") as f:
        json.dump({"AttackModel": {"Steps": content}}, f, indent=4)
    print(f"File saved: {file_path}")


# Function to check if all tier1 files exist based on the count of substeps files
def all_tiers_exist(substeps_count, tier_files):
    # Create a set of expected tier file names based on the count of substeps files
    expected_files = {
        f"_substeps_{str(i).zfill(2)}_tier1.json" for i in range(1, substeps_count + 1)
    }
    # Return True if all expected tier files are found in the tier_files list
    return expected_files.issubset(set(tier_files))


# Function to scan directories and process files
def process_directories(directory):
    # Dictionary to keep track of each substeps folder and its files
    substeps_folders = defaultdict(lambda: {"substeps_files": [], "tier_files": []})

    # Walk through the directory to find all *_substeps folders and their JSON files
    for root, dirs, files in os.walk(directory):
        for dir_name in dirs:
            if dir_name.endswith("_substeps"):
                substeps_path = os.path.join(root, dir_name)
                # List of all files in this substeps directory
                all_files = os.listdir(substeps_path)
                # Filter and collect files that match the patterns
                substeps_files = [f for f in all_files if f.endswith("_substeps.json")]
                tier_files = [f for f in all_files if f.endswith("_tier1.json")]
                substeps_folders[substeps_path]["substeps_files"] = substeps_files
                substeps_folders[substeps_path]["tier_files"] = tier_files

    # Process each substeps folder
    for substeps_path, files_dict in substeps_folders.items():
        substeps_files = files_dict["substeps_files"]
        tier_files = files_dict["tier_files"]

        # Check if the number of tier1 files matches the number of substeps files
        if all_tiers_exist(len(substeps_files), tier_files):
            # Full paths of tier1 json files
            tier_file_paths = [os.path.join(substeps_path, f) for f in tier_files]
            merged_content = merge_json_contents(tier_file_paths)

            # Parent directory of the substeps folder
            parent_directory = os.path.abspath(os.path.join(substeps_path, os.pardir))
            # Base name for the output file
            base_name = os.path.basename(substeps_path).replace("_substeps", "")
            # Create the output JSON file with the merged content
            create_json_file(parent_directory, base_name, merged_content)


# Run the process
process_directories(scan_directory)
# Please ensure to replace 'path/to/your/directory' with the actual path of the directory to scan.
