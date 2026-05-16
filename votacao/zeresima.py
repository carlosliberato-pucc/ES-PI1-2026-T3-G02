from database.conexao import conectar
import mysql.connector
import candidatos.crud.listarCandidatos as listarCandidatos
import utils
def zeresima():
    
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    print("\n:::::::::::: Zerésima ::::::::::::\n")
    utils.pontilhado("Excluindo Votos", 3)
    cursor.execute("TRUNCATE TABLE votos;")

    listarCandidatos.listarVotosCandidato()
