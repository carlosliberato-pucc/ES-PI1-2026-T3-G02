from database.conexao import conectar
import mysql.connector

def listarQntCandidato():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = """
        SELECT n.id_candidato, 
        n.nome_candidato,
        n.cargo,
        COUNT(v.id_voto) AS quantidade
        FROM candidatos n
        LEFT JOIN votos v ON n.id_candidato = v.id_candidato
        GROUP BY n.id_candidato, n.nome_candidato, n.cargo;
    """

    cursor.execute(sql)
    candidatos = cursor.fetchall()

    print("\n::: Histórico de Votos :::\n")
    for candidato in candidatos:
        print(f"Num Eleitoral: {candidato['id_candidato']}")
        print(f"Nome: {candidato['nome_candidato']}")
        print(f"Cargo: {candidato['cargo']}")
        print(f"Qnt de Votos: {candidato['quantidade']}")
        print("-" * 30)

    cursor.close()
    conexao.close()
