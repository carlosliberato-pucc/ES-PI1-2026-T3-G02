import random
import datetime 
import  mysql.connector


def conectar():
    # função para retornar uma nova conexão com o banco de dados

    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "sua_senha",
        database = "nome_banco"
    )