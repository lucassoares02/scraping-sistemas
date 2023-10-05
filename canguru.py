import requests
import json
from bd import inserir_dados


def pegar_dados_canguru(i):

    url = f"https://api-loja.cangurumais.com.br/v1/loja/produtos/{i}/filial/2/centro_distribuicao/1/detalhes"

    # Enviar uma solicitação GET para obter o conteúdo da página
    response = requests.get(url, headers={'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJ2aXBjb21tZXJjZSIsImF1ZCI6ImFwaS1hZG1pbiIsInN1YiI6IjZiYzQ4NjdlLWRjYTktMTFlOS04NzQyLTAyMGQ3OTM1OWNhMCIsInZpcGNvbW1lcmNlQ2xpZW50ZUlkIjpudWxsLCJpYXQiOjE2OTY1NDUxNzMsInZlciI6MSwiY2xpZW50IjpudWxsLCJvcGVyYXRvciI6bnVsbCwib3JnIjoiNDMifQ.-FnatdyjfroNGQBJHojBlL5MzU8ozB5uobAW_xIdy5nKziQTkXK18a68Qa0wgOYbhEpPoen7FvXP-j97zVB9rw'})

    try:
        produto = json.loads(response.text)
        nome_produto = produto["data"]["produto"]["descricao"]
        categoria = produto["data"]["produto"]["classificacao_mercadologica_id"]
        preco = produto["data"]["produto"]["preco"]
        print("====================================================")
        print("Nome do produto:", nome_produto)
        print("Categoria:", categoria)
        print("Preço:", preco)
        print("====================================================")
        inserir_dados(nome_produto, categoria, preco, "Canguru")

    except (Exception) as error:
        print(f'Erro: {url}')
        