import json
import os
import re
import time
import argparse
import unicodedata

import openai
import chardet

from settings import OLD_LABELS, NEW_LABELS
from settings import MODEL_ID, MODEL_RANDOMNESS_TAGGER
from settings import DATASET_DIRPATH, HUMANS_TAGGED_DIRNAME, DATASET_TXT_SUFFIXES


def get_response(messages: list):
    response = openai.ChatCompletion.create(  # https://platform.openai.com/docs/api-reference/chat/create
        model=MODEL_ID,
        messages=messages,
        temperature=MODEL_RANDOMNESS_TAGGER,
        stream=False,
    )
    return response.choices[0].message


def search_strings_in_text(text, strings_list):
    return any(s in text for s in strings_list)


def normalize_file(in_filepath):
    # open the file in binary mode and read its content
    with open(in_filepath, "rb") as input_f:
        content = input_f.read()
    # detect the file's encoding
    encoding = chardet.detect(content)["encoding"]
    # decode the contents of the file using the detected encoding
    decoded_content = content.decode(encoding)
    # normalize the text by replacing non-ASCII characters with their closest ASCII equivalent
    normalized_content = unicodedata.normalize(
        'NFKD', decoded_content).encode("ascii", "ignore").decode("utf-8")
    # write the normalized contents back to the file
    with open(in_filepath, "wb") as output_f:
        output_f.write(normalized_content.encode("utf-8"))


def read_clean_file(in_filepath):
    with open(in_filepath, "r", encoding="utf-8") as input_f:
        file_content = input_f.read()
        # remove the specified strings
        for string in OLD_LABELS:
            pattern = re.compile(re.escape(string), re.IGNORECASE)
            file_content = pattern.sub("", file_content)
        # remove empty lines # TODO: maybe unneeded
        '''
        file_content = "\n".join(
            [line for line in file_content.split("\n") if line.strip()]
        )
        '''
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


class NotCorrectlyTagged(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


if __name__ == "__main__":
    # create an argument for the string parameter 
    parser = argparse.ArgumentParser()
    parser.add_argument('-dir', dest='directory', default=DATASET_DIRPATH,
                        help='the directory to scan for tagging')
    # create an argument for the integer parameter
    parser.add_argument("-n", dest="number", type=int, default=10000,
                        help="the number of writeups to tag")
    args = parser.parse_args()
    # get the directory to scan
    starting_directory = args.directory
    # get the number of writeups to scan
    num_writeups = args.number

    with open("./api_keys.json", "r", encoding="utf-8") as f:
        api_key = json.load(f)["api_key"]
    openai.api_key = api_key
    with open("./guidelines.json", "r", encoding="utf-8") as f:
        requirements = json.load(f)
        basic_requirements = requirements["basic_requirements"]
        tagger_requirements = requirements["tagger_requirements"]
    guidelines = basic_requirements + tagger_requirements
    print("Sending the context...")
    get_response(messages=guidelines)

    try:
        print("Tagging new writeups...")
        # loop through all directories and subdirectories
        for dirpath, dirnames, filenames in os.walk(starting_directory):
            # loop through all files in the directory
            # skip the human tagged writeups
            if HUMANS_TAGGED_DIRNAME in dirnames:
                dirnames.remove(HUMANS_TAGGED_DIRNAME)
            for filename in filenames:
                # check if the file is a text file
                if filename.endswith(".txt"):
                    if not filename.endswith(DATASET_TXT_SUFFIXES[2]):
                        # check that the file is not yet tagged
                        prefix_filename = filename.split(".")[0]
                        if not os.path.exists(os.path.join(dirpath, prefix_filename+DATASET_TXT_SUFFIXES[2])):
                            num_writeups = num_writeups - 1
                            # original file
                            in_filepath = os.path.join(
                                dirpath, filename)
                            print(f"Writeup file (original): {in_filepath}")
                            # normalized file
                            file_content = normalize_file(in_filepath)
                            # cleaned file
                            file_content = read_clean_file(in_filepath)
                            # TODO: remove this (?)
                            '''
                            out_filepath = os.path.splitext(
                                in_filepath)[0] + TXT_SUFFIXES[1].split(".")[0] + os.path.splitext(in_filepath)[1]
                            write_file(out_filepath, file_content)
                            #print(f"Writeup file (cleaned): {out_filepath}")
                            '''
                            guidelines.append(
                                {"role": "user", "content": file_content})  # add the writeup
                            max_retries = 10
                            retry_count = 0
                            while retry_count < max_retries:
                                try:
                                    # tagged file
                                    assistant_output = get_response(
                                        messages=guidelines)
                                    # check if the response is correctly tagged
                                    if not search_strings_in_text(assistant_output["content"], NEW_LABELS):
                                        raise NotCorrectlyTagged(
                                            "Writeup not correctly tagged. Retrying...")
                                    # guidelines.append(assistant_output)
                                    out_filepath = os.path.splitext(
                                        in_filepath)[0] + DATASET_TXT_SUFFIXES[2].split(".")[0] + os.path.splitext(in_filepath)[1]
                                    write_file(
                                        out_filepath, assistant_output["content"])
                                    print(
                                        f"Writeup file (tagged): {out_filepath}")
                                    # TODO: remove this (?)
                                    '''
                                    # rename original file
                                    new_filename = filename.replace(
                                        ".txt", TXT_SUFFIXES[0])
                                    os.rename(os.path.join(dirpath, filename),
                                            os.path.join(dirpath, new_filename))
                                    '''
                                    break  # exit the loop if the function call succeeds
                                except NotCorrectlyTagged as e:
                                    print(e.message)
                                    retry_count += 1
                                except openai.error.InvalidRequestError as e:
                                    if str(e).startswith("This model's maximum context length"):
                                        print(
                                            "OpenAI API request exceeds maximum context length. Retrying...")
                                    else:
                                        # TODO: remove this
                                        print(f"{e}\n FIX THIS ERROR!")
                                    retry_count += 1
                                except openai.error.RateLimitError as e:
                                    print(
                                        "OpenAI API request exceeds rate limit. Slowing down...")
                                    time.sleep(60)  # sleep for 60 seconds
                                finally:
                                    if retry_count == max_retries:
                                        # delete files
                                        '''
                                        delete_file(filepath=out_filepath)
                                        delete_file(filepath=os.path.join(
                                            dirpath, filename))
                                        '''
                                        break
                            guidelines.pop()  # remove the writeup
                            if num_writeups == 0:
                                break
                if num_writeups == 0:
                    break
        print("Done.")
    except KeyboardInterrupt:
        print("Stop.")
