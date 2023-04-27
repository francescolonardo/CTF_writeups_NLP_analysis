import os
import pandas as pd

# Read the input .xlsx file
input_file = "NER_dictionaries.xlsx"
df = pd.read_excel(input_file, header=None, engine="openpyxl")

# Give column names for better readability
df.columns = ["Word", "Category"]

# Get unique category names
unique_categories = df["Category"].unique()

# Create a .csv file for each category
for category in unique_categories:
    category_df = df[df["Category"] == category]
    
    # Set the output file name
    output_file = f"NER_dictionary_{category}.csv"
    
    # Check if the DataFrame is not empty before saving to a .csv file
    if not category_df.empty:
        # Save the DataFrame as a .csv file without header and with utf-8 encoding
        category_df.to_csv(output_file, index=False, header=False, encoding="utf-8")

print("CSV files created successfully.")
