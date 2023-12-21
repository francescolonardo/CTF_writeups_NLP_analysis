import os
import json
from random import shuffle


def load_input_data(filename):
    with open(filename, "r") as file:
        return json.load(file)


def organize_data_by_taxonomy(data):
    taxonomy_to_substep = {}

    for entry in data:
        taxonomy_value = entry["Tier1Taxonomy"]

        if taxonomy_value not in taxonomy_to_substep:
            taxonomy_to_substep[taxonomy_value] = []

        taxonomy_to_substep[taxonomy_value].append(entry["SubstepString"])

    return taxonomy_to_substep


def save_data_to_files(data, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for taxonomy, substeps in data.items():
        # Clean up the taxonomy_value
        clean_taxonomy = (
            taxonomy.replace(" ", "-").replace("/", "-").replace(",", "").lower()
        )

        # Shuffle substeps
        shuffle(substeps)
        output_filename = os.path.join(
            output_folder, f"list_substeps_tier1_{clean_taxonomy}.json"
        )
        with open(output_filename, "w") as file:
            json.dump(substeps, file, indent=4)


def main():
    input_filename = "../data/list_substeps_tier1.json"
    output_folder = "../data/list_substeps_tier1"
    data = load_input_data(input_filename)
    organized_data = organize_data_by_taxonomy(data)
    save_data_to_files(organized_data, output_folder)
    print(f"Processing complete. Files saved to the `{output_folder}` directory.")


if __name__ == "__main__":
    main()
