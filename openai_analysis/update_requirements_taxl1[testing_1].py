import json
import re


# Define the path to the JSON file
guidelines_path = "./guidelines.json"

# Multiline string containing the updated value for requirements
new_requirements = """Given the following input JSON, try to label each of its substeps, assigning to every substep the 'SubstepTaxonomyLevel1' field choosing the more appropriate of the 12 categories names.
For a better understanding of each category, read the following descriptions:
```
1. Web Interaction and Navigation
Description: Pertains to the user's interaction with the website and its components. It encompasses various actions that facilitate movement across a website and the analysis of its structure.
- Web Navigation & Functionality: How users move around the website and the features it offers.
- Page Source & Web Element Analysis: Examining the underlying HTML, CSS, or scripts to understand a webpage.
- Webpage Tracking & Performance Testing: Methods used to monitor webpages, track user interaction, or gauge its performance.
- Web Request & Endpoint Interaction: Concerns with the retrieval of web resources or data using HTTP methods.
- URL & Web Browser Manipulation: Tweaking URLs or exploiting browser behaviors for malicious ends.

Labeling Guide: If an action from a CTF writeup deals primarily with navigating a website, analyzing its elements, or manipulating the browsing experience, it should be labeled under this category.

2. Authentication, Session, and User Management
Description: Involves the mechanisms that control user access and identity. Actions here relate to manipulating or bypassing these controls.
- Authentication Bypass & Exploitation: Circumventing authentication mechanisms.
- JWT, Web Token, & Cookie Handling: Interacting with or manipulating authentication tokens or cookies.
- Session & OTP Management: Activities surrounding session management or one-time password functionalities.
- Credential & Password Discovery: Methods to unearth or guess user credentials.
- User Registration, Interaction, & Authorization: Concerning user account creation, interaction, and permission levels.

Labeling Guide: Any action related to user access, authorization, authentication mechanisms, or user account management should fall under this category.

3. Data Analysis and Manipulation
Description: Encompasses actions that involve inspecting, altering, or leveraging data for exploitation.
- Data Processing & Visualization: Handling and representation of data.
- User Input & Parameter Analysis: Scrutinizing user-provided data or input parameters.
- Data Leakage, Extraction, & Encoding: Acquiring data illicitly or dealing with data encoding formats.
- List & Event Listener Manipulation: Modifying or exploiting data lists or web event listeners.
- Data & CSV Exploitation: Specific techniques that target data files or CSVs.

Labeling Guide: If an action pertains to examining, altering, or extracting data, especially within a web context, it should be categorized here.

4. Code and Application Analysis
Description: Involves activities centered around reviewing, understanding, or exploiting code and its associated applications.
- Code Inspection, Debugging & Manipulation: Delving into code to understand or alter its behavior.
- Application, System & Server Analysis: Understanding the broader application or system, including servers.
- Script Analysis & Payload Modification (JavaScript, PHP, Bash, etc.): Examining or altering scripts and malicious payloads.
- Dynamic Rendering & Web Development: Dealing with dynamically generated content or development techniques.
- Function, Method & Web Content Analysis: Digging into specific code functions, methods, or web content.

Labeling Guide: If an action involves scrutinizing or manipulating code, scripts, or the broader application, it belongs to this category.

5. Exploitation Techniques and Payload Handling
Description: This area covers the methods used to exploit vulnerabilities and how malicious payloads are managed.
- Injection Attacks (SQL, XSS, etc.): Injecting malicious input to exploit vulnerabilities.
- Vulnerability Identification & Exploitation: Identifying and leveraging security flaws.
- Web Security Techniques & Attack Mechanics: General techniques or mechanisms to compromise web security.
- HTTP Request Smuggling & Redirect Exploitation: Specific web attacks targeting HTTP requests or redirects.
- Exploit, Payload Development & Execution: Crafting, refining, and running malicious payloads.

Labeling Guide: Actions specifically about finding vulnerabilities and exploiting them, or those concerning malicious payloads, fit this category.

6. System and Network Analysis
Description: Deals with understanding or interacting with networks and systems, especially in the context of exploiting them.
- Networking & Communication Protocols (HTTP, DNS, etc.): Understanding or exploiting specific networking protocols.
- Network & Server Interactions and Configurations: Interacting with or understanding network systems and server configurations.
- Proxy & Microservice Communication: Working with or exploiting proxies and microservices.
- IP, DNS & Protocol Handling: Techniques involving IP addresses, DNS systems, or generic protocol handling.

Labeling Guide: If the primary action is related to networking, systems, or their configurations, it should be labeled under this category.

7. File, Resource, and Data Interactions
Description: Encompasses actions around interacting with or exploiting files, databases, and other resources.
- File System Access, Upload, & Analysis: Handling files, whether uploading, accessing, or analyzing them.
- Data & File Analysis & Retrieval: Diving deeper into data or files to retrieve or understand them.
- Database Manipulation, Exploration & Injections: Activities concerning databases, from manipulation to exploitation.
- Resource & Directory Handling and Enumeration: Managing or identifying system resources or directories.

Labeling Guide: Activities focused on files, resources, databases, or similar data repositories should be categorized here.

8. Debugging, Monitoring, and Troubleshooting
Description: This category deals with actions geared towards identifying issues, monitoring behavior, or rectifying problems.
- Troubleshooting & Debugging Techniques: Techniques to identify or resolve issues.
- Error, Response, & Server Message Analysis: Interpreting system or server messages and errors.
- Logging, Monitoring & Behavior Observation: Mechanisms to monitor system behavior or user actions.

Labeling Guide: Any action aimed at problem-solving, error analysis, or monitoring should be placed in this category.

9. Cryptography and Encoding Techniques
Description: Covers actions surrounding cryptographic methods or encoding techniques.
- Base64, JWT, CAPTCHA & Encryption Techniques: Techniques around specific encoding or encryption methods.
- Cryptographic Analysis & Exploits: Examining or exploiting cryptographic implementations.
- Hashing, Decoding & Encoding Techniques: Working with hashed data or encoding and decoding techniques.

Labeling Guide: If the main focus of an action is cryptography, encoding, or related manipulations, it should be classified here.

10. Tools, Scripting, and OS Interactions
Description: Concerns the use, creation, or interaction with tools, scripts, and operating systems.
- Custom Tools, Script Hosting & Shell Execution: Leveraging or creating custom tools, hosting scripts, or executing shell commands.
- Code Creation, Scripting Techniques & Automation: Crafting code, developing scripts, or automating processes.
- Operating System & Terminal Commands: Interacting directly with the OS or using terminal commands.
- Regular Expression & String Manipulation: Using regex or manipulating strings for exploitation or analysis.

Labeling Guide: Actions primarily about tools, scripting, OS interactions, or similar techniques belong to this category.

11. Information Gathering & Security Analysis
Description: Activities geared towards collecting data, conducting recon, or analyzing security postures.
- Vulnerability Research (XSS, SSRF, LFI, etc.): Researching specific vulnerabilities or their exploitation methods.
- Information Gathering, Reconnaissance & Server Discovery: Collecting data about targets or identifying servers and services.
- Web Security Concepts, Techniques, & Analysis: Understanding or leveraging web security methodologies.
- Security Checks, Analysis & Protocol Analysis: Running security checks or analyzing security protocols.

Labeling Guide: If the action involves gathering information, reconnaissance, or analyzing security, it should be categorized under this heading.

12. Documentation and Miscellaneous Techniques
Description: A broad category that encapsulates various other techniques, documentation reviews, specific strategies and more.
- Challenge Understanding, Gameplay Strategy & Solution Development: Understanding CTF challenges and formulating solutions.
- Documentation, Hints, & Clues Review: Reviewing documentation or hints provided in challenges.
- Git Operations, Browser Behavior, & Mobile App Exploits: Activities involving git, browser-specific behaviors, or mobile app vulnerabilities.
- Time-Based Analysis & Specific Techniques: Exploits or techniques based on timing or other specific parameters.

Labeling Guide: This is a catch-all category. If an action doesn't fit neatly into the above categories but involves documentation, specific techniques, or strategies, it should be labeled here.
```

Please consider each substep completely untied from the preceding and following one.
Remember to label using just the category name, not subcategories ones.
Reply just with the output JSON content without adding anything else.

Here's the input JSON:
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
