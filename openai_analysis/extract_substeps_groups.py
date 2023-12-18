import os
import json

directory = "./list_substeps"


def get_all_keys_from_file(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
        return data.keys()


def main():
    unique_keys = set()
    processed_files = set()

    # Walk through directory and subdirectories
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith("_grouped.json"):
                file_path = os.path.join(root, file)
                keys = get_all_keys_from_file(file_path)
                unique_keys.update(keys)
                processed_files.add(
                    file
                )  # Add the grouped file to the processed_files set

    # Save unique keys to list_substeps_groups.json
    output_filename = "substeps_groups.json"
    with open(output_filename, "w") as out_file:
        json.dump(list(unique_keys), out_file, indent=4)

    print(f"Successfully saved to `{output_filename}`!")


if __name__ == "__main__":
    main()
