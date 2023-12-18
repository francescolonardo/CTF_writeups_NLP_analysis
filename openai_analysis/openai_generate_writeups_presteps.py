import json
import os
import openai


def get_response(messages: list):
    response = openai.ChatCompletion.create(  # https://platform.openai.com/docs/api-reference/chat/create
        model="gpt-4",  # The name of the OpenAI chatbot model to use
        messages=messages,
        # temperature=1.0,
        stream=False,
    )
    return response.choices[0].message.content


def find_original_files_without_presteps():
    original_filepaths = []
    for dirpath, _, filenames in os.walk("../dataset_writeups"):
        for filename in filenames:
            if filename.endswith("_original.md"):
                original_filepath = os.path.join(dirpath, filename)
                presteps_filepath = original_filepath.replace(
                    "_original.md", "_presteps.json"
                )
                if not os.path.exists(presteps_filepath):
                    original_filepaths.append(original_filepath)
    return original_filepaths


if __name__ == "__main__":
    with open("./api_keys.json", "r", encoding="utf-8") as f:
        api_key = json.load(f)["api_key"]
    openai.api_key = api_key
    with open("./guidelines.json", "r", encoding="utf-8") as f:
        guidelines = json.load(f)
        requirements_presteps = guidelines["requirements"]["requirements_presteps"]

    try:
        original_filepaths = find_original_files_without_presteps()
        total_files = len(original_filepaths)

        for idx, original_filepath in enumerate(original_filepaths, start=1):
            with open(original_filepath, "r", encoding="utf-8") as writeup_file:
                writeup = writeup_file.read()
            messages = [
                {
                    "role": "user",
                    "content": requirements_presteps + writeup,
                }
            ]

            print(f"[{idx}/{total_files}] Processing `{original_filepath}`")
            try:
                response = get_response(messages=messages)
            except openai.error.InvalidRequestError as e:
                print(f"ERROR - OpenAI - {e}")

            # Attempt to parse the JSON data
            try:
                response_json_data = json.loads(response)
            except json.JSONDecodeError as e:
                print(f"ERROR - JSON may be truncated or invalid - {e}")
                response_json_data = None
            # Check if JSON is well-formed and complete
            if response_json_data is not None:
                print("INFO - JSON appears to be well-formed and complete.")
                presteps_filepath = original_filepath.replace(
                    "_original.md", "_presteps.json"
                )
                with open(presteps_filepath, "w", encoding="utf-8") as presteps_file:
                    json.dump(response_json_data, presteps_file, indent=4)
                print(f"Saved `{presteps_filepath}`")

    except KeyboardInterrupt:
        print("Stop.")
