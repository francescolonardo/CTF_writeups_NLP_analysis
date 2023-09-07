import os
import random
import re
import argparse

# Create a dictionary to map user friendly names to actual language identifiers used in code snippets
lang_map = {"python": "python|py", 
            "javascript": "javascript|js", 
            "bash": "bash|sh", 
            "php": "php",
            "http": "http"}

def find_code_snippets(md_file, lang_regex):
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
        snippets = re.findall(rf'```(?:{lang_regex})(.*?)```', content, re.DOTALL)
        return snippets

def get_random_code_snippet(directory, lang_regex):
    code_snippets = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                md_file = os.path.join(root, file)
                snippets = find_code_snippets(md_file, lang_regex)
                code_snippets.extend(snippets)

    if code_snippets:
        random_snippet = random.choice(code_snippets)
        print(random_snippet)
    else:
        print(f"No {lang_regex} code snippets were found in the specified directory.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Find specific language code snippets.')
    parser.add_argument('-l', '--language', type=str, help='The programming language to extract snippets for.')
    args = parser.parse_args()

    directory = '../dataset_writeups/humans'
    if args.language:
        if args.language.lower() in lang_map:
            get_random_code_snippet(directory, lang_map[args.language.lower()])
        else:
            print("Invalid language. Please choose from 'python', 'javascript', 'bash', 'php', or 'http'.")
    else:
        all_lang_regex = "|".join(lang_map.values())
        get_random_code_snippet(directory, all_lang_regex)
