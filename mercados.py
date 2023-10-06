import requests
import json
from bd import inserir_dados


def pegar_dados_json(i, token, supermercado, loja, filial):

    url = f"https://api-loja.{supermercado}.com.br/v1/loja/produtos/{i}/filial/{filial}/centro_distribuicao/1/detalhes"

    # Enviar uma solicitação GET para obter o conteúdo da página
    response = requests.get(url, headers={'Authorization': token})

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
        inserir_dados(nome_produto, categoria, preco, loja)

    except (Exception) as error:
        print(f'Erro: {url}')
        