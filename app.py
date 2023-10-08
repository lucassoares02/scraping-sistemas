from mercados import pegar_dados_json
from extrabom import pegar_dados_extrabom
from carone import pegar_dados_carone
from auth import get_token



token_canguru = get_token("https://api-loja.cangurumais.com.br/v1/auth/loja/login", "cangurumais.com.br")
token_perim = get_token("https://api-loja.perim.com.br/v1/auth/loja/login", "perim.com.br")

for i in range(10000):
   pegar_dados_json(i, token_canguru, "cangurumais", "Canguru", 2)
   pegar_dados_json(i, token_perim, "perim", "Perim", 1)
   pegar_dados_extrabom(i)
   pegar_dados_carone(i)