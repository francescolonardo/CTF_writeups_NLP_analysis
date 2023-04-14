import os
import pandas as pd

def convert_files():
    # Walk the current directory and its subdirectories
    for root, dirs, files in os.walk('.'):
        # Iterate over the files in the current directory
        for filename in files:
            # Check if the file is an Excel file
            if filename.endswith('.xlsx'):
                # Construct the output filename
                output_filename = os.path.splitext(filename)[0] + '.csv'
                # Load the Excel file into a pandas dataframe
                df = pd.read_excel(os.path.join(root, filename))
                # Write the dataframe to a CSV file with UTF-8 encoding
                df.to_csv(os.path.join(root, output_filename), encoding='utf-8', index=False)

# Call the function to convert the files
convert_files()
