import os
import json

# Start directory
start_directory = "../dataset_writeups"

for foldername, subfolders, filenames in os.walk(start_directory):
    for filename in filenames:
        if filename.endswith("_presteps.json"):
            presteps_filepath = os.path.join(foldername, filename)
            steps_filepath = os.path.join(
                foldername, filename.replace("_presteps", "_steps")
            )

            # Check if corresponding _steps.json file already exists
            if os.path.exists(steps_filepath):
                print(f"{steps_filepath} already exists. Skipping...")
                continue

            try:
                # Load _presteps.json file
                with open(presteps_filepath, "r") as f:
                    content = json.load(f)

                # Check if content is a list of strings
                if not all(isinstance(item, str) for item in content):
                    print(
                        f"{presteps_filepath} does not contain a list of strings. Skipping..."
                    )
                    continue

                # Prepare the output JSON structure
                output = {
                    "StepsModel": {
                        "Steps": [
                            {"StepNumber": idx + 1, "StepString": step}
                            for idx, step in enumerate(content)
                        ]
                    }
                }

                # Write _steps.json file
                with open(steps_filepath, "w") as f:
                    json.dump(output, f, indent=4)

                print(f"Successfully created {steps_filepath}")

            except json.JSONDecodeError:
                print(f"Failed to parse JSON in {presteps_filepath}. Skipping...")
            except Exception as e:
                print(f"Error processing {presteps_filepath}: {e}. Skipping...")

print("Processing Completed!")
