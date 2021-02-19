# from apiclient.discovery import build
# from google.oauth2 import service_account
# from pathlib import Path
# import os

# # BASE_DIR = Path(__file__).resolve(strict=True).parent
# # TEMPLATE_DIR = Path.joinpath(BASE_DIR, 'quantyoutube.json')


# #API_KEY = "/home/jorgeda/Downloads/Quantil/Automation_TI/quantyoutube.json"
# credentials = service_account.Credentials.from_service_account_file('client_secret_811961685726-rar3clpuboggi40k3va8rb3ao3jl8h44.apps.googleusercontent.com.json')
# #scoped_credentials = credentials.with_scopes(['https://www.googleapis.com/auth/drive.metadata.readonly'])
# youtube = build('youtube', 'v3', credentials=credentials)

# print(type(youtube))

# #print(TEMPLATE_DIR)

import os

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

Path_File_Secret = ""

CLIENT_SECRET_FILE = Path_File_Secret
SCOPES=['https://www.googleapis.com/auth/youtube.force-ssl']

flow=InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
credentials=flow.run_console()
youtube=build('youtube', 'v3', credentials=credentials)

print(youtube)