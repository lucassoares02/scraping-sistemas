import requests
import json

def get_token(url, domain):
    response = requests.post(url, {
    "domain": domain,
    "username": "loja",
    "key": "df072f85df9bf7dd71b6811c34bdbaa4f219d98775b56cff9dfa5f8ca1bf8469"
    })  

    response = json.loads(response.text)
    return f"Bearer {response['data']}"