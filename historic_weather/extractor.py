import json
import csv

# Load the JSON file
with open('Tokyo_historic.txt', 'r') as json_file:
    data = json.load(json_file)

# Mapping of JSON keys to desired CSV column names
field_mapping = {
    'datetime': 'date',
    'tempmin': 'min_temp',
    'tempmax': 'max_temp',
    'precip': 'total_rainfall',
    'conditions': 'conditions',
    'icon': 'icon'
}

# Extract the desired fields
fields = list(field_mapping.keys())
csv_headers = list(field_mapping.values())

# Open a new CSV file to write
with open('tokyo_historic.csv', 'w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers, quoting=csv.QUOTE_NONNUMERIC)
    
    # Write the header
    writer.writeheader()
    
    # Extract the 'days' array and write rows
    for day in data['days']:
        # Map the fields to the new names
        row = {field_mapping[key]: day[key] for key in fields}
        writer.writerow(row)

print("CSV file has been created")