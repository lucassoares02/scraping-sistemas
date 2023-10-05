import mysql.connector

# Configurações do banco de dados MySql
db_config = {
    'host': 'us-cdbr-east-05.cleardb.net',
    'port': '3306',
    'database': 'heroku_e636a57dad82d75',
    'user': 'b4858c0c0cb6ac',
    'password': 'f3aff47f'
}


# Função para inserir dados no banco de dados
def inserir_dados(nome_produto, categoria, preco, supermercado):
    print("** Inserindo no banco!")
    try:
        # Conectar ao banco de dados
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Executar uma consulta SQL para inserir os dados
        cursor.execute("INSERT INTO produto (nome, categoria, preco, supermercado) VALUES (%s, %s, %s, %s)", (nome_produto, categoria, preco, supermercado))

        # Confirmar a transação
        conn.commit()
    except (Exception, mysql.Error) as error:
        print("Erro ao inserir dados no MySql:", error)
    finally:
        # Fechar a conexão com o banco de dados
        if conn:
            cursor.close()
            conn.close()
