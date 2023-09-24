import os
import sys
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

import openai

# Initialize the OpenAI API client with your API key
openai.api_key = api_key


def writeup_to_json(writeup):
    # Define the prompt with the writeup
    prompt = f"```\n{writeup}\n```"

    # Create a list of messages in a chat-like format
    message_log = [
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": 

            """
            I'll give you a CTF writeup. I want you to produce a graph of the steps performed by the attacker in form of json. 
            If you find pieces of this writeup that are not natural language (code, different formalisms), replace them with a brief high-level explanation in natural language.
            Take in count that the attacker is a human, so some of the actions could be wrong, you have to insert them anyway and mark them someway as wrong.
            Remove useless informations about the challenge.

            Your reply should be like this json:

            {
            "Attacker Steps": [
                {
                "Step": 1,
                "Category": "Initial Page Analysis",
                "Actions": [
                    "Visit the provided URL: http://web.ctf.b01lers.com:1002/",
                    "Inspect the webpage for unusual elements."
                ]
                },
                {
                "Step": 2,
                "Category": "Cookie Discovery",
                "Actions": [
                    "Identify two strange cookies on the webpage: frequency and transmissions."
                ]
                },
                {
                "Step": 3,
                "Category": "Cookie Analysis",
                "Actions": [
                    "frequency increments with each page refresh.",
                    "transmissions have a fixed part at both ends and a variable part in the middle."
                ]
                },
                {
                "Step": 4,
                "Category": "Variable Part Format",
                "Actions": [
                    "Discover the format of the variable part of the transmissions cookie:",
                    "- Previous character of the flag.",
                    "- Actual character of the flag.",
                    "- Index of the actual character."
                ]
                },
                {
                "Step": 5,
                "Category": "Script Execution",
                "Actions": [
                    "Develop a Python script (scrambled.py) for flag retrieval."
                ]
                },
                {
                "Step": 6,
                "Category": "Script Workflow",
                "Actions": [
                    "Send HTTP requests to the target URL.",
                    "Extract and analyze cookies from the responses."
                ]
                },
                {
                "Step": 7,
                "Category": "Cookie Extraction",
                "Actions": [
                    "Read the transmissions cookie from each response, removing noise."
                ]
                },
                {
                "Step": 8,
                "Category": "Building the Flag",
                "Actions": [
                    "Compose the flag character by character using information from the transmissions cookies.",
                    "Iterate until the flag is complete (last character is '}')."
                ]
                },
                {
                "Step": 9,
                "Category": "Flag Recovery",
                "Actions": [
                    "Retrieve the flag: pctf{Down_With_the_Fallen,Carnivore,Telescope,It_Has_Begun,My_Demons}."
                ]
                }
            ]
            }

            Reply just with the json, not with any explanation.
            You can use numbers like 7.1, 7.2 to refers to nested actions.

            """
        },
        {"role": "system", "content": "Sure! Give me the writeup"},
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
explanation = writeup_to_json(writeup)

# Print the generated explanation
print(explanation)

file_path = file_name.replace(".txt", ".json")

# Open the file in write mode ('w')
with open(file_path, 'w') as file:
    file.write(explanation)

