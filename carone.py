import requests
import json
from bd import inserir_dados


def pegar_dados_carone(i):

    url = f"https://www.carone.com.br/api/catalog_system/pub/products/search/?fq=skuId:{i}"

    try:
        response = requests.get(url)
        produto = json.loads(response.text)
        nome_produto = produto[0]["productName"]
        categoria = produto[0]["categories"][0].split("/")[2]
        preco = produto[0]["items"][0]["sellers"][0]["commertialOffer"]["Installments"][0]["Value"]
        print("====================================================")
        print("Nome do produto:", nome_produto)
        print("Categoria:", categoria)
        print("Preço:", preco)
        print("====================================================")
        inserir_dados(nome_produto, categoria, preco, "Carone")

    except (Exception) as error:
        print(f'Erro: {url}')



        