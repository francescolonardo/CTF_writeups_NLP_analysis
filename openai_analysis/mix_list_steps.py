import json
import random

# Name of the input JSON file
input_file_name = "list_steps.json"

# Name of the output JSON file
output_file_name = "list_steps_mixed.json"

try:
    # Read the input JSON file
    with open(input_file_name, "r", encoding="utf-8") as input_file:
        strings = json.load(input_file)

    if not isinstance(strings, list) or not all(
        isinstance(item, str) for item in strings
    ):
        raise ValueError("The JSON file must contain a list of strings.")

    # Shuffle the order of strings
    random.shuffle(strings)

    # Write the shuffled strings to the output JSON file
    with open(output_file_name, "w", encoding="utf-8") as output_file:
        json.dump(strings, output_file, indent=4)

    print(f"The order of strings has been mixed and saved to {output_file_name}")

except FileNotFoundError:
    print(f"{input_file_name} not found.")
except json.JSONDecodeError:
    print(f"{input_file_name} is not a valid JSON file.")
except ValueError as ve:
    print(str(ve))
