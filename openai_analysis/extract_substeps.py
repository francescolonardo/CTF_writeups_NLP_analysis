import os
import json


# Function to recursively search for and collect "SubstepString" values from JSON files
def collect_substep_strings(directory):
    substep_strings = []

    # Traverse the directory and its subdirectories
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith("_substeps.json"):
                file_path = os.path.join(root, filename)
                try:
                    with open(file_path, "r", encoding="utf-8") as json_file:
                        data = json.load(json_file)
                        attack_model = data.get("AttackModel")
                        if attack_model:
                            steps = attack_model.get("Steps")
                            if steps:
                                for step in steps:
                                    substeps = step.get("Substeps")
                                    if substeps:
                                        for substep in substeps:
                                            substep_string = substep.get(
                                                "SubstepString"
                                            )
                                            if substep_string:
                                                substep_strings.append(substep_string)
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

    return substep_strings


# Directory to start the search
start_directory = "../dataset_writeups"

# Collect substeps
substeps = collect_substep_strings(start_directory)

# Write actions to a single output file
output_file = "substeps.json"
with open(output_file, "w", encoding="utf-8") as output_json:
    json.dump(substeps, output_json, ensure_ascii=False, indent=4)

print(f"Substeps collected and saved to `{output_file}`")
