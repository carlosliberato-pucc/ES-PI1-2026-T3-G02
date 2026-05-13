#Desenvolvido por Bruno Terra

from database.conexao import conectar
import mysql.connector

def buscarCandidato():
    """
    Solicita um número de votação pelo terminal e exibe os dados do candidato correspondente.
    
    Args:
        Nenhum
    
    Returns:
        None
    """

    print("\n--- Buscar Candidato ---")

    while True:
        numero_str = input("- Digite o número de votação do candidato: ").strip()
        if numero_str.isdigit() and int(numero_str) > 0:

            numero = int(numero_str)
            break

        else:
            print("Número inválido. Digite apenas números inteiros positivos.")


    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
 
    try:
        cursor.execute("SELECT * FROM candidatos WHERE id_candidato = %s", (numero,))
        candidato = cursor.fetchone()


        if candidato:
            print(f"\nN° Eleitoral: {candidato['id_candidato']}")
            print(f"Nome: {candidato['nome_candidato']}")
            print(f"Partido: {candidato['partido']}")
        else:
            print(f"\nNenhum candidato encontrado com o número {numero}.")
 
    except Exception as e:
        print(f"\nErro ao buscar candidato: {e}")
 
    finally:
        cursor.close()
        conexao.close()


