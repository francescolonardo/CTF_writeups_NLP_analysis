import json
import os
import ast
from collections import OrderedDict
import openai

dataset_directory = "../dataset_writeups"

with open("./taxonomy/taxonomy_tier2.json", "r") as file:
    json_tier2_taxonomy = json.load(file)


def build_tier2_possible_values(taxonomy):
    mapping = {}
    for entry in taxonomy:
        tier1 = entry["tier1_category"]
        tier2_values = [subitem["tier2_category"] for subitem in entry["tier2"]]
        mapping[tier1] = tier2_values
    return mapping


tier2_possible_values = build_tier2_possible_values(json_tier2_taxonomy)


def get_response(messages: list):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        stream=False,
    )
    return response.choices[0].message.content


def extract_tier2_info(tier1_taxonomy_main, tier1_taxonomy_alternative, json_data):
    results = []
    for taxonomy in [tier1_taxonomy_main, tier1_taxonomy_alternative]:
        current_result = []
        for item in json_data:
            if item["tier1_category"] == taxonomy:
                current_result.append(item["tier1_category"])
                for subitem in item["tier2"]:
                    line = "    {}: {}".format(
                        subitem["tier2_category"],
                        subitem["tier2_description"],
                    )
                    current_result.append(line)
                break
        if current_result:
            results.append("\n".join(current_result))
    return "\n\n".join(results)


def update_placeholder(prompt, new_info):
    updated_prompt = prompt.replace("{tier2_taxonomy}", new_info)
    return updated_prompt


def find_substeps_files_without_tier2(directory):
    tier2_missing_filepaths = []
    for dirpath, _, filenames in os.walk(directory):
        if "_substeps_tier1" in dirpath:
            for filename in filenames:
                if "_substep_" in filename and filename.endswith("_tier1.json"):
                    tier2_filename = filename.replace("_tier1.json", "_tier2.json")
                    tier2_filepath = os.path.join(dirpath, tier2_filename)
                    if not os.path.exists(tier2_filepath):
                        tier2_missing_filepaths.append(os.path.join(dirpath, filename))
    return tier2_missing_filepaths


def extract_json(response):
    try:
        return json.loads(response)
    except json.JSONDecodeError:
        try:
            return ast.literal_eval(response)
        except (ValueError, SyntaxError):
            print(
                "Error: The response string is neither valid JSON nor a Python dict-like string"
            )
            return None


if __name__ == "__main__":
    with open("./api_keys.json", "r", encoding="utf-8") as f:
        api_key = json.load(f)["api_key"]
    openai.api_key = api_key
    with open(
        "./prompts/prompt_tier2taxonomy_labelling_minimal_template.txt",
        "r",
        encoding="utf-8",
    ) as f:
        prompt = f.read()

    try:
        substeps_filepaths = find_substeps_files_without_tier2(dataset_directory)
        total_files = len(substeps_filepaths)
        for idx, subtep_filepath in enumerate(substeps_filepaths, start=1):
            with open(subtep_filepath, "r", encoding="utf-8") as substep_file:
                json_substep = json.load(substep_file)

            tier1_taxonomy_main = json_substep.get("Tier1TaxonomyMain", None)
            tier1_taxonomy_alternative = json_substep.get(
                "Tier1TaxonomyAlternative", None
            )

            current_tier2_info = extract_tier2_info(
                tier1_taxonomy_main, tier1_taxonomy_alternative, json_tier2_taxonomy
            )

            updated_prompt = update_placeholder(prompt, current_tier2_info)
            messages = [{"role": "user", "content": updated_prompt + str(json_substep)}]

            print(f"[{idx}/{total_files}] Processing `{subtep_filepath}`")
            try:
                response = get_response(messages=messages)
                response_json_data = extract_json(response)

                if response_json_data is not None:
                    required_fields = [
                        "SubstepNumber",
                        "SubstepString",
                        "Tier1TaxonomyMain",
                        "Tier1TaxonomyAlternative",
                        "Tier2TaxonomyMain",
                        "Tier2TaxonomyAlternative",
                    ]

                    if all(field in response_json_data for field in required_fields):
                        if (
                            response_json_data["Tier1TaxonomyAlternative"] == "N/A"
                            and response_json_data["Tier2TaxonomyAlternative"] != "N/A"
                        ):
                            response_json_data["Tier2TaxonomyAlternative"] = "N/A"
                            print("INFO - Forced 'Tier2TaxonomyAlternative' to 'N/A'")

                        if (
                            response_json_data["Tier1TaxonomyAlternative"] != "N/A"
                            and response_json_data["Tier2TaxonomyAlternative"] == "N/A"
                        ):
                            print(
                                "ERROR - 'Tier2TaxonomyAlternative' can't be 'N/A' if 'Tier1TaxonomyAlternative' is not 'N/A'."
                            )
                            continue

                        tier1_main_value = response_json_data.get("Tier1TaxonomyMain")
                        tier2_main_value = response_json_data.get("Tier2TaxonomyMain")
                        tier1_alternative_value = response_json_data.get(
                            "Tier1TaxonomyAlternative"
                        )
                        tier2_alternative_value = response_json_data.get(
                            "Tier2TaxonomyAlternative"
                        )

                        if tier2_main_value not in tier2_possible_values.get(
                            tier1_main_value, []
                        ):
                            print(
                                f"ERROR - 'Tier2TaxonomyMain' value '{tier2_main_value}' does not belong to the possible values of '{tier1_main_value}'."
                            )
                            continue

                        if (
                            tier2_alternative_value != "N/A"
                            and tier2_alternative_value
                            not in tier2_possible_values.get(
                                tier1_alternative_value, []
                            )
                        ):
                            print(
                                f"ERROR - 'Tier2TaxonomyAlternative' value '{tier2_alternative_value}' does not belong to the possible values of '{tier1_alternative_value}'."
                            )
                            continue

                        ordered_response_json_data = OrderedDict(
                            [
                                ("SubstepNumber", response_json_data["SubstepNumber"]),
                                ("SubstepString", response_json_data["SubstepString"]),
                                (
                                    "Tier1TaxonomyMain",
                                    response_json_data["Tier1TaxonomyMain"],
                                ),
                                (
                                    "Tier2TaxonomyMain",
                                    response_json_data["Tier2TaxonomyMain"],
                                ),
                                (
                                    "Tier1TaxonomyAlternative",
                                    response_json_data["Tier1TaxonomyAlternative"],
                                ),
                                (
                                    "Tier2TaxonomyAlternative",
                                    response_json_data["Tier2TaxonomyAlternative"],
                                ),
                            ]
                        )

                        print("INFO - JSON appears to be well-formed and complete.")
                        tier1_filepath = subtep_filepath.replace(
                            "_tier1.json", "_tier2.json"
                        )

                        with open(tier1_filepath, "w", encoding="utf-8") as tier1_file:
                            json.dump(ordered_response_json_data, tier1_file, indent=4)
                        print(f"Saved `{tier1_filepath}`")

                    else:
                        print("ERROR - JSON may be truncated or invalid.")
                        continue

                else:
                    print("ERROR - JSON may be truncated or invalid.")
                    continue

            except openai.error.InvalidRequestError as e:
                print(f"ERROR - OpenAI - {e}")
                continue

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
