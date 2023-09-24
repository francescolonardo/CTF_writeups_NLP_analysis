import os
from dotenv import load_dotenv
import sys

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

import openai

# Initialize the OpenAI API client with your API key
openai.api_key = api_key


def update_taxonomy(writeup, partial_taxonomy, taxonomy_category, taxonomy_category_description):
    # Define the prompt with the writeup
    prompt_writeup = f"```\n{writeup}\n```"
    prompt_taxonomy = f"```\n{partial_taxonomy}\n```"

    # Create a list of messages in a chat-like format
    message_log = [
        {
            "role": "user",
            "content":
            """
            I'll provide you with a CTF writeup in a text file.

            I've created a taxonomy with the following categories: 
            Initial Reconnaissance: The initial phase of gathering information and understanding the challenge.
            Challenge Analysis: The process of understanding the challenge's mechanics and requirements.
            Script Development: Creating custom scripts or tools to automate tasks or exploit vulnerabilities.
            Tool Used: Utilizing pre-existing CTF tools to streamline and enhance the challenge-solving process.
            Automated Workflow:  Executing automated processes to interact with the challenge or target.
            Data Analysis: Analyzing data or information obtained from the challenge.
            Flag Construction: Building the flag or solution incrementally as more information is gathered.
            Flag Retrieval: The final step of obtaining and presenting the flag as the solution.

            For this task, you should only focus on the """ + taxonomy_category + """ category.

            Your task is to review and potentially enhance the actions within the """ + taxonomy_category + """ category based on the provided writeup. You can add, modify, or delete actions, but only if it's absolutely necessary. If you believe no changes are needed, you can simply return the same taxonomy piece.

            Please keep in mind that the taxonomy should remain as general as possible, and you should not add actions that are too specific or related to the provided writeup.
            Moreover the taxonomy should be as concise as possible so add a new action only if it's absolutely necessary.

            Here's the taxonomy piece:
            """ + prompt_taxonomy + """

            And here's the writeup:
            """ + prompt_writeup + """

            Before adding an action consider that the categories are mutual exclusive, so if an action could be part of another category do not add it.

            Your response will include the enanched taxonomy without adding others details.
            """
        }
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

    try:
        with open("./logs/log.txt", 'a', encoding='utf-8') as t:
            t.write("\n \n" + str(assistant_reply))
    except Exception as e:
        print(f"Error saving the log file: {e}")
        sys.exit(1)  # Exit the script with a non-zero status code if there's an error

    return assistant_reply
