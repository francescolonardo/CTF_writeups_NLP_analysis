import os
import json
import re

input_directory = "./substeps_groups_tier1"  # Adjusted to the desired input directory
output_directory = "./substeps_groups_tier1"


def extract_tier1_category_from_filename(filename):
    """Extract the tier1 category name from the filename."""
    match = re.match(r"substeps_groups_tier1_(.*?).json", filename)
    return match.group(1) if match else None


def split_and_save(data, category_name):
    """Split the data into chunks of 75 and save them."""  # Updated comment
    category_output_dir = os.path.join(output_directory, category_name)

    # Ensure the category output directory exists
    if not os.path.exists(category_output_dir):
        os.makedirs(category_output_dir)

    # Split data into chunks of 75
    for i in range(0, len(data), 75):  # Adjusted to 75
        chunk = data[i : i + 75]  # Adjusted to 75
        start_index = i + 1
        end_index = i + len(chunk)
        output_filename = f"substeps_groups_tier1_{start_index:04}-{end_index:04}.json"
        output_path = os.path.join(category_output_dir, output_filename)

        # Save the chunk to a file
        with open(output_path, "w") as out_file:
            json.dump(chunk, out_file, indent=4)


def main():
    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for file in os.listdir(input_directory):
        if file.startswith("substeps_groups_tier1_") and file.endswith(".json"):
            category_name = extract_tier1_category_from_filename(file)
            if category_name:
                with open(os.path.join(input_directory, file), "r") as in_file:
                    data = json.load(in_file)
                split_and_save(data, category_name)

    print(f"Successfully split and saved the data to `{output_directory}`!")


if __name__ == "__main__":
    main()
