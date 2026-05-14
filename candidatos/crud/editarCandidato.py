# Desenvolvido por Bruno Terra


from database.conexao import conectar
import mysql.connector


def editarCandidato() -> None:
    """
    Busca um candidato pelo número de votação e permite a edição de seus dados.
    Mantém os valores atuais caso o usuário deixe o campo em branco.
    Impede a troca para um número já utilizado por outro candidato (RF001.11).

    Args:
        Nenhum.

    Returns:
        None
    """
    print("\n--- Editar Candidato ---")

    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

 
 
    # Busca o candidato pelo número para confirmar que ele existe
    while True:
        numero_str = input("- Digite o número de votação do candidato: ").strip()
        if numero_str.isdigit() and int(numero_str) > 0:
            numero = int(numero_str)
            break
        print("Número inválido. Digite apenas números inteiros positivos.")



  
    cursor.execute("SELECT * FROM candidatos WHERE id_candidato = %s", (numero,))
    candidato = cursor.fetchone()



    if not candidato:
   
        print("Candidato não encontrado.")
        cursor.close()
        conexao.close()
        return

 
    print(f"\nCandidato encontrado: {candidato['nome_candidato']} | Partido: {candidato['partido']}")
    print("Deixe em branco para manter o valor atual.\n")



    # Coleta os novos dados, mantendo os antigos se deixado em branco
   
  
    novo_nome = input(f"Novo nome [{candidato['nome_candidato']}]: ").strip()
    if not novo_nome:
        novo_nome = candidato['nome_candidato']

    novo_partido = input(f"Novo partido [{candidato['partido']}]: ").strip()
    if not novo_partido:
        novo_partido = candidato['partido']

    novo_numero_str = input(f"Novo número de votação [{candidato['id_candidato']}]: ").strip()
    if not novo_numero_str:
        novo_numero = candidato['id_candidato']
    else:
        if not novo_numero_str.isdigit() or int(novo_numero_str) <= 0:
            print("Edição cancelada: número inválido.")
            cursor.close()
            conexao.close()
            return
        novo_numero = int(novo_numero_str)

   
        # verifica se o novo número já está em uso por outro candidato
        if novo_numero != candidato['id_candidato']:
            cursor.execute("SELECT id_candidato FROM candidatos WHERE id_candidato = %s", (novo_numero,))
            if cursor.fetchone():
                print(f"Edição cancelada: o número {novo_numero} já está em uso por outro candidato.")
                cursor.close()
                conexao.close()
                return

 
    # Atualiza no banco de dados
    try:
        sql = """
            UPDATE candidatos
            SET id_candidato = %s, nome_candidato = %s, partido = %s
            WHERE id_candidato = %s
        """
        cursor.execute(sql, (novo_numero, novo_nome, novo_partido, candidato['id_candidato']))
        conexao.commit()
        print("\nCandidato atualizado com sucesso!")

    except mysql.connector.Error as e:
        conexao.rollback()
        print(f"Erro ao atualizar no banco: {e}")

    finally:
        cursor.close()
        conexao.close()