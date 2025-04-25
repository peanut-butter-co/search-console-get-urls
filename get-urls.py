from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

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
    'dimensions': ['query', 'page']
}
response = webmasters_service.searchanalytics().query(
    siteUrl='https://grimey.com/', 
    body=request
).execute()

# Print the response data 
print(response)