import json
import csv

# Input and output file names
input_json = 'results-all.json'
output_csv = 'results-all.csv'

# Load JSON data from file
with open(input_json, 'r', encoding='utf-8') as f:
    gsc_data = json.load(f)

# Open CSV file for writing
with open(output_csv, mode='w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)

    # Write header row
    writer.writerow([
        "Title",
        "Url",
        "Clicks",
        "Impressions",
        "Click Through Rate",
        "Position"
    ])

    # Write each data row
    for row in gsc_data.get("rows", []):
        keys = row.get("keys", ["", ""])
        writer.writerow([
            keys[0],                            # Title
            keys[1],                            # URL
            row.get("clicks", 0),
            row.get("impressions", 0),
            row.get("ctr", 0),
            row.get("position", 0)
        ])

print(f"✅ CSV export complete: {output_csv}")