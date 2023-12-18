import json
import os
import re
import openai


with open("./taxonomy/taxonomy_tier1.json", "r") as file:
    taxonomy_tier1 = json.load(file)


def get_response(messages: list):
    response = openai.ChatCompletion.create(  # https://platform.openai.com/docs/api-reference/chat/create
        model="gpt-3.5-turbo",  # The name of the OpenAI chatbot model to use
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


def find_list_substeps_files_without_grouped():
    list_substeps_filepaths = []
    # Define the directory to search in
    search_dir = "./list_substeps_tier1"

    # This regex will match filenames with the pattern "list_substeps_tier1_{tier1_category_name}_*.json"
    pattern = re.compile(r"^list_substeps_tier1_(.*?)_.*\.json$")

    for dirpath, dirnames, filenames in os.walk(search_dir):
        # Skip the root directory
        if dirpath == search_dir:
            continue

        for filename in filenames:
            if pattern.match(filename) and not filename.endswith("_grouped.json"):
                list_substeps_filepath = os.path.join(dirpath, filename)
                grouped_substeps_filepath = list_substeps_filepath.replace(
                    ".json", "_grouped.json"
                )
                if not os.path.exists(grouped_substeps_filepath):
                    list_substeps_filepaths.append(list_substeps_filepath)
    return list_substeps_filepaths


def extract_json(s: str):
    # Search for string patterns that start with an opening brace
    for match in re.finditer(r"{", s):
        substr = s[match.start() :]
        braces_count = 0
        end_pos = -1
        for idx, char in enumerate(substr):
            if char == "{":
                braces_count += 1
            elif char == "}":
                braces_count -= 1
            if braces_count == 0:
                end_pos = idx
                break
        if end_pos != -1:
            potential_str = substr[: end_pos + 1]
            try:
                potential_json = json.loads(potential_str)
                return potential_json
            except json.JSONDecodeError:
                continue
    return None


if __name__ == "__main__":
    with open("./api_keys.json", "r", encoding="utf-8") as f:
        api_key = json.load(f)["api_key"]
    openai.api_key = api_key
    with open(
        "./prompts/prompt_group_list_substeps_tier1_category_template.txt",
        "r",
        encoding="utf-8",
    ) as f:
        prompt = f.read()

    try:
        list_substeps_filepaths = find_list_substeps_files_without_grouped()
        total_files = len(list_substeps_filepaths)

        for idx, list_substeps_filepath in enumerate(list_substeps_filepaths, start=1):
            with open(list_substeps_filepath, "r", encoding="utf-8") as f:
                list_substeps_chunk = f.read()

            # Extract the directory name from the current filepath
            current_directory_name = os.path.basename(
                os.path.dirname(list_substeps_filepath)
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
                    "content": updated_prompt + list_substeps_chunk,
                }
            ]

            print(f"[{idx}/{total_files}] Processing `{list_substeps_filepath}`")
            try:
                response = get_response(messages=messages)
            except openai.error.InvalidRequestError as e:
                print(f"ERROR - OpenAI - {e}")

            # Attempt to parse the JSON data
            response_json_data = extract_json(response)

            # Check if JSON is well-formed and complete
            if response_json_data is not None:
                print("INFO - JSON appears to be well-formed and complete.")

                # Check the number of keys in the JSON
                if len(response_json_data.keys()) < 3:
                    print("WARNING - JSON has less than 3 keys. Skipping this file.")
                    continue
                if len(response_json_data.keys()) > 9:
                    print("WARNING - JSON has more than 9 keys. Skipping this file.")
                    continue

                # Check the number of lines in the JSON
                formatted_json = json.dumps(response_json_data, indent=4)
                if (
                    formatted_json.count("\n") > 64
                ):  # Subtract 1 because a single line has 0 '\n'
                    print("WARNING - JSON has more than 65 lines. Skipping this file.")
                    continue

                grouped_substeps_filepath = list_substeps_filepath.replace(
                    ".json", "_grouped.json"
                )
                with open(grouped_substeps_filepath, "w", encoding="utf-8") as f:
                    f.write(formatted_json)

                print(f"Saved `{grouped_substeps_filepath}`")
            else:
                print("ERROR - JSON may be truncated or invalid.")

    except KeyboardInterrupt:
        print("Stop.")
