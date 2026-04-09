import  mysql.connector
from mysql.connector import Error

def conectar():
    # função para retornar uma nova conexão com o banco de dados

    try:
        conexao = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "senha",
            database = "ladpy"
        )
        if conexao.is_connected():
            print("Conexão com banco de dados com sucesso (DEPOIS APAGAR)")
            return conexao
    except Error as e:
        print("Erro ao conectar ao banco de dados (DEPOIS APAGAR)")
        return None
    
