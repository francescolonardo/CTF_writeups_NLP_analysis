import os
import json


def create_steps_json(file_path):
    # Getting the file name without extension and replacing _summary with _steps
    base_name = os.path.splitext(file_path)[0].replace("_summary", "_steps")

    with open(file_path, "r") as file:
        lines = file.readlines()

    steps = [
        {"StepNumber": index + 1, "StepString": line.strip()}
        for index, line in enumerate(lines)
    ]
    attack_model = {"AttackModel": {"Steps": steps}}

    # Correcting the output file name to base_name + ".json"
    json_file_path = f"{base_name}.json"
    with open(json_file_path, "w") as file:
        json.dump(attack_model, file, indent=4)
    print(f"Created: {json_file_path}")


def main():
    directory = "../dataset_writeups"  # Start directory, can replace with the directory of your choice

    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith("_summary.txt"):
                summary_file_path = os.path.join(foldername, filename)
                json_file_path = summary_file_path.replace(
                    "_summary.txt", "_steps.json"
                )

                if not os.path.exists(json_file_path):
                    create_steps_json(summary_file_path)


if __name__ == "__main__":
    main()
