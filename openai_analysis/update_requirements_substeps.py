import json
import re


# Define the path to the JSON file
guidelines_path = "./guidelines.json"

# Multiline string containing the updated value for "requirements_substeps"
new_requirements = """Precisely refine the provided attack model, disaggregating each step into the single actions taken in the step wherever applicable. If disaggregating a step into separate actions is not viable, abstain from adding a Substeps list for that particular step, and instead include a singular Substep with the original "StepString" value as the value of "SubstepString". I want that each step is divided in substeps.

Please strictly conform to the specified JSON format to structure the OUTPUT:
{
    "AttackModel": {
        "Steps": [
            {
                "StepNumber": 1,
                "StepString": "Concise synopsis of the primary action within the attack.",
                "Substeps": [
                    {
                        "SubstepNumber": 1.1,
                        "SubstepString": "Terse description of the individual action undertaken in this step.",
                    }
                    // Incorporate more single action-specific substeps as required
                ]
            }
            ...
        ]
    }
}

Return only the refined JSON surrounded by backticks, and assure no supplementary content or commentary is integrated.

Below is the INPUT attack model to be refined, and it is imperative that the values of "StepString" are retained:
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
    guidelines_data["requirements"]["requirements_substeps"] = new_requirements
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
