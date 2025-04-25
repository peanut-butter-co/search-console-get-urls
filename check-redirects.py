import csv
import requests
from urllib.parse import urljoin
import time

# Configuration
RESULTS_FILE = 'results.csv'
REDIRECTS_FILE = 'redirects.csv'
OUTPUT_FILE = 'redirects-analisis.csv'
BASE_URL = 'https://grimey.com'
DELAY = 1  # seconds

def get_status_code(url):
    try:
        if not url.startswith(('http://', 'https://')):
            url = urljoin(BASE_URL, url)
        response = requests.get(url, timeout=10, allow_redirects=True)
        return response.status_code
    except requests.exceptions.Timeout:
        return "Timeout"
    except requests.exceptions.ConnectionError:
        return "Connection Error"
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

# Load redirects into a dictionary
redirects_dict = {}
with open(REDIRECTS_FILE, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)  # Skip header if present
    for row in reader:
        if len(row) >= 2:
            redirects_dict[row[0].strip()] = row[1].strip()

# Read input URLs from results.csv
urls = []
with open(RESULTS_FILE, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)  # Skip header if present
    for row in reader:
        if row:
            urls.append(row[0].strip())

# Process and write to output
with open(OUTPUT_FILE, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['URL', 'Redirect', 'Status'])  # Header

    for i, url in enumerate(urls, 1):
        if url in redirects_dict:
            redirect = redirects_dict[url]
            writer.writerow([url, redirect, ''])  # Redirect found
            print(f"{i}/{len(urls)}: Found redirect for {url} -> {redirect}")
        else:
            status = get_status_code(url)
            writer.writerow([url, '', status])  # No redirect, fetch status
            print(f"{i}/{len(urls)}: Checked {url} -> {status}")
            if i < len(urls):
                time.sleep(DELAY)

print(f"✅ Analysis complete. Output saved to {OUTPUT_FILE}")
