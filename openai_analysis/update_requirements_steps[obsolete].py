import json
import re


# Define the path to the JSON file
guidelines_path = "./guidelines.json"

# Multiline string containing the updated value for requirements
new_requirements = """Generate a comprehensive attack model from the following writeup summarization.

Use this JSON format as a guide:
{
    "AttackModel": {
        "Steps": [
            {
                "StepNumber": 1,
                "StepString": "Summarized step within the attack.",
            }
            // Add more steps as needed
        ]
    }
}

Reply just with the JSON between backticks without adding anything else.

Here's the writeup summarization:
"""

# Remove '\t', replace '\n' with ' ', and replace consecutive spaces with a single space
new_requirements = re.sub(r"\t", "", new_requirements)
new_requirements = re.sub(r"\n", " ", new_requirements)
new_requirements = re.sub(r"\s+", " ", new_requirements)

try:
    # Read existing JSON data from the file
    with open(guidelines_path, "r", encoding="utf-8") as guidelines_file:
        guidelines_data = json.load(guidelines_file)
    # Update the specific value you want to change
    guidelines_data["requirements"]["requirements_steps"] = new_requirements
    # Write the modified dictionary back to the JSON file
    with open(guidelines_path, "w", encoding="utf-8") as guidelines_file:
        json.dump(guidelines_data, guidelines_file, indent=4)
    print(f"{guidelines_path} updated successfully.")
except FileNotFoundError:
    print(f"JSON file not found: {guidelines_path}")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
