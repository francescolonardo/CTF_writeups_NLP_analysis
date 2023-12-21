import os
import json

input_directory = "../data/list_substeps"
output_filename = "../data/groups.json"
miscellaneous_output_filename = "../data/group_miscellaneous.json"


def get_all_keys_from_file(file_path):
    with open(file_path, "r") as file:
        try:
            data = json.load(file)
            return data.keys()
        except json.decoder.JSONDecodeError as e:
            print(f"Error reading JSON file: {file_path}")
            raise e


def get_miscellaneous_strings(file_path):
    with open(file_path, "r") as file:
        try:
            data = json.load(file)
            return data.get("Miscellaneous", [])
        except json.decoder.JSONDecodeError as e:
            print(f"Error reading JSON file: {file_path}")
            raise e


def main():
    unique_keys = set()
    miscellaneous_strings = []
    processed_files = set()

    # Walk through directory and subdirectories
    for root, _, files in os.walk(input_directory):
        for file in files:
            if file.endswith("_grouped.json"):
                file_path = os.path.join(root, file)
                try:
                    keys = get_all_keys_from_file(file_path)
                    unique_keys.update(keys)

                    misc_strings = get_miscellaneous_strings(file_path)
                    miscellaneous_strings.extend(misc_strings)

                    processed_files.add(
                        file
                    )  # Add the grouped file to the processed_files set
                except json.decoder.JSONDecodeError as e:
                    print(f"Error processing file: {file_path}")
                    print(e)

    with open(output_filename, "w") as out_file:
        json.dump(list(unique_keys), out_file, indent=4)

    with open(miscellaneous_output_filename, "w") as out_file:
        json.dump(miscellaneous_strings, out_file, indent=4)

    print(f"Successfully saved to `{output_filename}`.")
    print(f"Successfully saved to `{miscellaneous_output_filename}`.")


if __name__ == "__main__":
    main()
