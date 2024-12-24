import csv
import yaml
import pandas as pd

# Read CSV file
csv_file = '../_data/students.csv'
yaml_file = '../_data/students.yml'

# Read CSV file into DataFrame
df = pd.read_csv(csv_file)

# Rename columns
df.rename(columns={'Name':'name','Projects involved in (separated by ;)': 'info','Years in SenseLab(from-to)': 'yr','link to your url':'link'}, inplace=True)

# Convert DataFrame to list of dictionaries
data = df.to_dict(orient='records')
print(data)

# Write to YAML file with ordered columns
with open(yaml_file, mode='w') as outfile:
    yaml.dump(data, outfile, default_flow_style=False, sort_keys=False)