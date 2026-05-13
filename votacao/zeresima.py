from database.conexao import conectar
import mysql.connector
import candidatos.crud.listarCandidatos as listarCandidatos

def zeresima():
    
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    print("\n:::::::::::: Zerésima ::::::::::::")
    print("--- Excluíndo Histórico de Votos ---")
    cursor.execute("TRUNCATE TABLE votos;")

    listarCandidatos.listarVotosCandidato()
