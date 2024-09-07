from googleapiclient.errors import HttpError
import time

def addsong(youtube,playlistId,videoId):
    try:
        playlists_insert_response = youtube.playlistItems().insert(
            part='snippet',
            body={
                'snippet':{
                    'playlistId':playlistId,
                    "resourceId": {
                        "kind": "youtube#video",
                        "videoId": videoId
                    }
                }
            }
        ).execute()
        print(playlists_insert_response["snippet"]["title"])
    except HttpError as e:
        if e.resp.status == 409:
            print("http error 409")
            print("mainly due to youtube problem...")
            print("try again in 5 seconds")
            time.sleep(5)
            addsong(youtube,playlistId,videoId)
        elif e.resp.status == 403:
            print("http error 403")
            print("youtube api exceed:(")
            print("plz try it next day")
            exit(0)

