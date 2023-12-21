import json
import os
import re
import openai


with open("./taxonomy_tier1/taxonomy_tier1.json", "r") as file:
    taxonomy_tier1 = json.load(file)


def get_response(messages: list):
    response = openai.ChatCompletion.create(  # https://platform.openai.com/docs/api-reference/chat/create
        model="gpt-4",  # The name of the OpenAI chatbot model to use
        messages=messages,
        # temperature=1.0,
        stream=False,
    )
    return response.choices[0].message.content


# Get category and description based on directory name
def get_category_description(json_data, directory_name):
    for item in json_data:
        if item["directory"] == directory_name:
            return item["category"], item["description"]
    return None, None


# Function to update the placeholders in the text
def update_placeholders(text, category_text, description_text):
    # Replace placeholders with the provided text
    updated_text = text.replace("{category}", category_text)
    updated_text = updated_text.replace("{description}", description_text)
    return updated_text


def find_substeps_groups_files_without_merged():
    substeps_groups_filepaths = []
    # Define the directory to search in
    search_dir = "./substeps_groups_tier1"
    for dirpath, _, filenames in os.walk(search_dir):
        # Skip files directly under the search_dir
        if dirpath == search_dir:
            continue

        for filename in filenames:
            # Check if the filename starts with "substeps_groups_"
            # and ends with ".json" but not with "_merged.txt"
            if (
                filename.startswith("substeps_groups_tier1")
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
        "./prompts/prompt_merge_substeps_groups_tier1_category_template.txt",
        "r",
        encoding="utf-8",
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

            # Extract the directory name from the current filepath
            current_directory_name = os.path.basename(
                os.path.dirname(substeps_groups_filepath)
            )

            # Fetch the corresponding category and description based on the extracted directory name
            (
                current_category,
                current_description,
            ) = get_category_description(taxonomy_tier1, current_directory_name)

            # Replace placeholders in the prompt with the fetched category and description
            updated_prompt = update_placeholders(
                prompt, current_category, current_description
            )

            # Prepare the message object to send to the OpenAI API
            messages = [
                {
                    "role": "user",
                    "content": updated_prompt + substeps_groups_chunk,
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
