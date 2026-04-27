#Desenvolvido por Nicolas Reis

from database.conexao import conectar
import mysql.connector
import eleitores.validacoes as validacoes
import menus
import eleitores.criptoCPF as criptoCPF
import eleitores.chaveAcesso as chaveAcesso
import eleitores

def editarEleitor():
    print("\n===== EDITAR ELEITOR =====\n")
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    # Busca o eleitor pelo CPF para confirmar que ele existe
    cpf = input("- Digite o CPF (somente números): ")
    while not validacoes.validaCPF(cpf):
        # validação do cpf
        if not validacoes.validaCPF(cpf):
            print("--Erro: CPF Inválido. Tente Novamente...\n")
            cpf = input("- Digite o CPF (somente números): ")

    # Criptografa o CPF para buscar no banco
    cpf_convertido = criptoCPF.cpf_para_letras(cpf)
    cpf_criptografado = criptoCPF.criptografar_hill(cpf_convertido)

    cursor.execute("SELECT * FROM eleitores WHERE cpf = %s", (cpf_criptografado,))
    eleitor = cursor.fetchone()

    if not eleitor:
        print("Eleitor não encontrado.")
        cursor.close()
        conexao.close()
        return

    print(f"\nEleitor encontrado: {eleitor['nome_eleitor']}")
    print("Deixe em branco para manter o valor atual.\n")

    # Coleta os novos dados, mantendo os antigos se deixado em branco
    novo_nome = input(f"Novo nome [{eleitor['nome_eleitor']}]: ").strip()
    if not novo_nome:
        novo_nome = eleitor['nome_eleitor']

    novo_cpf = input(f"Novo CPF (somente números): ").strip()
    if not novo_cpf:
        novo_cpf_criptografado = cpf_criptografado  # mantém o atual
    else:
        if not validacoes.validaCPF(novo_cpf):
            print("Edição cancelada: Novo CPF inválido.")
            cursor.close()
            conexao.close()
            return
        novo_cpf_convertido = criptoCPF.cpf_para_letras(novo_cpf)
        novo_cpf_criptografado = criptoCPF.criptografar_hill(novo_cpf_convertido)

    novo_titulo = input(f"Novo Título de Eleitor [{eleitor['titulo_eleitor']}]: ").strip()
    if not novo_titulo:
        novo_titulo = eleitor['titulo_eleitor']
    else:
        if not validacoes.validaTitulo(novo_titulo):
            print("Edição cancelada: Novo Título inválido.")
            cursor.close()
            conexao.close()
            return

    mesarioQuestion = input(f"É Mesário? (1 - SIM / 0 - NAO) [{eleitor['perfil']}]: ").strip()
    if not mesarioQuestion:
        novo_perfil = eleitor['perfil']
    elif mesarioQuestion == '1':
        novo_perfil = 'mesario'
    elif mesarioQuestion == '0':
        novo_perfil = 'eleitor'
    else:
        print("Edição cancelada: valor inválido para perfil.")
        cursor.close()
        conexao.close()
        return

    # Atualiza no banco de dados
    try:
        sql = """
            UPDATE eleitores
            SET nome_eleitor = %s, cpf = %s, titulo_eleitor = %s, perfil = %s
            WHERE id_eleitor = %s
        """
        cursor.execute(sql, (novo_nome, novo_cpf_criptografado, novo_titulo, novo_perfil, eleitor['id_eleitor']))
        conexao.commit()
        print("\nEleitor atualizado com sucesso!")

    except mysql.connector.Error as e:
        conexao.rollback()
        print(f"Erro ao atualizar no banco: {e}")

    cursor.close()
    conexao.close()

    menus.menuGerenciamento()
