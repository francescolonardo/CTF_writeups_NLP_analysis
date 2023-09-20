import os
import sys
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

import openai

# Initialize the OpenAI API client with your API key
openai.api_key = api_key


def writeup_to_json(message_log):
    try:
        # Make an API call to generate the explanation
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=message_log,
            max_tokens=1000,
            stop=None,
            temperature=0.7,
        )

        # Extract the assistant's reply from the response
        assistant_reply = response["choices"][0]["message"]["content"]

        return assistant_reply
    except Exception as e:
        print(f"Error processing writeup: {e}")
        return None


def save_json(filename, json_data):
    # Create a JSON file with the same name as the text file
    json_file_path = filename.replace(".txt", ".json")

    # Open the JSON file in write mode ('w')
    with open(json_file_path, "w") as json_file:
        json_file.write(json_data)


def process_writeup_file(file_path):
    try:
        # Read the writeup from the file
        with open(file_path, "r") as file:
            writeup = file.read()
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return

    # Define the message_log with the prompt
    message_log = [
        {
            "role": "user",
            "content": 
            """
            Generate a comprehensive attack model from a CTF writeup, elucidating the attacker's thought process leading to their solution.
            Strive for maximal abstraction to create a generic attack model independent of the specific writeup.
            Use the following JSON format as a guide:
            {
            "AttackModel": {
                    "NameOfTheChallenge": "Specify the name of the challenge.",
                    "AttackerCapabilities": [
                        "List the capabilities or skills possessed by the attacker."
                    ],
                    "Target": {
                        "Type": "Specify the type of target (e.g., Web Application, Network Service, IoT Device).",
                        "Vulnerabilities": [
                            //List the vulnerabilities present in the target system.
                        ],
                        "SecurityMeasures": [
                            //List the security measures or configurations of the target.
                        ]
                    },
                    "Steps": [
                        {
                            "StepNumber": 1,
                            "Description": "Provide a detailed description of this step within the process. You can use a hypothetical scenario to illustrate.",
                            "ToolsUsed": "Specify any tools used here; otherwise, set to null.",
                            "StepDetails": {
                                "Hypothesis": "Explain why the attacker is performing this action. What is their goal in this step?",
                                "Action": "Describe the specific action taken during this step. What is the attacker doing?",
                                "Result": "Describe the outcome or result of the action. What did the attacker achieve?",
                                "Success": "Indicate whether the Hypothesis matches the Result as 'Success' or 'Failed'.",
                                "FailingReason": "If the action fails, explain the reason for the failure. If the action succeeds, set to null."
                            }
                        }
                        // Add more steps as needed
                    ]
                }
            }
            Here's the writeup:
            """ + writeup
        }
    ]

    # Get the explanation, and skip if there's an error

    explanation = writeup_to_json(message_log)
    if explanation is None:
        return

    return explanation


def main(folder_path):
    # Check if the folder exists
    if not os.path.isdir(folder_path):
        print(f"Folder '{folder_path}' not found.")
        sys.exit(1)

    # Initialize a set to store processed filenames without the extension
    processed_files = set()

    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        # Check if the file has a ".txt" extension
        if filename.endswith(".txt"):
            # Construct the full path to the file
            file_path = os.path.join(folder_path, filename)

            # Check if there's a corresponding JSON file for this document
            json_file_path = file_path.replace(".txt", ".json")
            if os.path.exists(json_file_path):
                # Skip processing if a JSON file already exists
                print(
                    f"Skipping processing for file '{filename}' as it already has a JSON counterpart."
                )
                continue

            # Process the writeup file
            explanation = process_writeup_file(file_path)
            if explanation is None:
                continue

            # Print the generated explanation
            print(f"File: {filename}")

            # Save the JSON data to a file
            save_json(file_path, explanation)

            # Add the filename (without extension) to the set of processed files
            processed_files.add(filename.rsplit(".", 1)[0])

    # Optionally, you can print the list of processed filenames
    print(f"Processed Files: {processed_files}")


if __name__ == "__main__":
    # Check if the command-line argument for the folder name is provided
    if len(sys.argv) < 2:
        print("Usage: python your_script.py <folder_path>")
        sys.exit(1)

    # Get the folder path from the command-line argument
    folder_path = sys.argv[1]

    # Run the main function
    main(folder_path)
