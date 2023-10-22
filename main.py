from http import HTTPStatus
import json
from dotenv import load_dotenv
import os
import base64
from requests import post, get
import requests

load_dotenv()

client_id = os.getenv("clientID")
client_secret = os.getenv("clientSecret")

def get_token():
    authStr = client_id + ":" + client_secret
    authBytes = authStr.encode("utf-8")
    authBase64 = str(base64.b64encode(authBytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + authBase64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return{"Authorization": "Bearer " + token}

#create playlist for chapter
def create_playlist(name, public=False):
    response = requests.post(
        url = f"https://api.spotify.com/v1/users/{client_id}/playlists",
        headers = get_auth_header(token),
        json = {
            "name": name,
            "public": public
        }
    )
    json_resp = response.json()

    return json_resp

#get songs that match the guidelines

#put those songs in the playlist


#testing playlist
token = get_token()
playlist_test = create_playlist("test1")
print(playlist_test)
