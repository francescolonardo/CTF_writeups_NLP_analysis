import os
import sys
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

import openai

# Initialize the OpenAI API client with your API key
openai.api_key = api_key

'''
If none of the actions in the taxonomy fits the action in the writeup, create a new action and write at the and of your reply something like this:
            'NEW ACTION: <Category>: <Action>'
'''


def json_with_tax(writeup):
    # Define the prompt with the writeup
    prompt = f"```\n{writeup}\n```"

    # Create a list of messages in a chat-like format
    message_log = [
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": 

            """
            I'll give you a CTF writeup in form of a json file. Each step in the writeup has a category, feel free to change the category name, picking one from the following taxonomy. 
            Give to each action in the writeup a lable taken from the chosen taxonomy category:

            For example this:
            "Category": "Writing a script",
            "Actions": {"Develop a Python script (scrambled.py) for flag retrieval."}

            Becomes this:
            "Category": "SCRIPT DEVELOPMENT",
            "Actions": {"DEVELOPE AUTOMATION SCRIPTS" : { "Develop a Python script (scrambled.py) for flag retrieval."}}
            
            "CTF Write-Up Taxonomy": {
            "Initial Reconnaissance": {
                "Description": "The initial phase of gathering information and understanding the challenge.",
                "Actions": {
                "VISIT THE PROVIDED URL": "Access the challenge URL or resource provided.",
                "INSPECT WEBPAGE/RESOURCE": "Analyze the webpage or resource for clues, anomalies, or hidden elements.",
                "IDENTIFY COOKIES": "Discover and examine cookies or session data.",
                "ENUMERATE ENDPOINTS": "Search for hidden or additional endpoints or resources.",
                "SOURCE CODE ANALYSIS": "Examine HTML, JavaScript, or server-side code for vulnerabilities or hints.",
                "FINGERPRINTING": "Identify server software, technologies, or versions in use.",
                "DIRECTORY AND FILE ENUMERATION": "Scan for hidden directories or files on web servers."
                }
            },
            "Challenge Analysis": {
                "Description": "The process of understanding the challenge's mechanics and requirements.",
                "Actions": {
                "READ CHALLENGE DESCRIPTION": "Analyze the challenge description or prompt for hints or context.",
                "IDENTIFY VULNERABILITIES": "Search for potential vulnerabilities in the challenge.",
                "IDENTIFY ATTACK SURFACES": "Determine the potential attack vectors or surfaces in the challenge.",
                "REVERSE ENGINEERING": "Decompile or reverse engineer binaries or code if applicable.",
                "PROTOCOL ANALYSIS": "Analyze network protocols used in challenges (e.g., HTTP, TCP/IP).",
                "CRYPTOGRAPHY ASSESSMENT": "Evaluate cryptographic components and algorithms."
                }
            },
            "Script Development": {
                "Description": "Creating custom scripts or tools to automate tasks or exploit vulnerabilities.",
                "Actions": {
                "DEVELOP AUTOMATION SCRIPTS": "Write code to automate repetitive actions or tasks.",
                "EXPLOIT DEVELOPMENT": "Create exploits or payloads for vulnerabilities.",
                "BRUTE FORCE SCRIPTS": "Write scripts for password or token brute forcing.",
                "DECODING/ENCODING TOOLS": "Create tools for decoding or encoding data.",
                "CUSTOM WORDLISTS": "Generate custom wordlists for dictionary attacks.",
                "STEGANOGRAPHY TOOLS": "Develop tools for analyzing steganographic challenges.",
                "USE EXISTING TOOLS": "Leverage pre-existing CTF tools for specific tasks."
                }
            },
            "Tool Used": {
                "Description": "Utilizing pre-existing CTF tools to streamline and enhance the challenge-solving process.",
                "Actions": {
                "TOOL SELECTION": "Identify and choose appropriate tools for specific CTF tasks.",
                "TOOL CONFIGURATION": "Configure tools to suit the challenge's requirements.",
                "AUTOMATED SCANNING": "Use automated scanning tools to discover vulnerabilities or services.",
                "PASSWORD CRACKING": "Leverage password cracking tools for challenges involving credentials.",
                "FORENSICS TOOLS": "Use digital forensics tools for challenges involving file analysis.",
                "NETWORK ANALYSIS TOOLS": "Employ network analysis tools for challenges related to traffic analysis."
                }
            },
            "Automated Workflow": {
                "Description": "Executing automated processes to interact with the challenge or target.",
                "Actions": {
                "AUTOMATE HTTP REQUESTS": "Use scripts to send HTTP requests to the challenge server or web application.",
                "DATA EXTRACTION": "Automatically extract data or information from responses.",
                "AUTOMATED EXPLOITATION": "Automate the exploitation of vulnerabilities or weaknesses.",
                "NETWORK SCANNING": "Automate network scanning for open ports or services.",
                "PAYLOAD DELIVERY": "Automate the delivery of payloads to target systems.",
                "UTILIZE EXISTING TOOLS": "Incorporate existing CTF automation tools."
                }
            },
            "Data Analysis": {
                "Description": "Analyzing data or information obtained from the challenge.",
                "Actions": {
                "COOKIE ANALYSIS": "Study the behavior and content of cookies.",
                "PACKET CAPTURE ANALYSIS": "Examine network packet captures for clues or data.",
                "DATA MANIPULATION": "Perform operations on extracted data to derive insights or reveal patterns.",
                "DATA VISUALIZATION": "Visualize data to identify trends or anomalies.",
                "FREQUENCY ANALYSIS": "Analyze character or data frequency for patterns."
                }
            },
            "Flag Construction": {
                "Description": "Building the flag or solution incrementally as more information is gathered.",
                "Actions": {
                "PIECE TOGETHER THE FLAG": "Assemble parts of the flag using discovered information.",
                "ITERATIVE FLAG BUILDING": "Build the flag character by character or step by step.",
                "REVERSE ENGINEERING": "Analyze and reconstruct encrypted or obfuscated flag components.",
                "CRYPTOGRAPHIC ANALYSIS": "Analyze cryptographic challenges to uncover key components.",
                "MATHEMATICAL ANALYSIS": "Apply mathematical principles to solve challenges."
                }
            },
            "Flag Retrieval": {
                "Description": "The final step of obtaining and presenting the flag as the solution.",
                "Actions": {
                "RETRIEVE THE FLAG": "Fetch and display the complete flag or solution.",
                "FINALIZE WRITE-UP": "Prepare the CTF write-up for submission or documentation.",
                "VERIFY FLAG VALIDITY": "Ensure the obtained flag is correct and valid.",
                "WRITE CHALLENGE EXPLOITATION NOTES": "Document the steps taken to exploit vulnerabilities.",
                "POST-CHALLENGE CLEANUP": "Clean up any leftover artifacts or resources used during the challenge."
                }
            }
            }
            }

            Reply just with the json, not with any explanation.
            """
        },
        {"role": "system", "content": "Sure! Give me the writeup in json format"},
        {"role": "user", "content": prompt},
    ]

    # Make an API call to generate the explanation
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # The name of the OpenAI chatbot model to use
        messages=message_log,  # The conversation history up to this point
        max_tokens=1000,  # Adjust the token limit as needed
        stop=None,  # The stopping sequence for the generated response, if any (not used here)
        temperature=0.7,  # The "creativity" of the generated response (higher temperature = more creative)
    )

    # Extract the assistant's reply from the response
    assistant_reply = response["choices"][0]["message"]["content"]

    return assistant_reply


# Check if the command-line argument for the file name is provided
if len(sys.argv) < 2:
    print("Usage: python your_script.py <file_name>")
    sys.exit(1)

# Get the file name from the command-line argument
file_name = sys.argv[1]

# Read the writeup from the specified file
try:
    with open(file_name, "r") as file:
        writeup = file.read()
except FileNotFoundError:
    print(f"File '{file_name}' not found.")
    sys.exit(1)

# Get the explanation
explanation = json_with_tax(writeup)

# Print the generated explanation
print(explanation)

file_path = file_name.replace(".json", "_tax.json")

# Open the file in write mode ('w')
with open(file_path, 'w') as file:
    file.write(explanation)

