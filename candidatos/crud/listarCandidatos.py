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
    

    print("===== LISTA DE CANDIDATOS(AS) =====\n")

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

def listarVotosCandidato():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = """
        SELECT n.id_candidato, 
        n.nome_candidato,
        COUNT(v.id_voto) AS quantidade
        FROM candidatos n
        LEFT JOIN votos v ON n.id_candidato = v.id_candidato
        GROUP BY n.id_candidato, n.nome_candidato;
    """

    cursor.execute(sql)
    candidatos = cursor.fetchall()

    print("\n\n::: Histórico de Votos :::\n")
    for candidato in candidatos:
        print(f"{candidato['id_candidato']} - {candidato['nome_candidato']}\nTotal de Votos: {candidato['quantidade']}")
        print("-" * 30)

    cursor.close()
    conexao.close()