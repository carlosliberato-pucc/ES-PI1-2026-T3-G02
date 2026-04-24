# Desenvolvido por Nicolas Reis
import mysql.connector
from mysql.connector import Error
import sys

# função de conctar com o banco de dados
def conectar():
    try:
        # buscando o banco de dados
        conexao = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "Nicolas2020",
            database = "ladpy"
        )
        if conexao.is_connected():
            return conexao  
    except Error as e:
        print("--Erro ao conectar ao banco de dados")
        sys.exit()
    
