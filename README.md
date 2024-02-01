# youtubeuploader
The (Automatic) Youtube Uploader (For Timelapses)

Welcome to the most automated, slightly magical way to upload your daily doses of breathtaking views to YouTube. 

## What It Does 🚀

This Python script automatically scans and uploads any new videos in a specified folder to a specified YouTube channel every hour. 
Which videos will it upload? This script checks the filename of the video files it finds and only updates videos matching the last 7 days.

## Getting Started 🛠

Before you embark on this journey, there are a few things you need to set up:

### Prerequisites

- Python 3.x installed on your system.
- `google-api-python-client` and `google-auth-oauthlib` packages installed. You can install them via pip:

```bash
pip install --upgrade google-api-python-client google-auth-oauthlib
```

- A Google Cloud project with the YouTube Data API v3 enabled.
- OAuth 2.0 credentials for a Desktop app downloaded as YOUR_CLIENT_SECRET_FILE.json.

### Installation

1. Clone this repository to your local machine or download the script directly.
2. Replace YOUR_CLIENT_SECRET_FILE.json with the path to your downloaded OAuth 2.0 credentials file.
3. Update the ROOT_VIDEO_DIRECTORY in the script to point to your timelapse videos directory.

### Usage
Simply run the script with Python and let the magic happen:

```bash
python youtube_upload.py
```

The script does its rounds every hour, checking for new timelapse videos and uploading them with the correct yesterday date in the title. It's like a time machine, but for YouTube uploads!

### Features ✨
- Automatically uploads timelapse videos to YouTube.
- Titles the video based on the date of the day before, regardless of the filename.
- Adds a custom description for each video, sharing a snippet about the view and directing viewers to a new channel for future uploads.
- Maintains a log of uploaded videos to avoid duplicates.

### Customizing Your Uploads 🎨
- Feel free to tweak the upload_video function to include your preferred tags, categories, or even modify the video description. This script is just a starting point to automate your uploads. The sky (or should we say, the sunset?) is the limit!

### Acknowledgments 🙏
Yeah, not gonna lie, this was all ChatGPT (I can't code to save my life). But hey, it works.

### License 📄
Do whatever you want with it.
