import json
import re


# Define the path to the JSON file
guidelines_path = "./guidelines.json"

# Multiline string containing the updated value for requirements
new_requirements = """Given the following attack model, assign to every substep a 'Taxonomy' field choosing between one of these values: [Reconnaissance, Analysis, Exploitation], according to the following guidelines:
```
- Reconnaissance.

In this phase, attackers gather as much information as possible about the target to find ways to infiltrate the system. Activities in this phase usually involve identifying system components, observing behaviors, and discovering available information that can aid in the attack. It's more about scanning and discovering rather than exploiting or analyzing.

Keywords/Indicators:
    Observing
    Discovering
    Identifying (simple identification, no deep analysis)
    Navigating
    Visiting

Substep Example:
    "Visit the website."

- Analysis.

This phase is about in-depth scrutiny of the discovered information and observed behaviors. It involves studying the collected data, understanding system behaviors, identifying vulnerabilities, and planning the attack. It is more focused and detailed compared to the Reconnaissance phase but does not involve actual exploitation.

Keywords/Indicators:
    Analyzing
    Understanding
    Examining
    Studying
    Reviewing

Substep Example:
    "Analyze the source of checkpass.php to identify potential vulnerabilities."

- Exploitation.

This phase involves leveraging the identified vulnerabilities to gain unauthorized access or privileges in the system. It is about manipulating system behaviors, inputs, or functionalities to achieve the attacker’s goals. Here, the attacker uses the insights gained from the Analysis phase to perform actual attacks on the system.

Keywords/Indicators:
    Exploiting
    Manipulating
    Leveraging
    Injecting
    Executing

Substep Example:
    "Attempt to get a reverse shell using specific payload and replace with your server IP."

Applying the Taxonomy to Substeps.

When applying this taxonomy to the substeps, consider the primary focus of each substep. If a substep is mainly about observing and discovering, it falls under Reconnaissance. If it involves scrutinizing, studying, and understanding details or behaviors, it belongs to Analysis. And, if the substep involves utilizing vulnerabilities or functionalities to manipulate system behavior or gain unauthorized access, privileges, or information, it is considered Exploitation.

Consider the primary action and goal in each substep for accurate labeling. If a substep seems to contain elements of multiple categories, consider the predominant or final action or goal in that substep. For example, if a substep involves discovering information and then analyzing it, consider whether the discovery or the analysis is the primary focus of that substep.
```

Reply just with the JSON between backticks without adding anything else.

Here's the attack model:
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
    guidelines_data["requirements"]["requirements_taxl1"] = new_requirements
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
