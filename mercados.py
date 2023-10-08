import requests
import json
from bd import inserir_dados
import json

f = open('data.json')
f1 = open('data_perim.json')
data = json.load(f)
data_perim = json.load(f1)


def pegar_dados_json(i, token, supermercado, loja, filial):

    url = f"https://api-loja.{supermercado}.com.br/v1/loja/produtos/{i}/filial/{filial}/centro_distribuicao/1/detalhes"

    # Enviar uma solicitação GET para obter o conteúdo da página
    response = requests.get(url, headers={'Authorization': token})

    try:
        produto = json.loads(response.text)
        nome_produto = produto["data"]["produto"]["descricao"]
        categoria = for_categories(produto["data"]["produto"]["classificacao_mercadologica_id"], loja)
        preco = produto["data"]["produto"]["preco"]
        print("====================================================")
        print("Nome do produto:", nome_produto)
        print("Categoria:", categoria)
        print("Preço:", preco)
        print("====================================================")
        inserir_dados(nome_produto, categoria, preco, loja)

    except (Exception) as error:
        print(f'Erro: {url}')



def for_categories(id, loja):
    value = data
    if loja == "Perim":
        value = data_perim
    for i in range (len(value)):
        if(value[i]['classificacao_mercadologica_id'] == id):
            return value[i]['descricao']
        