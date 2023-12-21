import os
import json
from random import shuffle


def load_input_data(filename):
    with open(filename, "r") as file:
        return json.load(file)


def organize_data_by_taxonomy(data):
    taxonomy_to_substep = {}

    for entry in data:
        for taxonomy_key in ["Tier1TaxonomyMain", "Tier1TaxonomyAlternative"]:
            taxonomy_value = entry[taxonomy_key]

            # Determine the origin (main/alternative)
            origin = "main" if taxonomy_key == "Tier1TaxonomyMain" else "alternative"

            if taxonomy_value not in taxonomy_to_substep:
                taxonomy_to_substep[taxonomy_value] = {"main": [], "alternative": []}

            taxonomy_to_substep[taxonomy_value][origin].append(entry["SubstepString"])

    return taxonomy_to_substep


def save_data_to_files(data, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for taxonomy, origins in data.items():
        # Clean up the taxonomy_value
        clean_taxonomy = (
            taxonomy.replace(" ", "-").replace("/", "-").replace(",", "").lower()
        )

        # Shuffle combined substeps (both main and alternative)
        combined_substeps = origins["main"] + origins["alternative"]
        shuffle(combined_substeps)  # <-- Shuffle here
        output_filename_combined = os.path.join(
            output_folder, f"list_substeps_tier1_{clean_taxonomy}.json"
        )
        with open(output_filename_combined, "w") as file:
            json.dump(combined_substeps, file, indent=4)

        # Shuffle main substeps
        shuffle(origins["main"])  # <-- Shuffle here
        output_filename_main = os.path.join(
            output_folder, f"list_substeps_tier1_{clean_taxonomy}_main.json"
        )
        with open(output_filename_main, "w") as file:
            json.dump(origins["main"], file, indent=4)

        # Shuffle alternative substeps
        shuffle(origins["alternative"])  # <-- Shuffle here
        output_filename_alternative = os.path.join(
            output_folder, f"list_substeps_tier1_{clean_taxonomy}_alternative.json"
        )
        with open(output_filename_alternative, "w") as file:
            json.dump(origins["alternative"], file, indent=4)


def main():
    input_filename = "list_substeps_tier1.json"
    output_folder = "list_substeps_tier1"
    data = load_input_data(input_filename)
    organized_data = organize_data_by_taxonomy(data)
    save_data_to_files(organized_data, output_folder)
    print(f"Processing complete. Files saved to the `{output_folder}` directory.")


if __name__ == "__main__":
    main()
