import os
import json
import traceback  # For improved error logging


# Function to recursively search for and collect "SubstepString" values from JSON files
def collect_substep_strings(directory):
    substep_strings_analysis = []
    substep_strings_exploitation = []

    # Traverse the directory and its subdirectories
    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            # Check whether the path is a file before processing it
            if os.path.isfile(file_path) and filename.endswith("_taxl1.json"):
                try:
                    with open(file_path, "r", encoding="utf-8") as json_file:
                        data = json.load(json_file)
                        # Navigating JSON structure defensively to avoid TypeErrors
                        attack_model = data.get("AttackModel", {})
                        steps = attack_model.get("Steps", [])
                        for step in steps:
                            substeps = step.get("Substeps", [])
                            for substep in substeps:
                                substep_type = substep.get("SubstepType")
                                substep_string = substep.get("SubstepString")
                                if substep_string:
                                    if substep_type == "Analysis":
                                        substep_strings_analysis.append(substep_string)
                                    elif substep_type == "Exploitation":
                                        substep_strings_exploitation.append(
                                            substep_string
                                        )
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")
                    traceback.print_exc()  # Print the full traceback

    return substep_strings_analysis, substep_strings_exploitation


# Directory to start the search
start_directory = "../dataset_writeups"

# Collect substeps
substeps_analysis, substeps_exploitation = collect_substep_strings(start_directory)

# Write substeps to output files  # Updated comment
output_file_analysis = "substeps_analysis.json"
output_file_exploitation = "substeps_exploitation.json"
with open(output_file_analysis, "w", encoding="utf-8") as output_json:
    json.dump(substeps_analysis, output_json, ensure_ascii=False, indent=4)
with open(output_file_exploitation, "w", encoding="utf-8") as output_json:
    json.dump(substeps_exploitation, output_json, ensure_ascii=False, indent=4)

print(f"Substeps collected and saved to `{output_file_analysis}`")
print(f"Substeps collected and saved to `{output_file_exploitation}`")
