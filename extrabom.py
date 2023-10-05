from bs4 import BeautifulSoup
import requests
from bd import inserir_dados



def pegar_dados_extrabom(i):
     # URL da página que você deseja fazer scraping
    url = f'https://www.extrabom.com.br/p/unknow/{i}'

    # Enviar uma solicitação GET para obter o conteúdo da página
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)



    try:
        # Verificar se a solicitação foi bem-sucedida
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extrair Nome do produto
            nome_produto = soup.find('h1', class_='nome-produto').text.strip()

            # Extrair Categoria
            breadcrumbs = soup.find('div', class_='breadcrumb breadcrumb-section').find_all('a')
            categoria = breadcrumbs[-1].text.strip()

            # Extrair partes do preço
            preco_reais = soup.find('span', class_='rs').text.strip()
            preco_decimais = soup.find('span', class_='dec').text.strip()
            preco_centavos = soup.find('span', class_='cent').text.strip()

            # Juntar as partes do preço em uma única string
            preco = f"{preco_reais}{preco_decimais}{preco_centavos}"

            # Imprimir os resultados
            print("====================================================")
            print("Nome do produto:", nome_produto)
            print("Categoria:", categoria)
            print("Preço:", preco.replace("R$", "").replace(",", "."))
            print("====================================================")

            inserir_dados(nome_produto.capitalize(), categoria.capitalize(), preco.replace("R$", "").replace(",", "."), "Extrabom")

        else:
            print("Falha ao acessar a página:", response.status_code)
    except (Exception) as error:
        print(f"Url Inválida: {url}")