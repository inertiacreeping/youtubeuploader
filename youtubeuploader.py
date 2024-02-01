import datetime
import os
import json
import re
import time
from datetime import datetime, timedelta
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# YouTube API setup
CLIENT_SECRETS_FILE = "YOUR_CLIENT_SECRET_FILE.json"
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

# Root directory to scan for videos
ROOT_VIDEO_DIRECTORY = r'C:\Timelapse\snapshots'  # Use a raw string for file paths
UPLOADED_VIDEOS_FILE = 'uploaded_videos.json'
CHECK_INTERVAL = 3600  # Check every hour (3600 seconds)

def get_authenticated_service():
    print("Starting authentication process...")
    creds = None
    if os.path.exists('token.pickle'):
        print("Found existing token.pickle file.")
        with open('token.pickle', 'rb') as token:
            creds = Credentials.from_authorized_user_file('token.pickle', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            print("Refreshing expired credentials...")
            creds.refresh(Request())
        else:
            print("Generating new credentials...")
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'w') as token:
            token.write(creds.to_json())
    print("Authentication successful.")
    return build(API_SERVICE_NAME, API_VERSION, credentials=creds)

def upload_video(youtube, file_path, title):
    print(f"Preparing to upload video: {file_path}")
    body = {
        'snippet': {
            'title': title,
            'description': ("This is a daily timelapse of Napier from just north of the Taupo road. "
                            "Please note that future videos will be uploaded to my new channel - "
                            "Napier Views - Timelapse (https://www.youtube.com/channel/UCfQugnGB8jHH-AjBNT8DtcQ)"),
            'tags': ['timelapse', 'Napier'],
            'categoryId': '22'
        },
        'status': {
            'privacyStatus': 'public'
        }
    }
    media = MediaFileUpload(file_path, chunksize=-1, resumable=True)
    request = youtube.videos().insert(part='snippet,status', body=body, media_body=media)
    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f"Uploaded {int(status.progress() * 100)}%")
    print(f"Upload Complete: {response['snippet']['title']}")

def get_video_files():
    print("Scanning for video files...")
    files = []
    for root, dirs, filenames in os.walk(ROOT_VIDEO_DIRECTORY):
        for filename in filenames:
            if filename.startswith("TIMELAPSE_") and filename.endswith(".mp4"):
                print(f"Found file: {filename}")
                match = re.match(r"TIMELAPSE_(.*?)_(\d{4}-\d{2}-\d{2})_.*\.mp4", filename)
                if match:
                    video_date = datetime.strptime(match.group(2), "%Y-%m-%d")
                    if datetime.now() - video_date < timedelta(days=7):
                        files.append(os.path.join(root, filename))
                        print(f"Adding file to upload list: {filename}")
    if not files:
        print("No new video files found for upload.")
    return files

def read_uploaded_videos():
    print("Reading list of previously uploaded videos...")
    if os.path.exists(UPLOADED_VIDEOS_FILE):
        with open(UPLOADED_VIDEOS_FILE, 'r') as file:
            return json.load(file)
    return {}

def write_uploaded_videos(videos):
    print("Updating list of uploaded videos...")
    with open(UPLOADED_VIDEOS_FILE, 'w') as file:
        json.dump(videos, file)

def main():
    print("Starting YouTube upload script...")
    youtube = get_authenticated_service()
    
    while True:
        uploaded_videos = read_uploaded_videos()
        video_files_to_upload = get_video_files()
        
        for video_file in video_files_to_upload:
            if video_file not in uploaded_videos:
                # Calculate yesterday's date instead of reading from the filename
                yesterday_date = datetime.now() - timedelta(days=1)
                title_date = yesterday_date.strftime("%A %d/%m/%Y")
                title = f"Napier Timelapse: {title_date}"

                upload_video(youtube, video_file, title)
                uploaded_videos[video_file] = True
                write_uploaded_videos(uploaded_videos)
                print(f"Uploaded: {os.path.basename(video_file)}")
            else:
                print(f"File already uploaded: {os.path.basename(video_file)}")
        
        print(f"Waiting for {CHECK_INTERVAL} seconds before next check.")
        time.sleep(CHECK_INTERVAL)

if __name__ == '__main__':
    main()
