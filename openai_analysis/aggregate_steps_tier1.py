import os
import json
import re


def find_unpaired_files(directory):
    all_files = {}
    max_substeps = {}  # New dictionary to store the max substeps for each prefix

    # Walk through directory and all its subdirectories
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            # Extract substeps number
            substep_match = re.match(r".*_substeps_(\d+)(?:_tier1)?\.json$", filename)
            if substep_match:
                substep_num = int(substep_match.group(1))
                prefix = filename.split("_substeps_")[0]

                # Update the max substeps for this prefix if required
                if prefix not in max_substeps or substep_num > max_substeps[prefix]:
                    max_substeps[prefix] = substep_num

                # Separate the storage of tier1 and normal substeps
                if "_tier1" in filename:
                    if prefix not in all_files:
                        all_files[prefix] = []
                    all_files[prefix].append(os.path.join(dirpath, filename))

    unpaired_files = {}

    # Check for each prefix if *_substeps_tier1.json file exists
    for prefix, filepaths in all_files.items():
        tier1_file = os.path.join(
            os.path.dirname(filepaths[0]), f"{prefix}_substeps_tier1.json"
        )
        if not os.path.exists(tier1_file) and len(filepaths) == max_substeps[prefix]:
            unpaired_files[prefix] = sorted(filepaths)

    return unpaired_files


def create_aggregated_json(unpaired_files):
    for prefix, filepaths in unpaired_files.items():
        content = []
        for filepath in filepaths:
            with open(filepath, "r") as f:
                content.append(json.load(f))
        aggregated_content = {"AttackModel": {"Steps": content}}

        output_file_path = os.path.join(
            os.path.dirname(filepaths[0]), "..", f"{prefix}_tier1.json"
        )
        with open(output_file_path, "w") as out_file:
            json.dump(aggregated_content, out_file, indent=4)
        print(
            f"Created output file: {output_file_path}"
        )  # Added print statement for each output file


if __name__ == "__main__":
    directory = "../dataset_writeups"
    unpaired_files = find_unpaired_files(directory)
    create_aggregated_json(unpaired_files)
    print(f"Processed {len(unpaired_files)} unpaired files.")
