import os
import json

input_file = "substeps_groups.json"
output_directory = "./substeps_groups"


def split_and_save(data):
    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Split data into chunks of 100
    for i in range(0, len(data), 100):
        chunk = data[i : i + 100]
        start_index = i + 1
        end_index = i + len(chunk)
        output_filename = f"substeps_groups_{start_index:04}-{end_index:04}.json"
        output_path = os.path.join(output_directory, output_filename)

        # Save the chunk to a file
        with open(output_path, "w") as out_file:
            json.dump(chunk, out_file, indent=4)


def main():
    # Load data from input file
    with open(input_file, "r") as file:
        data = json.load(file)

    split_and_save(data)
    print("Successfully split and saved the data!")


if __name__ == "__main__":
    main()
