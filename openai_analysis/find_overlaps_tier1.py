import json
import os


def sanitize_filename(filename):
    filename = filename.replace("/", "-").replace(" ", "-")
    filename = filename.replace(",", "")
    return filename.lower()


# 1. Read the input JSON file
with open("list_substeps_tier1.json", "r") as file:
    data = json.load(file)

# 2. Iterate and categorize
categorized_data = {}

for record in data:
    main_category = record["Tier1TaxonomyMain"]
    alternative_category = record["Tier1TaxonomyAlternative"]
    substep_string = record["SubstepString"]

    # Initialize the main category if not present
    if main_category not in categorized_data:
        categorized_data[main_category] = {}

    # Append the substep string to the appropriate category
    categorized_data[main_category].setdefault(alternative_category, []).append(
        substep_string
    )

# 3. Write the result to output files
output_directory = "overlaps_tier1"
os.makedirs(output_directory, exist_ok=True)

for main_category, values in categorized_data.items():
    formatted_data = [{key: value} for key, value in values.items()]

    # Use the sanitized filename when saving
    with open(
        f"{output_directory}/overlaps_tier1_{sanitize_filename(main_category)}.json",
        "w",
    ) as file:
        json.dump(formatted_data, file, indent=4)

print(f"All files have been saved to `{output_directory}`.")
