from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import json

# Path to the JSON key you downloaded
KEY_FILE = './key.json'

# Define the required scope
SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]

# Create credentials object from the key file
print("credentials:")

# Create credentials object with scope
credentials = Credentials.from_service_account_file(KEY_FILE, scopes=SCOPES)

# Set up the API service
webmasters_service = build('searchconsole', 'v1', credentials=credentials)

# Make an API request to fetch data
request = {
    'startDate': '2020-01-01', 
    'endDate': '2025-04-25',
    'dimensions': ['query', 'page'],
    'rowLimit': 25000  # Maximum allowed by the API
}

# Initialize variables for pagination
all_rows = []
start_row = 0

while True:
    # Add startRow parameter for pagination
    request['startRow'] = start_row
    
    # Make the API request
    response = webmasters_service.searchanalytics().query(
        siteUrl='https://grimey.com/', 
        body=request
    ).execute()
    
    # Get the rows from the response
    rows = response.get('rows', [])
    
    # If no more rows, break the loop
    if not rows:
        break
    
    # Add the rows to our collection
    all_rows.extend(rows)
    
    # Update the start row for the next iteration
    start_row += len(rows)
    
    print(f"Fetched {len(rows)} rows. Total so far: {len(all_rows)}")

# Create the final response structure
final_response = {
    'rows': all_rows,
    'responseAggregationType': response.get('responseAggregationType', ''),
    'rowsPerPage': response.get('rowsPerPage', 0),
    'totalRows': len(all_rows)
}

# Save the complete data to a JSON file
with open('results-all.json', 'w') as f:
    json.dump(final_response, f)

print(f"✅ Results saved to results.json. Total rows: {len(all_rows)}")