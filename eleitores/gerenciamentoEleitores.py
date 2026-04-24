# Desenvolvido por Carlos Liberato
# Desenvolvido por Bruno Terra
# Desenvolvido por Felipe Miranda
# Desenvolvido por Gabriel Coutinho
# Desenvolvido pr Nicolas Reis
from database.conexao import conectar
import mysql.connector
from . import validacoes
import eleitores.criptoCPF as criptoCPF
import eleitores.chaveAcesso as chaveAcesso
import eleitores.criptoChaveAcesso as criptoChaveAcesso

def cadastrarEleitor():

    """
    cadastrarEleitor()
    Parâmetros de Entrada (Args):
    Nenhum (void). A função é interativa e obtém os dados diretamente via input().
    Retorno (Returns):
    None. A função encerra sua execução após o sucesso da transação ou ao encontrar uma falha de validação (usando return antecipado).
    """

    conexao = conectar()
    cursor = conexao.cursor() # variavel para gerar funções do mysql

    print('\n::: Cadastro de Eleitor :::\n')
    nome = input("- Digite o nome completo: ")
    cpf = input("- Digite o CPF (somente números): ")
    titulo = input("- Digite o Título de Eleitor (somente números): ")

    mesarioQuestion = int(input("- O Eleitor é Mesário? (1 - SIM / 0 - NAO): "))
    perfil = 'eleitor'
    
    if mesarioQuestion == 0:
        perfil = 'eleitor'
    elif mesarioQuestion == 1:
        perfil = 'mesario'
    else:
        print('--Erro: valor inválido\n')

    flag_voto = False

    # chamando função de validação
    if not validacoes.validaTitulo(titulo):
        print("Cadastro cancelado: Título Inválido.")
        return
    
    # validação do cpf
    if not validacoes.validaCPF(cpf):
        print("Cadastro cancelado: CPF Inválido.")
        return

    # validação do cpf
    cpf_convertido = criptoCPF.cpf_para_letras(cpf)
    cpf_criptografado = criptoCPF.criptografar_hill(cpf_convertido)
    
    #chave de acesso
    chave_acesso = chaveAcesso.gerarChaveAcesso(nome)
    chave_acesso_cripto = criptoChaveAcesso.criptografar_hill(chave_acesso)
    print(f"Chave de acesso criada: {chave_acesso}")

    # insercao com o banco de dados
    try:
        sql = """
            INSERT INTO eleitores 
            (nome_eleitor, cpf, titulo_eleitor, perfil, chave_acesso, flag_voto) 
            VALUES (%s, %s, %s, %s, %s, %s)
            """
        cursor.execute(sql, (nome,cpf_criptografado,titulo,perfil,chave_acesso_cripto,flag_voto))
        conexao.commit()
        print("Dados Cadastrados com Sucesso!")

    except mysql.connector.Error as e:
        conexao.rollback()
        print(f"Erro ao inserir no banco: {e}")
    
    cursor.close()
    conexao.close()

def buscarEleitor():
    # Conecta ao banco de dados e cria um cursor que retorna resultados como dicionário
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    # Exibe o menu de opções para escolher o tipo de busca
    print("\n::: Buscar Eleitor :::\n")
    print("[1] Buscar por CPF")
    print("[2] Buscar por Título de Eleitor")
    print("[3] Buscar por Nome")

    # Loop para garantir que a opção seja um número inteiro válido
    while True:
        try:
            opcao = int(input("Digite a opção desejada: "))
            break
        except ValueError:
            print("\nERRO: digite apenas números. Tente novamente.\n")
    
    # Busca por CPF
    if opcao == 1:
        cpf = input("Digite o CPF (somente números): ").strip()
        if not validacoes.validaCPF(cpf):
            print("Busca cancelada: CPF inválido.")
            cursor.close()
            conexao.close()
            return
        
        # Converte o CPF para letras e criptografa usando a mesma lógica de armazenamento
        cpf_convertido = criptoCPF.cpf_para_letras(cpf)
        cpf_criptografado = criptoCPF.criptografar_hill(cpf_convertido)
        sql = '''
            SELECT id_eleitor, nome_eleitor, cpf, titulo_eleitor, perfil, chave_acesso, flag_voto
            FROM eleitores
            WHERE cpf = %s
        '''
        params = (cpf_criptografado,)

    # Busca por Título de Eleitor
    elif opcao == 2:
        titulo = input("Digite o Título De Eleitor (somente números): ").strip()
        if not validacoes.validaTitulo(titulo):
            print("Busca cancelada: Título inválido.")
            cursor.close()
            conexao.close()
            return
        
        sql = '''
            SELECT id_eleitor, nome_eleitor, cpf, titulo_eleitor, perfil, chave_acesso, flag_voto
            FROM eleitores
            WHERE titulo_eleitor = %s
        '''
        params = (titulo,)

    # Busca por Nome
    elif opcao == 3:
        nome = input("Digite o nome completo ou parte do nome: ").strip()
        if not nome:
            print("Busca cancelada: Nome inválido.")
            cursor.close()
            conexao.close()
            return
        
        # Usa LIKE para permitir busca por partes do nome
        sql = '''
            SELECT id_eleitor, nome_eleitor, cpf, titulo_eleitor, perfil, chave_acesso, flag_voto
            FROM eleitores
            WHERE nome_eleitor LIKE %s
        '''
        params = (f'%{nome}%',)

    # Opção inválida
    else:
        print("Opção de busca inválida.")
        cursor.close()
        conexao.close()
        return
    
    # Executa a consulta e salva os registros encontrados
    cursor.execute(sql, params)
    registros = cursor.fetchall()

    if not registros:
        print("\nNenhum eleitor encontrado.")
    else:
        print("\nResultados da busca: ")
        for eleitor in registros:
            # Descriptografa CPF e chave de acesso antes de mostrar
            cpf_decodificado = criptoCPF.letras_para_cpf(criptoCPF.descriptografar_hill(eleitor['cpf']))
            chave_acesso_decodificada = criptoChaveAcesso.descriptografar_hill(eleitor['chave_acesso'])
            print(f"\nID: {eleitor['id_eleitor']}")
            print(f"Nome: {eleitor['nome_eleitor']}")
            print(f"CPF: {cpf_decodificado}")
            print(f"Título: {eleitor['titulo_eleitor']}")
            print(f"Perfil: {eleitor['perfil']}")
            print(f"Chave de Acesso: {chave_acesso_decodificada}")
            print(f"Votou: {'Sim' if eleitor['flag_voto'] else 'Não'}")
    
    # Fecha cursor e conexão ao final da função
    cursor.close()
    conexao.close()


def editarEleitor():
    print("\n===== EDITAR ELEITOR =====\n")
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    # Busca o eleitor pelo CPF para confirmar que ele existe
    cpf = input("Digite o CPF do eleitor que deseja editar (somente números): ").strip()
    if not validacoes.validaCPF(cpf):
        print("Edição cancelada: CPF inválido.")
        cursor.close()
        conexao.close()
        return

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