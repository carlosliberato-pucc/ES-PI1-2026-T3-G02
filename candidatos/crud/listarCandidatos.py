#Desenvolvido por Bruno Terra

from database.conexao import conectar
import mysql.connector

def listarCandidatos():
    """
    Lista todos os Candidatos armazenados no banco de dados por ordem alfabética.
    
    Args:
        Nenhum.
    Returns:
        None."""
    

    print("---Lista de Candidatos ---")

    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)


    try:
        cursor.execute("SELECT * FROM candidatos ORDER BY nome_candidato ASC")
        candidatos = cursor.fetchall()
 
        if not candidatos:
            print("Nenhum candidato cadastrado.")
            return



        for candidato in candidatos:
            print(f"N° Eleitoral: {candidato['id_candidato']}")
            print(f"Nome: {candidato['nome_candidato']}")
            print(f"Partido: {candidato['partido']}")
            print("-" * 30)
 
    except Exception as e:
        print(f"\nErro ao listar candidatos: {e}")
 
    finally:
        cursor.close()
        conexao.close()
