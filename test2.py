import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.http import MediaFileUpload
import datetime

Path_File_Secret = ""

CLIENT_SECRET_FILE = Path_File_Secret
SCOPES=["https://www.googleapis.com/auth/youtube.upload"]

flow=InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
credentials=flow.run_console()
youtube=build("youtube", "v3", credentials=credentials)

#print(youtube)

upload_date_tieme = datetime.datetime(2020, 12, 25, 12, 30, 0).isoformat() + ".000z"

request_body = {
    "snippet": {
        "categoryI": 19,
        "title": "Cargando video",
        "description": "Hola Video"
    },
    "status":{
        "privacyStatus":"private",
        "publishAt":upload_date_tieme,
        "selfDeclaredMadeForKids":False,
        "madeForKids": False,

    },
    "notifySubscribers": False
}

mediaFile = MediaFileUpload("/home/jorgeda/Downloads/Quantil/Automation_TI/Youtube/zoom_0.mp4")

print('Cargando Video...')
response_upload = youtube.videos().insert(
    part="snippet,status",
    body=request_body,
    media_body=mediaFile
).execute()

print('Video Cargado!')

"""Referencias"""
# https://github.com/youtube/api-samples/blob/master/python/upload_video.py
# https://www.youtube.com/watch?v=2zYJMI_OPIY
# https://github.com/youtube/api-samples/tree/master/python

