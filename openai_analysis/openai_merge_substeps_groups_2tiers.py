import json
import os
import re
import openai


def get_response(messages: list):
    response = openai.ChatCompletion.create(  # https://platform.openai.com/docs/api-reference/chat/create
        model="gpt-4",  # The name of the OpenAI chatbot model to use
        messages=messages,
        # temperature=1.0,
        stream=False,
    )
    return response.choices[0].message.content


def find_substeps_groups_files_without_merged():
    substeps_groups_filepaths = []
    # Define the directory to search in
    search_dir = "./substeps_groups_2tiers"
    for dirpath, _, filenames in os.walk(search_dir):
        for filename in filenames:
            # Check if the filename starts with "substeps_groups_"
            # and ends with ".json" but not with "_merged.json"
            if (
                filename.startswith("substeps_groups_")
                and filename.endswith(".json")
                and not filename.endswith("_merged.txt")
            ):
                # Get the complete path of the current file
                substeps_groups_filepath = os.path.join(dirpath, filename)
                # Formulate the path of the corresponding _merged.json file
                merged_substeps_filepath = substeps_groups_filepath.replace(
                    ".json", "_merged.txt"
                )
                # Check if the _merged.json file exists
                if not os.path.exists(merged_substeps_filepath):
                    substeps_groups_filepaths.append(substeps_groups_filepath)
    return substeps_groups_filepaths


if __name__ == "__main__":
    with open("./api_keys.json", "r", encoding="utf-8") as f:
        api_key = json.load(f)["api_key"]
    openai.api_key = api_key
    with open(
        "./prompts/prompt_merge_substeps_groups_2tiers.txt", "r", encoding="utf-8"
    ) as f:
        prompt = f.read()

    try:
        substeps_groups_filepaths = find_substeps_groups_files_without_merged()
        total_files = len(substeps_groups_filepaths)

        for idx, substeps_groups_filepath in enumerate(
            substeps_groups_filepaths, start=1
        ):
            with open(substeps_groups_filepath, "r", encoding="utf-8") as f:
                substeps_groups_chunk = f.read()
            messages = [
                {
                    "role": "user",
                    "content": prompt + substeps_groups_chunk,
                }
            ]

            print(f"[{idx}/{total_files}] Processing `{substeps_groups_filepath}`")
            try:
                response = get_response(messages=messages)
            except openai.error.InvalidRequestError as e:
                print(f"ERROR - OpenAI - {e}")

            merged_groups_filepath = substeps_groups_filepath.replace(
                ".json", "_merged.txt"
            )
            with open(merged_groups_filepath, "w", encoding="utf-8") as f:
                f.write(response)

            print(f"Saved `{merged_groups_filepath}`")

    except KeyboardInterrupt:
        print("Stop.")
