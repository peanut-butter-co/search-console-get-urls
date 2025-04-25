import csv
import requests
from urllib.parse import urljoin
import time

# Configuration
INPUT_FILE = '404.csv'
OUTPUT_FILE = '404-codes.csv'
BASE_URL = 'https://grimey.com'  # Base URL to prepend to relative URLs
DELAY = 1  # Delay between requests in seconds to avoid overwhelming the server

def get_status_code(url):
    try:
        # If URL is relative, join it with base URL
        if not url.startswith(('http://', 'https://')):
            url = urljoin(BASE_URL, url)
        
        # Make the request with a timeout
        response = requests.get(url, timeout=10, allow_redirects=True)
        return response.status_code
    except requests.exceptions.RequestException as e:
        # Handle various request exceptions
        if isinstance(e, requests.exceptions.Timeout):
            return "Timeout"
        elif isinstance(e, requests.exceptions.ConnectionError):
            return "Connection Error"
        else:
            return f"Error: {str(e)}"

# Read URLs from input CSV
urls = []
with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)  # Skip header row
    for row in reader:
        if row:  # Check if row is not empty
            urls.append(row[0])

print(f"Found {len(urls)} URLs to check")

# Check status codes and write results
with open(OUTPUT_FILE, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['URL', 'Status Code'])  # Write header
    
    for i, url in enumerate(urls, 1):
        status_code = get_status_code(url)
        writer.writerow([url, status_code])
        
        # Print progress
        print(f"Checked {i}/{len(urls)}: {url} -> {status_code}")
        
        # Add delay between requests
        if i < len(urls):  # Don't delay after the last request
            time.sleep(DELAY)

print(f"✅ Results saved to {OUTPUT_FILE}")
