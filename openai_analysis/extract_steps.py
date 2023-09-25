import os
import json


# Function to recursively search for and collect "StepString" values from JSON files
def collect_step_strings(directory):
    step_strings = []

    # Traverse the directory and its subdirectories
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith("_steps.json"):
                file_path = os.path.join(root, filename)
                try:
                    with open(file_path, "r", encoding="utf-8") as json_file:
                        data = json.load(json_file)
                        attack_model = data.get("AttackModel")
                        if attack_model:
                            steps = attack_model.get("Steps")
                            if steps:
                                for step in steps:
                                    step_string = step.get("StepString")
                                    if step_string:
                                        step_strings.append(step_string)
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

    return step_strings


# Directory to start the search
start_directory = "../dataset_writeups"

# Collect steps
steps = collect_step_strings(start_directory)

# Write actions to a single output file
output_file = "steps.json"
with open(output_file, "w", encoding="utf-8") as output_json:
    json.dump(steps, output_json, ensure_ascii=False, indent=4)

print(f"Substeps collected and saved to `{output_file}`")
