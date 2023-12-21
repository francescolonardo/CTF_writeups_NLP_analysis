import os
import json


def scan_directory_for_files(root_dir, file_pattern, exclude_pattern):
    """
    Scans the directory and subdirectories for files matching the given pattern and excludes files matching the exclude pattern.

    :param root_dir: Root directory to start the scan from.
    :param file_pattern: File pattern to look for.
    :param exclude_pattern: File pattern to exclude.
    :return: A list of file paths matching the given pattern and not matching the exclude pattern.
    """
    matching_files = []

    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(file_pattern) and exclude_pattern not in filename:
                matching_files.append(os.path.join(dirpath, filename))

    return matching_files


def extract_values_from_files(file_paths):
    """
    Extracts the required values from the files, skipping files where 'Substeps' is an empty list.

    :param file_paths: A list of file paths.
    :return: A list of dictionaries containing extracted values.
    """
    data = []

    for file_path in file_paths:
        with open(file_path, "r") as f:
            file_data = json.load(f)

            # Skip the file if 'Substeps' is not present or the list is empty
            if not file_data.get("Substeps"):
                continue

            # Navigating through the non-empty 'Substeps'
            for step in file_data["Substeps"]:
                substep_string = step.get("SubstepString", None)
                tier1 = step.get("Tier1Taxonomy", None)

                if substep_string or tier1:  # Ensure there's data to add
                    data_entry = {
                        "SubstepString": substep_string,
                        "Tier1Taxonomy": tier1,
                    }
                    data.append(data_entry)

    return data


def main():
    dataset_dir = "../data/dataset_writeups"
    file_pattern = "_tier1.json"
    exclude_pattern = "_steps_"
    output_filename = "../data/list_substeps_tier1.json"

    matching_files = scan_directory_for_files(
        dataset_dir, file_pattern, exclude_pattern
    )

    extracted_data = extract_values_from_files(matching_files)

    with open(output_filename, "w") as out_file:
        json.dump(extracted_data, out_file, indent=4)

    print(f"Processing complete. Output saved to {output_filename}.")


if __name__ == "__main__":
    main()
