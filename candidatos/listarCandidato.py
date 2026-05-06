from database.conexao import conectar
import mysql.connector

def buscarCandidatoPorNumero(numero, cargo):
    # Busca um candidato pelo número exibido ou pelo id interno, se disponível.
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    try:
        sql = "SELECT * FROM candidatos WHERE cargo = %s AND (num_candidato = %s OR id_candidato = %s);"
        cursor.execute(sql, (cargo, numero, numero))
    except mysql.connector.Error:
        # Caso o banco não tenha a coluna num_candidato, tenta apenas por id_candidato.
        sql = "SELECT * FROM candidatos WHERE cargo = %s AND id_candidato = %s;"
        cursor.execute(sql, (cargo, numero))

    candidato = cursor.fetchone()
    cursor.close()
    conexao.close()
    return candidato

def imprimirCandidato(numero, cargo):
    candidato = buscarCandidatoPorNumero(numero, cargo)

    if candidato:
        num = candidato.get('num_candidato', candidato.get('id_candidato'))
        print(f"\nN° Eleitoral: {num}")
        print(f"Nome: {candidato['nome_candidato']}")
        print(f"Partido: {candidato['partido']}")
        print(f"Cargo: {candidato['cargo']}\n")

        return candidato
    else:
        print(f"\nN° Eleitoral: NULO")
        print(f"Nome: NULO")
        print(f"Partido: NULO")
        print(f"Cargo: NULO\n")

        return None

def _tem_num_candidato(cursor):
    # Verifica se a coluna num_candidato existe na tabela de candidatos.
    cursor.execute("SHOW COLUMNS FROM candidatos LIKE 'num_candidato';")
    return cursor.fetchone() is not None


def listarVotosCandidato():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    if _tem_num_candidato(cursor):
        sql = """
            SELECT n.num_candidato, 
            n.nome_candidato,
            n.cargo,
            COUNT(v.id_voto) AS quantidade
            FROM candidatos n
            LEFT JOIN votos v ON n.id_candidato = v.id_candidato
            GROUP BY n.id_candidato, n.num_candidato, n.nome_candidato, n.cargo;
        """
    else:
        sql = """
            SELECT n.id_candidato AS num_candidato, 
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
        print(f"{candidato['num_candidato']} - {candidato['nome_candidato']}\nTotal de Votos: {candidato['quantidade']}")
        print("-" * 30)

    cursor.close()
    conexao.close()
