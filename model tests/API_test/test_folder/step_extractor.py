import json
import os
import argparse

# Create a command-line argument parser
parser = argparse.ArgumentParser(description='Create separate JSON files for each step of the attack model.')
parser.add_argument('input_file', metavar='input_file', type=str, help='Path to the input JSON file')

# Parse the command-line arguments
args = parser.parse_args()

# Input JSON file path
input_file_path = args.input_file

# Check if the input file exists
if not os.path.isfile(input_file_path):
    print(f"Input file '{input_file_path}' does not exist.")
    exit(1)

# Determine the directory of the input file
input_dir = os.path.dirname(input_file_path)

# Load the JSON data from the input file
with open(input_file_path, 'r') as input_file:
    data = json.load(input_file)

# Extract the Steps from the AttackModel
steps = data['AttackModel']['Steps']

# Iterate over each step and create a new JSON file in the same directory
for step in steps:
    step_number = step['StepNumber']
    output_file_name = os.path.join(input_dir, f'step{step_number}.json')

    # Create a dictionary with the desired format
    step_data = {
        f'Step{step_number}': {
            "Description": step['Description'],
            "ToolsUsed": step['ToolsUsed'],
            "StepDetails": {
                "Hypothesis": step['StepDetails']['Hypothesis'],
                "Action": step['StepDetails']['Action'],
                "Result": step['StepDetails']['Result'],
                "Success": step['StepDetails']['Success'],
                "FailingReason": step['StepDetails']['FailingReason']
            }
        }
    }

    # Write the step data to a new JSON file in the same directory
    with open(output_file_name, 'w') as output_file:
        json.dump(step_data, output_file, indent=4)

print(f"Files created successfully in the same directory as '{input_file_path}'.")
