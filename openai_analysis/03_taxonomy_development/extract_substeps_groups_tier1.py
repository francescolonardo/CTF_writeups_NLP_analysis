import os
import json
import re

directory = "./list_substeps_tier1"
output_directory = "./substeps_groups_tier1"


def get_all_keys_from_file(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
        return data.keys()


def extract_tier1_category_from_filename(filename):
    # Extracts the tier1 category name from the filename
    match = re.match(r"list_substeps_tier1_(.*?)_.*_grouped.json", filename)
    return match.group(1) if match else None


def main():
    # Use a dictionary to group keys by their tier1 category name
    keys_by_category = {}
    processed_files = set()

    # Create output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Walk through directory and subdirectories
    for root, dirs, files in os.walk(directory):
        # Skip the root directory
        if root == directory:
            continue

        for file in files:
            if file.endswith("_grouped.json"):
                tier1_category_name = extract_tier1_category_from_filename(file)
                if tier1_category_name:
                    file_path = os.path.join(root, file)
                    keys = get_all_keys_from_file(file_path)

                    # Add the keys to the corresponding category set
                    if tier1_category_name not in keys_by_category:
                        keys_by_category[tier1_category_name] = set()
                    keys_by_category[tier1_category_name].update(keys)

                    processed_files.add(
                        file
                    )  # Add the grouped file to the processed_files set

    # Save unique keys for each category to individual files in the output_directory
    for category, unique_keys in keys_by_category.items():
        output_filename = os.path.join(
            output_directory, f"substeps_groups_tier1_{category}.json"
        )
        with open(output_filename, "w") as out_file:
            json.dump(list(unique_keys), out_file, indent=4)
        print(f"Successfully saved to `{output_filename}`!")


if __name__ == "__main__":
    main()
