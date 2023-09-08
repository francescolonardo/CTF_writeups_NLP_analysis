import os
import re

# Create a dictionary to map user friendly names to actual language identifiers used in code snippets
lang_map = {"python": "python|py",
            "javascript": "javascript|js",
            "bash": "bash|sh",
            "php": "php",
            "http": "http",
            "html": "html",
            "css": "css"}

# Also create a map for conversion from short form to full form
short_to_full = {"py": "python", "js": "javascript", "sh": "bash", "http": "http", "php": "php", "html": "html", "css": "css"}

def extract_and_replace_snippets(match, base_filename):
    lang, snippet = match.group(1), match.group(2)
    short_lang = lang if lang in short_to_full else [k for k, v in short_to_full.items() if v == lang]
    if not short_lang:
        print(f"Unexpected language identifier: {lang} in the file: {base_filename}")
        return match.group(0)  # return the original text
    short_lang = short_lang[0] if isinstance(short_lang, list) else short_lang
    extract_and_replace_snippets.snippets.append((short_lang, snippet))
    full_lang = short_to_full[short_lang]
    placeholder = f"[./{base_filename}_code{len(extract_and_replace_snippets.snippets):03d}_{full_lang}.txt]"
    return placeholder

extract_and_replace_snippets.snippets = []

def extract_code_snippets(file_path, base_filename):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Extract all code snippets and replace them with placeholders
    for lang, lang_regex in lang_map.items():
        content = re.sub(rf'```({lang_regex})(.*?)```', 
                         lambda m: extract_and_replace_snippets(m, base_filename), 
                         content, flags=re.DOTALL)
    return extract_and_replace_snippets.snippets, content

def save_snippets_and_text(file_path, snippets, text_with_placeholders):
    directory, filename = os.path.split(file_path)
    base_filename = filename.replace('_original.md', '')

    # Create a new directory for each file
    new_directory = os.path.join(directory, base_filename)
    os.makedirs(new_directory, exist_ok=True)

    for i, (lang, snippet) in enumerate(snippets):
        code_filename = f"{base_filename}_code{i+1:03d}_{short_to_full[lang]}.txt"
        code_path = os.path.join(new_directory, code_filename)
        with open(code_path, 'w', encoding='utf-8') as f:
            f.write(snippet)

    text_filename = f"{base_filename}_text.txt"
    text_path = os.path.join(new_directory, text_filename)
    with open(text_path, 'w', encoding='utf-8') as f:
        f.write(text_with_placeholders)

def process_directory(root_dir):
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith("_original.md"):
                file_path = os.path.join(dirpath, filename)
                extract_and_replace_snippets.snippets = []
                base_filename = filename.replace('_original.md', '')
                snippets, text_with_placeholders = extract_code_snippets(file_path, base_filename)
                if snippets:  # Only save snippets and text if there are any snippets
                    save_snippets_and_text(file_path, snippets, text_with_placeholders)

if __name__ == "__main__":
    dataset_writeups_dir = "dataset_writeups"
    process_directory(dataset_writeups_dir)
               
