import os
import json

# Change this path to where your files are located
base_path = "./list_substeps_tier1"

# Step 1: List all files
files = [f for f in os.listdir(base_path) if os.path.isfile(os.path.join(base_path, f))]

# Step 2 & 3: Extract tier1_category_name and create folders
categories = set()
for file in files:
    if file.startswith("list_substeps_tier1_") and file.endswith("_main.json"):
        category = file.replace("list_substeps_tier1_", "").replace("_main.json", "")
        categories.add(category)
        category_folder = os.path.join(base_path, category)
        if not os.path.exists(category_folder):
            os.mkdir(category_folder)

# Step 4: Process the *_main.json files
for category in categories:
    main_file_path = os.path.join(base_path, f"list_substeps_tier1_{category}.json")
    with open(main_file_path, "r") as f:
        data = json.load(f)

    # Assuming the JSON file contains a list of strings. Adjust accordingly if the structure is different.
    chunks = [data[x : x + 35] for x in range(0, len(data), 35)]

    for idx, chunk in enumerate(chunks):
        start_idx = idx * 35 + 1
        end_idx = start_idx + len(chunk) - 1
        filename = f"list_substeps_tier1_{category}_{start_idx:04d}-{end_idx:04d}.json"
        chunk_file_path = os.path.join(base_path, category, filename)

        with open(chunk_file_path, "w") as f:
            json.dump(chunk, f, indent=4)

print("Processing complete!")
