from database.conexao import conectar
import mysql.connector

def imprimirCandidato(numero, cargo):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = f"SELECT * FROM candidatos WHERE num_candidato = %s AND cargo = %s;"

    cursor.execute(sql, (numero,cargo))
    candidato = cursor.fetchone()

    if candidato:
        print(f"\nN° Eleitoral: {candidato['num_candidato']}")
        print(f"Nome: {candidato['nome_candidato']}")
        print(f"Partido: {candidato['partido']}")
        print(f"Cargo: {candidato['cargo']}\n")

        return True
    else:
        print(f"\nN° Eleitoral: NULO")
        print(f"Nome: NULO")
        print(f"Partido: NULO")
        print(f"Cargo: NULO\n")

        return False

def listarVotosCandidato():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = """
        SELECT n.num_candidato, 
        n.nome_candidato,
        n.cargo,
        COUNT(v.id_voto) AS quantidade
        FROM candidatos n
        LEFT JOIN votos v ON n.id_candidato = v.id_candidato
        GROUP BY n.id_candidato, n.num_candidato, n.nome_candidato, n.cargo;
    """

    cursor.execute(sql)
    candidatos = cursor.fetchall()

    print("\n::: Histórico de Votos :::\n")
    for candidato in candidatos:
        print(f"{candidato['num_candidato']} - {candidato['nome_candidato']}\nTotal de Votos: {candidato['quantidade']}")
        print("-" * 30)

    cursor.close()
    conexao.close()
