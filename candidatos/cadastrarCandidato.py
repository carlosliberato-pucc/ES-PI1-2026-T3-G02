# Desenvolvido por Bruno Terra
from database.conexao import conectar
import mysql.connector


def cadastrarCandidato() -> None:
    """
    Solicita os dados de um novo candidato via terminal e o registra no banco de dados.
    O número de votação é usado como identificador único (id_candidato).
    Número duplicado é impedido pelo banco (chave primária) e tratado com mensagem clara.

    Args:
        Nenhum.

    Returns:
        None
    """
    print("\n--- Cadastrar Candidato ---")

    nome = input("Nome do candidato: ").strip()
    partido = input("Partido: ").strip()

    while True:
        numero_str = input("Número de votação: ").strip()
        if numero_str.isdigit() and int(numero_str) > 0:
            numero = int(numero_str)
            break
        print("Número inválido. Digite apenas números inteiros positivos.")

    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            "INSERT INTO candidatos (id_candidato, nome_candidato, partido) VALUES (%s, %s, %s)",
            (numero, nome, partido)
        )
        conexao.commit()
        print(f"\nCandidato '{nome}' cadastrado com sucesso! Número de votação: {numero}")

    except mysql.connector.errors.IntegrityError:
        print(f"\nErro: o número {numero} já está em uso por outro candidato. Cadastro cancelado.")

    except Exception as e:
        print(f"\nErro inesperado ao cadastrar candidato: {e}")

    finally:
        cursor.close()
        conexao.close()