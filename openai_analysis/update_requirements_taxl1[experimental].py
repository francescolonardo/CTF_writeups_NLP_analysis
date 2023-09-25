import json
import re


# Define the path to the JSON file
guidelines_path = "./guidelines.json"

# Multiline string containing the updated value for "steps_requirements"
new_requirements = """Given the following attack model, assign to every substep a 'SubstepType' field choosing between one of these values: [Analysis, Exploitation], according to the following guidelines:
```
'Analysis': Information Gathering, Vulnerability Identification, and Analysis {
    Pre-emptive Reconnaissance and Identification {
        Observational Analysis: Gleaning insights into a target's components, structure, and functionalities for a comprehensive understanding and preliminary assessment.
    }
    Comprehensive Source Code Review {
        Logic & Functionality Dissection: Probing application source codes for logical structures, underlying functionalities, and potential weak points that might harbor vulnerabilities.
    }
    User Interaction and Behavioral Study {
        Anomaly Detection: Scrutinizing application interactions to detect unconventional patterns or outcomes arising from user interactions.
    }
    Network Infrastructure and Database Examination {
        Structural Investigation: Delving into the relational patterns of databases and the dialogues between clients and servers for vulnerabilities in communications and data storage.
    }
    Advanced Data Exploration and Interpretation {
        Sensitive Information Scrutiny: Interpreting acquired data intricately to unearth sensitive information or potential vulnerability points.
    }
    Configuration and Dependency Review {
        Detailed Assessment: Evaluating system setups, external dependencies, and their configurations to trace potential misconfigurations and weaknesses susceptible to exploitation.
    }
}

'Exploitation': Active Exploitation and Advanced Attack Implementation {
    Authentication Manipulation and Session Compromise {
        Security Bypassing: Manipulating authentication mechanics and session variables to sidestep security validations and gain unauthorized access.
    }
    Arbitrary Code Execution and Malicious Payload Deployment {
        Vulnerability Leveraging: Seizing the discovered vulnerabilities to execute arbitrary commands and insert harmful payloads, compromising the integrity of the target.
    }
    Sophisticated Web Attack Execution {
        Multi-Faceted Application Compromise: Implementing advanced web attacks, such as XSS and CSRF, to breach application security by exploiting identified vulnerabilities.
    }
    Client-Side Intervention and Manipulation {
        Browser and Request Exploitation: Leveraging client-side vulnerabilities and modifying request parameters to compromise client security.
    }
    Network Protocol Intrusion and Compromise {
        Protocol Vulnerability Exploitation: Utilizing weaknesses in various network protocols to breach network security and implement sophisticated attacks.
    }
    Implementation of Specialized Exploitation Techniques {
        Advanced Vulnerability Chaining: Applying intricate methods, innovative techniques, and specialized tools for complex vulnerability chaining and advanced payload crafting to compromise security on multiple levels.
    }
}
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
