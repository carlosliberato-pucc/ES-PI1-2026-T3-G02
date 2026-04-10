# Desenvolvido por Carlos Liberato
# Desenvolvido por Bruno Terra
from database.conexao import conectar
from . import validacoes

def cadastrarEleitor():
    conexao = conectar()
    cursor = conexao.cursor() # variavel para gerar funções do mysql

    print('\n::: Cadastro de Eleitor :::\n')
    nome = input("- Digite o nome completo: ")
    cpf = input("- Digite o CPF (somente números): ")
    titulo = input("- Digite o Título de Eleitor (somente números): ")

    mesarioQuestion = int(input("- O Eleitor é Mesário? (1 - SIM / 0 - NAO): "))
    perfil = 'eleitor'

    flag_voto = False

    if mesarioQuestion == 0:
        perfil = 'eleitor'
    elif mesarioQuestion == 1:
        perfil = 'mesario'
    else:
        print('--Erro: valor inválido\n')

    # chamando função de validação
    if len(titulo) != 12:
        print("--ERRO:  Título inválido, são necessários 12 dígitos.")
    elif validacoes.verificaTitulo(titulo):
        print("VALIDO")
        # chamar função de criptografia
    else:
        print('INVALIDO')
    
    if validacoes.verificacaoDeDuplicidade(cpf):
        print("--ERRO: esse cpf já foi cadastrados")
        return
    if validacoes.verificacaoDeDuplicidade(titulo):
        print("--ERRO: esse titulo já foi cadastrados")
        return
    

