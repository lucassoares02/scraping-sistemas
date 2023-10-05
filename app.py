from canguru import pegar_dados_canguru
from extrabom import pegar_dados_extrabom
import requests
import json

response = requests.post("https://api-loja.cangurumais.com.br/v1/auth/loja/login", {
    "domain": "cangurumais.com.br",
    "username": "loja",
    "key": "df072f85df9bf7dd71b6811c34bdbaa4f219d98775b56cff9dfa5f8ca1bf8469"
})

response = json.loads(response.text)
token = f"Bearer {response['data']}"

print(token)

for i in range(100):
   pegar_dados_canguru(i, token)
   pegar_dados_extrabom(i)