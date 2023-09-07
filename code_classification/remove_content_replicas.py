import json
from collections import Counter

programming_languages = ["bash", "python", "javascript", "php", "html", "css"]

for lang in programming_languages:
    file_name = f"dataset_content_{lang}.jsonl"

    # Step 1: Load the .jsonl file.
    with open(file_name, 'r', encoding="utf-8") as f:
        lines = f.readlines()

    # Step 2: Extract the 'content' field from each JSON object.
    contents = [json.loads(line)['content'] for line in lines]

    # Step 3: Keep track of the frequency of each code snippet.
    content_counter = Counter(contents)

    # Step 4: Write back to the same .jsonl file only the JSON objects with unique code snippets.
    unique_lines = []
    for line in lines:
        obj = json.loads(line)
        if content_counter[obj['content']] == 1:
            unique_lines.append(json.dumps(obj) + '\n')

    with open(file_name, 'w', encoding="utf-8") as f:
        f.writelines(unique_lines)

    print(f"Number of unique lines in the {lang} file: {len(unique_lines)}")
