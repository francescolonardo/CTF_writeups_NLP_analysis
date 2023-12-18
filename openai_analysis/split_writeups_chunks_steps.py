import os
import json


def find_substeps_files(directory):
    """
    Scans a directory for [filename]_substeps.json files
    :param directory: Directory to scan
    :return: List of file paths
    """
    matches = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith("_substeps.json"):
                matches.append(os.path.join(root, filename))
    return matches


def split_and_save(json_file):
    """
    Splits the input json file into multiple chunks and save each chunk as a separate file
    :param json_file: Path to the input json file
    """
    with open(json_file, "r", encoding="utf-8") as file:
        data = json.load(file)
        if "AttackModel" in data and "Steps" in data["AttackModel"]:
            steps = data["AttackModel"]["Steps"]
            raw_filename = os.path.splitext(os.path.basename(json_file))[0]
            filename = raw_filename.replace("_substeps", "")
            dir_path = os.path.dirname(json_file)

            # Create a folder named after the json_file without its extension and with "_steps"
            output_dir = os.path.join(dir_path, filename + "_steps")
            os.makedirs(
                output_dir, exist_ok=True
            )  # 'exist_ok=True' ensures no error if the directory already exists

            for index, step in enumerate(steps):
                out_filename = os.path.join(
                    output_dir, f"{filename}_step_{index + 1:02}.json"
                )
                try:
                    with open(out_filename, "w", encoding="utf-8") as out_file:
                        json.dump(step, out_file, indent=4)
                except FileNotFoundError as e:
                    print(
                        f"Error writing to {out_filename}. Directory exists: {os.path.exists(output_dir)}"
                    )
                    raise e


if __name__ == "__main__":
    directory = os.path.join("..", "dataset_writeups")
    files = find_substeps_files(directory)
    for file in files:
        split_and_save(file)
