import json
import os
import re
import openai


def get_response(messages: list):
    response = openai.ChatCompletion.create(  # https://platform.openai.com/docs/api-reference/chat/create
        model="gpt-3.5-turbo",  # The name of the OpenAI chatbot model to use
        messages=messages,
        # temperature=1.0,
        stream=False,
    )
    return response.choices[0].message.content


def find_substeps_files_without_taxl1():
    substeps_filepaths = []
    for dirpath, _, filenames in os.walk("../dataset_writeups"):
        for filename in filenames:
            # Check if filename matches pattern [filename]_substeps_xx.json
            if (
                "_substeps_" in filename
                and filename.endswith(".json")
                and not filename.endswith("_taxl1.json")
            ):
                substeps_filepath = os.path.join(dirpath, filename)
                taxl1_filepath = substeps_filepath.replace(".json", "_taxl1.json")
                if not os.path.exists(taxl1_filepath):
                    substeps_filepaths.append(substeps_filepath)
    return substeps_filepaths


def extract_json(s: str):
    # Search for string patterns that look like JSON objects
    for match in re.finditer(r"{[^}]*}", s):
        substr = s[match.start() :]
        # Try to load the substring as json, extending the substring until it succeeds or it's clear it's not json.
        for end in range(len(substr), 0, -1):
            try:
                potential_json = json.loads(substr[:end])
                # If it succeeds, return the valid json object.
                return potential_json
            except json.JSONDecodeError:
                continue
    return None  # Return None if no valid JSON object is found.


if __name__ == "__main__":
    with open("./api_keys.json", "r", encoding="utf-8") as f:
        api_key = json.load(f)["api_key"]
    openai.api_key = api_key
    with open("./guidelines.json", "r", encoding="utf-8") as f:
        guidelines = json.load(f)
        taxonomy_requirements = guidelines["requirements"]["requirements_taxl1"]

    try:
        substeps_filepaths = find_substeps_files_without_taxl1()
        total_files = len(substeps_filepaths)

        for idx, subteps_filepath in enumerate(substeps_filepaths, start=1):
            with open(subteps_filepath, "r", encoding="utf-8") as substeps_file:
                substeps = substeps_file.read()
            messages = [
                {
                    "role": "user",
                    "content": taxonomy_requirements + substeps,
                }
            ]

            print(f"[{idx}/{total_files}] Processing `{subteps_filepath}`")
            try:
                response = get_response(messages=messages)
            except openai.error.InvalidRequestError as e:
                print(f"ERROR - OpenAI - {e}")

            # Attempt to parse the JSON data
            response_json_data = extract_json(response)

            # Check if JSON is well-formed and complete
            if response_json_data is not None:
                # Check the top-level fields in the response_json_data
                if all(
                    key in response_json_data
                    for key in ["StepNumber", "StepString", "Substeps"]
                ):
                    # Iterate over each substep in the response_json_data
                    for substep in response_json_data.get("Substeps", []):
                        # Check if all the required fields exist in a substep
                        if all(
                            key in substep
                            for key in [
                                "SubstepNumber",
                                "SubstepString",
                                "SubstepTaxonomyLevel1",
                            ]
                        ):
                            # The structure seems well-formed and complete.
                            print("INFO - JSON appears to be well-formed and complete.")
                            taxl1_filepath = subteps_filepath.replace(
                                ".json", "_taxl1.json"
                            )
                            with open(
                                taxl1_filepath, "w", encoding="utf-8"
                            ) as taxl1_file:
                                json.dump(response_json_data, taxl1_file, indent=4)
                            print(f"Saved `{taxl1_filepath}`")
                        else:
                            print(
                                f"ERROR - Substep {substep.get('SubstepNumber', 'Unknown')} is missing some fields."
                            )
                else:
                    print("ERROR - JSON is missing expected keys or values.")
            else:
                print("ERROR - JSON may be truncated or invalid.")

    except KeyboardInterrupt:
        print("Stop.")
