"""
Script to read the students.csv file and convert it to a students.yml file
Displays name, info(project name), yr(years in SenseLab), link
Sorts the students by name
"""

import csv
import yaml
import pandas as pd
import os

# Determine the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the paths to the CSV and YAML files relative to the script directory
csv_file = os.path.join(script_dir, '../_data/students.csv')
yaml_file = os.path.join(script_dir, '../_data/students.yml')

df = pd.read_csv(csv_file)

# Rename columns to match the YAML specifications
df.rename(columns={'Name':'name','Projects involved in (separated by ;)': 'info','Years in SenseLab(from-to)': 'yr','link to your url':'link'}, inplace=True)

# Sort the DataFrame by the 'name' column
df.sort_values(by='name', inplace=True)

# Convert DataFrame to list of dictionaries
data = df.to_dict(orient='records')
print(data)

# Write to YAML file with ordered columns
with open(yaml_file, mode='w') as outfile:
    outfile.write("# do not make any changes to this file\n")
    yaml.dump(data, outfile, default_flow_style=False, sort_keys=False)