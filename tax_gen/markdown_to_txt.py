import os
import markdown2
from bs4 import BeautifulSoup

# Function to convert a Markdown file to plain text and remove HTML tags
def convert_markdown_to_text(markdown_file):
    with open(markdown_file, 'r', encoding='utf-8') as f:
        markdown_content = f.read()
        html_content = markdown2.markdown(markdown_content)
        # Parse HTML and remove tags
        soup = BeautifulSoup(html_content, 'html.parser')
        text_content = soup.get_text()
        return text_content

# Function to traverse a directory and convert Markdown files to text
def convert_directory_to_text(directory):
    # Create the "txt_writeups" folder if it doesn't exist
    txt_folder = os.path.join(directory, "txt_writeups")
    os.makedirs(txt_folder, exist_ok=True)
    
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".md"):
                markdown_file = os.path.join(root, filename)
                txt_filename = os.path.splitext(filename)[0] + ".txt"
                txt_filepath = os.path.join(txt_folder, txt_filename)
                text_content = convert_markdown_to_text(markdown_file)
                with open(txt_filepath, 'w', encoding='utf-8') as txt_file:
                    txt_file.write(text_content)

# Specify the directory to traverse
directory_to_convert = "./markdown_writeups"

# Call the function to convert Markdown files to text and store them in "txt_writeups" folder
convert_directory_to_text(directory_to_convert)
