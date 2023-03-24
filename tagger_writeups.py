import json
import os
import re
import time

import openai


MODEL_ID = "gpt-3.5-turbo"
# more contextually relevant and less creative responses (from 0.0 to 2.0)
RANDOMNESS_LEVEL = 0.5
WRITEUPS_DIRNAME = "./dataset_writeups/"
TXT_SUFFIXES = ["_original.txt", "_cleaned.txt", "_tagged.txt"]
LABELS_TO_REMOVE = ["# overview", "# analysis",
                    "# attack execution", "# attack_execution"]
REQUESTED_LABELS = ["#overview", "#analysis", "#attack_execution"]


def get_response(messages: list):
    response = openai.ChatCompletion.create(  # https://platform.openai.com/docs/api-reference/chat/create
        model=MODEL_ID,
        messages=messages,
        temperature=RANDOMNESS_LEVEL,
        stream=False,
    )
    return response.choices[0].message


def search_strings_in_text(text, strings_list):
    return any(s in text for s in strings_list)


def read_clean_file(in_filepath):
    with open(in_filepath, "r") as input_f:
        file_content = input_f.read()
        # remove the specified strings
        for string in LABELS_TO_REMOVE:
            pattern = re.compile(re.escape(string), re.IGNORECASE)
            file_content = pattern.sub("", file_content)
        # remove empty lines # TODO: maybe unneeded
        file_content = "\n".join(
            [line for line in file_content.split("\n") if line.strip()]
        )
        # replace newline characters with spaces
        # file_content = file_content.replace("\n", " ")  # TODO: maybe unneeded
        return file_content


def write_file(out_filepath, file_content):
    with open(out_filepath, "w") as output_file:
        output_file.write(file_content)


def delete_file(filepath):
    if os.path.isfile(filepath):
        try:
            os.remove(filepath)
            print(f"Writeup file: {filepath} successfully deleted.")
        except Exception as e:
            print(f"Error deleting writeup file {filepath}: {e}")


if __name__ == "__main__":
    with open("./api_keys.json") as f:
        api_key = json.load(f)["api_key"]
    openai.api_key = api_key
    with open("./guidelines.json") as f:
        requirements = json.load(f)
        basic_requirements = requirements["basic_requirements"]
        tagger_requirements = requirements["tagger_requirements"]
    guidelines = basic_requirements + tagger_requirements
    print("Sending the context...")
    get_response(messages=guidelines)

    print("Tagging new writeups...")
    # loop through all directories and subdirectories
    for dirpath, dirnames, filenames in os.walk(WRITEUPS_DIRNAME):
        # loop through all files in the directory
        for filename in filenames:
            # check if the file is a text file
            if filename.endswith(".txt"):
                if not filename.endswith(TXT_SUFFIXES[0]) and not filename.endswith(TXT_SUFFIXES[1]) and not filename.endswith(TXT_SUFFIXES[2]):
                    # original file
                    in_filepath = os.path.join(
                        WRITEUPS_DIRNAME, filename)  # TODO: fix this
                    print(f"Writeup file (original): {in_filepath}")
                    # cleaned file
                    file_content = read_clean_file(in_filepath)
                    out_filepath = os.path.splitext(
                        in_filepath)[0] + TXT_SUFFIXES[1].split(".")[0] + os.path.splitext(in_filepath)[1]
                    write_file(out_filepath, file_content)
                    #print(f"Writeup file (cleaned): {out_filepath}")
                    guidelines.append(
                        {"role": "user", "content": file_content})
                    max_retries = 3
                    retry_count = 0
                    while retry_count < max_retries:
                        try:
                            # tagged file
                            assistant_output = get_response(
                                messages=guidelines)
                            # search if the response is correctly tagged
                            if not search_strings_in_text(assistant_output["content"], REQUESTED_LABELS):
                                break
                            guidelines.append(assistant_output)
                            out_filepath = os.path.splitext(
                                in_filepath)[0] + TXT_SUFFIXES[2].split(".")[0] + os.path.splitext(in_filepath)[1]
                            write_file(
                                out_filepath, assistant_output["content"])
                            print(f"Writeup file (tagged): {out_filepath}")
                            # rename original file
                            new_filename = filename.replace(
                                ".txt", TXT_SUFFIXES[0])
                            os.rename(os.path.join(WRITEUPS_DIRNAME, filename),
                                      os.path.join(WRITEUPS_DIRNAME, new_filename))
                            break  # exit the loop if the function call succeeds
                        except openai.error.InvalidRequestError as e:
                            print(f"OpenAI API request is invalid: {e}")
                            retry_count += 1
                            if retry_count == max_retries:
                                # delete files
                                '''
                                delete_file(filepath=out_filepath)
                                delete_file(filepath=os.path.join(
                                    WRITEUPS_DIRNAME, filename))
                                '''
                                break
                        except openai.error.RateLimitError as e:
                            print(
                                f"OpenAI API request exceeds rate limit: {e}")
                            time.sleep(60)  # sleep for 60 seconds
