from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

CLIENT_SECRETS_FILE = 'client_secret.json'
# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account.
SCOPES = ['https://www.googleapis.com/auth/youtube']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
# Authorize the request and store authorization credentials.

def connect():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    # run.console() malfunctioning
    credentials = flow.run_local_server()
    return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)

def create_yt_playlist(youtube,title):
    playlists_insert_response = youtube.playlists().insert(
        part='snippet,status',
        body={
            'snippet':{
                "title":title,
                "description":"args.description"
            },
            "status":{
                "privacyStatus":'unlisted'
            }
        }
    ).execute()
    # print(playlists_insert_response['id'])
    return playlists_insert_response['id']


if __name__=='__main__':
    youtube=connect()
    # print(create_yt_playlist(youtube,"test0"))
