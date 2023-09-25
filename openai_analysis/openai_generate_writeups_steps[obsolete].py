import json
import os
import openai


def get_response(messages: list):
    response = openai.ChatCompletion.create(  # https://platform.openai.com/docs/api-reference/chat/create
        model="gpt-3.5-turbo",  # The name of the OpenAI chatbot model to use
        messages=messages,
        temperature=1.0,
        stream=False,
    )
    return response.choices[0].message.content


def find_summary_files_without_steps():
    summary_filepaths = []
    for dirpath, dirnames, filenames in os.walk("../dataset_writeups"):
        for filename in filenames:
            if filename.endswith("_summary.txt"):
                summary_filepath = os.path.join(dirpath, filename)
                steps_filepath = summary_filepath.replace("_summary.txt", "_steps.json")
                if not os.path.exists(steps_filepath):
                    summary_filepaths.append(summary_filepath)
    return summary_filepaths


if __name__ == "__main__":
    with open("./api_keys.json", "r", encoding="utf-8") as f:
        api_key = json.load(f)["api_key"]
    openai.api_key = api_key
    with open("./guidelines.json", "r", encoding="utf-8") as f:
        guidelines = json.load(f)
        requirements_steps = guidelines["requirements"]["requirements_steps"]

    try:
        summary_filepaths = find_summary_files_without_steps()
        total_files = len(summary_filepaths)

        for idx, summary_filepath in enumerate(summary_filepaths, start=1):
            with open(summary_filepath, "r", encoding="utf-8") as writeup_file:
                writeup = writeup_file.read()
            messages = [
                {
                    "role": "user",
                    "content": requirements_steps + writeup,
                }
            ]

            print(f"[{idx}/{total_files}] Processing `{summary_filepath}`")
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
                # Check if the structure contains the expected keys and values
                if (
                    "AttackModel" in response_json_data
                    and "Steps" in response_json_data["AttackModel"]
                ):
                    print("INFO - JSON appears to be well-formed and complete.")
                    steps_filepath = summary_filepath.replace(
                        "_summary.txt", "_steps.json"
                    )
                    with open(steps_filepath, "w", encoding="utf-8") as steps_file:
                        json.dump(response_json_data, steps_file, indent=4)
                    print(f"Saved `{steps_filepath}`")
                else:
                    print("ERROR - JSON is missing expected keys or values.")

    except KeyboardInterrupt:
        print("Stop.")
