import json
import re


# Define the path to the JSON file
guidelines_path = "./guidelines.json"

# Multiline string containing the updated requirements
new_requirements = """Given the following CTF writeup, please detail, every step taken during the CTF challenge.
For each step, please keep all details clear and concise to maintain the utility of the information for future study and analysis on the attacker's steps.

Please, reply just with a JSON with a list without name, in which every line is filled just with the step string.
Please, avoid any step numbering.
Please, refrain from including anything in your response except the JSON.

Here's the CTF writeup:
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
    guidelines_data["requirements"]["requirements_presteps"] = new_requirements
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
