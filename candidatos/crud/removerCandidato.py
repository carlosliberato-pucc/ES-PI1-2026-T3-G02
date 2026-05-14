#Desenvolvido por Bruno Terra

from database.conexao import conectar
import mysql.connector


def removerCandidato():
    """
    Pede o número do candidato via terminal, e o remove do bancco de dados.
    Exibe os dados do candidato selecionado antes de ocorrer a remoção.
    
    Args:
        Nenhum
    
    Return:
        None
        """
    
    print('-- Remover Candidato ---')

    while True:
        numero_str = input("Digite o número do candidato a ser removido: ").strip()
        if numero_str.isdigit() and int(numero_str) > 0:
            numero = int(numero_str)
            break

        else:
            print("Número inválido, tente novamente apenas com numeros positivos")
        
    
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)


    try:
        cursor.execute("SELECT * FROM candidatos WHERE id_candidato = %s", (numero,))
        candidato = cursor.fetchone()


        if not candidato:
            print(f"Nenhum candidato foi encontrado com o numero {numero}")
            return
        
        
        cursor2 = conexao.cursor()
        cursor2.execute("DELETE FROM candidatos WHERE id_candidato = %s", (numero,))
        conexao.commit()
        print(f"\nCandidato '{candidato['nome_candidato']}' removido com sucesso!")


    except mysql.connector.Error as e:
        conexao.rollback()
        print(f"erro ao remover candidato {e}")

    finally:
        cursor.close()
        conexao.close()




