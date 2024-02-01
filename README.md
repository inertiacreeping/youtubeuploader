# youtubeuploader
The (Automatic) Youtube Uploader (For Timelapses)

Welcome to the most automated, slightly magical way to upload your daily doses of breathtaking views to YouTube. 
(I use my (Timelapse Creator script)[https://github.com/inertiacreeping/Unifi-Timelapse] to create a daily timelapse of my local views, then this script monitors the output folder for new timelapse videos, and uploads them.)

## What It Does 🚀

This Python script automatically scans and uploads any new videos in a specified folder to a specified YouTube channel every hour. 
Which videos will it upload? This script checks the filename of the video files it finds and only updates videos matching the last 7 days.

## Getting Started 🛠

Before you embark on this journey, there are a few things you need to set up:

### Google Cloud and YouTube API

This guide will walk you through creating a project in Google Cloud, enabling the YouTube Data API, and setting up OAuth 2.0 credentials for your Napier Timelapse Uploader.

#### Step 1: Create a Google Cloud Project

1. **Sign in to Google Cloud Platform**
   - Go to the [Google Cloud Console](https://console.cloud.google.com/) and sign in with your Google account. Create an account if you don't have one, obviously.

2. **Create a New Project**
   - Click on the project dropdown near the top left of the page.
   - Click the "New Project" text in the top right of the new popup.
   - Enter a project name and select a billing account if prompted.
   - Click "Create".

#### Step 2: Enable the YouTube Data API v3

1. **Search for the YouTube Data API v3**
   - Use the top search bar to find "YouTube Data API v3".
2. **Enable the API**
   - Click on the YouTube Data API v3 and press "Enable".

#### Step 3: Create Credentials

1. **Access the Credentials Page**
   - Once the YouTube API has been enabled, click on the blue "Manage" button.
   - Once you're redirected to the API metrics page, click on "Create Credentials" blue button in the top right.

2. **Configure the OAuth Consent Screen**
   - Select the **user** data type 
   - Fill in the required fields (app name, user support email, developer contact information).
   - Save and continue, add scopes if necessary (I dunno, select all scopes).
   - Select "Desktop app" as the application type.
   - Name your OAuth client and click "Create".

4. **Download the JSON File**
   - Find the newly created credentials and click the download button to get your `YOUR_CLIENT_SECRET_FILE.json`.

## Step 4: Install Required Python Packages

Ensure you have the necessary Python packages:

```bash
pip install --upgrade google-api-python-client google-auth-oauthlib


### Youtube API Services - Audit and Quota Extension Form

You'll need to fill out this (annoying form)[https://support.google.com/youtube/contact/yt_api_form?hl=en] for your channel, so that the videos aren't locked to private (to combat spam). Takes 2-5 days for Youtube to approve your app.

### Prerequisites

- Python 3.x installed on your system.
- `google-api-python-client` and `google-auth-oauthlib` packages installed. You can install them via pip:

```bash
pip install --upgrade google-api-python-client google-auth-oauthlib
```

- A Google Cloud project with the YouTube Data API v3 enabled (you should have done this previously)
- OAuth 2.0 credentials for a Desktop app downloaded as YOUR_CLIENT_SECRET_FILE.json.

### Installation

1. Clone this repository to your local machine or download the script directly.
2. Replace YOUR_CLIENT_SECRET_FILE.json with the path to your downloaded OAuth 2.0 credentials file (or just put your secrets file in the same folder as the script)
3. Update the ROOT_VIDEO_DIRECTORY in the script to point to your timelapse videos directory (by default it's C:\Timelapse\snapshots)

### Usage
Simply run the script with Python and let the magic happen:

```bash
python youtube_upload.py
```

The script does its rounds every hour, checking for new timelapse videos and uploading them with the correct yesterday date in the title.

### Features ✨
- Automatically uploads timelapse videos to YouTube.
- Titles the video based on the date of the day before, regardless of the filename.
- Adds a custom description for each video, sharing a snippet about the view and directing viewers to a new channel for future uploads.
- Maintains a log of uploaded videos to avoid duplicates.

### Customizing Your Uploads 🎨
- Feel free to tweak the upload_video function to include your preferred tags, categories, or even modify the video description. This script is just a starting point to automate your uploads. 

### Acknowledgments 🙏
Yeah, not gonna lie, this was all ChatGPT (I can't code to save my life). But hey, it works.

### License 📄
Do whatever you want with it.
