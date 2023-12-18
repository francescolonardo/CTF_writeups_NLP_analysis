import os
import json


def find_files_in_directory(path, pattern, exclude_folder_suffix):
    """
    Search for files that match a specific pattern in a directory (and its subdirectories)
    while excluding files inside folders with a specified suffix.
    """
    matched_files = []

    for dirpath, _, filenames in os.walk(path):
        if dirpath.endswith(
            exclude_folder_suffix
        ):  # Skip directories with a certain suffix
            continue

        for filename in filenames:
            if filename.endswith(pattern):
                matched_files.append(os.path.join(dirpath, filename))

    return matched_files


def process_files(base_path):
    """
    Process the matched files, extract substeps, and write them to new files.
    """
    # Fetch all the files that match the pattern
    files_to_process = find_files_in_directory(base_path, "_tier1.json", "_steps")

    for file in files_to_process:
        with open(file, "r") as f:
            content = json.load(f)
            steps = content.get("AttackModel", {}).get("Steps", [])

            substep_count = 1
            writeup_title = file.split("_tier1.json")[0].split(os.sep)[-1]

            # Create a directory for the substeps
            substep_dir = os.path.join(
                os.path.dirname(file), f"{writeup_title}_substeps_tier1"
            )
            if not os.path.exists(substep_dir):
                os.makedirs(substep_dir)
                print(f"Folder '{substep_dir}' created successfully!")

            # Extract substeps and write them to separate files
            for step in steps:
                for substep in step.get("Substeps", []):
                    substep_file = os.path.join(
                        substep_dir,
                        f"{writeup_title}_substep_{substep_count:03}_tier1.json",
                    )
                    with open(substep_file, "w") as outfile:
                        json.dump(substep, outfile, indent=4)
                    print(f"File '{substep_file}' created successfully!")
                    substep_count += 1


if __name__ == "__main__":
    # Define the base directory here
    base_directory = "../dataset_writeups"  # replace with your directory path
    process_files(base_directory)
