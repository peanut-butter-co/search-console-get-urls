# Google Search Console URL Exporter

This tool allows you to export all indexed URLs from Google Search Console, bypassing the 1000 URLs download limit imposed by the Search Console web interface.

## Prerequisites

- Python 3.x
- Google Cloud Platform account
- Access to the target website in Google Search Console

## Setup Instructions

### 1. Create a Google Cloud Project

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the Search Console API for your project:
   - Go to "APIs & Services" > "Library"
   - Search for "Search Console API"
   - Click "Enable"

### 2. Create a Service Account

1. In the Google Cloud Console, go to "APIs & Services" > "Credentials"
2. Click "Create Credentials" > "Service Account"
3. Fill in the service account details:
   - Name: `search-console-exporter`
   - Description: "Service account for Search Console URL export"
4. Click "Create and Continue"
5. Grant the service account the "Search Console API User" role
6. Click "Done"

### 3. Create and Download Service Account Key

1. In the service account list, find your newly created account
2. Click on the service account name
3. Go to the "Keys" tab
4. Click "Add Key" > "Create new key"
5. Choose JSON format
6. Click "Create"
7. The key file will be downloaded automatically

### 4. Add Service Account to Search Console

1. Go to [Google Search Console](https://search.google.com/search-console)
2. Select your property
3. Go to "Settings" > "Users and permissions"
4. Click "Add User"
5. Enter the service account email (found in the downloaded JSON file as `client_email`)
6. Set permission level to "Full" or "Restricted" (depending on your needs)
7. Click "Add"

### 5. Setup the Project

1. Clone this repository
2. Place the downloaded service account key JSON file in the project root directory
3. Rename the key file to `key.json`

## Usage

1. Install required Python packages:
   ```bash
   pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
   ```

2. Run the URL export script:
   ```bash
   python get-urls.py
   ```

The script will fetch all indexed URLs for the specified site and print them to the console. You can modify the date range and other parameters in the script as needed.

## Script Configuration

You can modify the following parameters in `get-urls.py`:
- `startDate`: Start date for the data range (format: YYYY-MM-DD)
- `endDate`: End date for the data range (format: YYYY-MM-DD)
- `siteUrl`: The URL of your site in Search Console (must match exactly)

## Security Note

Keep your `key.json` file secure and never commit it to version control. The example key file (`key.example.json`) is provided for reference only.

## Troubleshooting

If you encounter permission errors:
1. Verify the service account email has been added to Search Console
2. Check that the Search Console API is enabled in your Google Cloud project
3. Ensure the service account has the correct permissions

## License

This project is open source and available under the MIT License.
