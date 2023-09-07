import os
import json
import csv
import fnmatch

def main():
    # Define the CSV output file name
    output_file = "dataset_code_language.csv"
    
    # Get the list of all jsonl files in the current directory
    jsonl_files = [f for f in os.listdir('.') if fnmatch.fnmatch(f, 'dataset_content_*.jsonl')]

    # Open the CSV file in write mode
    with open(output_file, 'w', encoding='utf-8', newline='') as csv_file:
        # Create a CSV writer
        writer = csv.writer(csv_file)
        
        # Write the header row
        writer.writerow(["code", "language"])

        # For each jsonl file
        for jsonl_file in jsonl_files:
            # Extract the language from the file name
            language = jsonl_file.split('_')[2].split('.')[0]

            # Open the jsonl file
            with open(jsonl_file, 'r', encoding='utf-8') as jf:
                # For each line in the jsonl file
                for line in jf:
                    # Load the JSON object
                    data = json.loads(line)
                    
                    # Write the code and language to the CSV file
                    writer.writerow([data["content"], language])

if __name__ == "__main__":
    main()
