import os
import json


def rename_fields(data):
    if "AttackModel" in data and "Steps" in data["AttackModel"]:
        for step in data["AttackModel"]["Steps"]:
            # Rename 'StepKey' to 'StepNumber'
            if "StepKey" in step:
                step["StepNumber"] = step.pop("StepKey")
            # Rename 'StepValue' to 'StepString'
            if "StepValue" in step:
                step["StepString"] = step.pop("StepValue")
    return data


def process_directory(dir_path):
    # Walk through directory and subdirectories
    for foldername, subfolders, filenames in os.walk(dir_path):
        for filename in filenames:
            if filename.endswith("_steps.json"):
                filepath = os.path.join(foldername, filename)
                with open(filepath, "r", encoding="utf-8") as file:
                    try:
                        data = json.load(file)
                    except json.JSONDecodeError as e:
                        print(f"Error decoding JSON in {filepath}: {e}")
                        continue

                # Rename fields in the JSON object
                modified_data = rename_fields(data)

                # Write the modified JSON object back to the file
                with open(filepath, "w", encoding="utf-8") as file:
                    json.dump(modified_data, file, indent=4)


if __name__ == "__main__":
    dir_path = "../dataset_writeups"  # Current directory. Change this to the directory you want to scan
    process_directory(dir_path)
