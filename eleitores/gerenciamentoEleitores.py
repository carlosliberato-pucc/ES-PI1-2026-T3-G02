# Desenvolvido por Carlos Liberato
# Desenvolvido por Bruno Terra
# Desenvolvido por Felipe Miranda
# Desenvolvido por Gabriel Coutinho
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
    """
    buscarEleitor()
    Permite buscar um eleitor no banco de dados por CPF, Título de Eleitor ou Nome.
    A busca por CPF e Título utiliza criptografia para proteger os dados sensíveis.
    Parâmetros de Entrada (Args):
    Nenhum (void). A função é interativa e obtém os dados diretamente via input().
    Retorno (Returns):
    None. Exibe os resultados da busca ou mensagens de erro.
    """

    # Conecta ao banco de dados e cria cursor com retorno em dicionário para facilitar acesso aos dados
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    # Exibe o menu de opções de busca
    print("\n::: Buscar Eleitor :::\n")
    print("[1] Buscar por CPF")
    print("[2] Buscar por Título de Eleitor")
    print("[3] Buscar por Nome")

    # Loop para validar entrada numérica da opção
    while True:
        try:
            opcao = int(input("Digite a opção desejada: "))
            break
        except ValueError:
            print("\nERRO: digite apenas números. Tente novamente.\n")
    
    # Opção 1: Busca por CPF
    if opcao == 1:
        # Solicita e valida o CPF digitado
        cpf = input("Digite o CPF (somente números): ").strip()
        if not validacoes.validaCPF(cpf):
            print("Busca cancelada: CPF inválido.")
            cursor.close()
            conexao.close()
            return
        
        # Converte CPF para letras e criptografa usando Cifra de Hill (para buscar no banco criptografado)
        cpf_convertido = criptoCPF.cpf_para_letras(cpf)
        cpf_criptografado = criptoCPF.criptografar_hill(cpf_convertido)
        
        # Prepara a query SQL para buscar eleitor pelo CPF criptografado
        sql = '''
            SELECT id_eleitor, nome_eleitor, cpf, titulo_eleitor, perfil, chave_acesso, flag_voto
            FROM eleitores
            WHERE cpf = %s
        '''
        params = (cpf_criptografado,)