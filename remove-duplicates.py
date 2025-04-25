import json
import csv
from urllib.parse import urlparse, urlunparse

# Function to remove query parameters from URL
def clean_url(url):
    parsed = urlparse(url)
    # Reconstruct URL without query parameters
    return urlunparse((
        parsed.scheme,
        parsed.netloc,
        parsed.path,
        '',  # params
        '',  # query
        ''   # fragment
    ))

# Read the JSON file
with open('results-all.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Extract URLs and remove duplicates
unique_urls = set()
for row in data.get('rows', []):
    if len(row.get('keys', [])) > 1:  # Ensure we have a URL
        url = row['keys'][1]  # URL is in keys[1]
        clean = clean_url(url)
        unique_urls.add(clean)

# Sort URLs alphabetically
sorted_urls = sorted(unique_urls)

# Write to CSV
with open('results.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    # Write header
    writer.writerow(['URL'])
    # Write each URL
    for url in sorted_urls:
        writer.writerow([url])

print(f"✅ Processed {len(data.get('rows', []))} rows")
print(f"✅ Found {len(unique_urls)} unique URLs")
print(f"✅ Results saved to results.csv")
