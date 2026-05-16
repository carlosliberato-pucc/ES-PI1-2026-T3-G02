# Desenvolvido por Nicolas Reis
#Desenvolvido por Carlos Liberato
import mysql.connector
from mysql.connector import Error
import sys

# função de conctar com o banco de dados
def conectar():
    """Estabelece uma conexão com o banco de dados MySQL 'ladpy' no localhost.

    Args:
        Nenhum.

    Returns:
        (object) MySQLConnection: Retorna o objeto de conexão ativa caso o acesso seja bem-sucedido.
    """
    try:
        # buscando o banco de dados
        conexao = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "C4rl0s.1",
            database = "ladpy"
        )
        if conexao.is_connected():
            return conexao  
    except Error as e:
        print("--Erro ao conectar ao banco de dados")
        print(e)
        sys.exit()
    
