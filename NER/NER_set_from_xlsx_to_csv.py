import pandas as pd

# Read the data from the Excel file
df = pd.read_excel('NER_set.xlsx')

# Write the data to a CSV file encoded with utf-8
df.to_csv('NER_set.csv', index=False, encoding='utf-8')
