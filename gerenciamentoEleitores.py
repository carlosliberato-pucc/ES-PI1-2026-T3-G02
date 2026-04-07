def cadastrarEleitor():

    print('\n::: Cadastro de Eleitor :::\n')
    nome = input("Digite o nome completo do eleitor: ")
    titulo = input("Digite o Título do Eleitor (somente números): ")
    cpf = int(input("Digite o CPF do Eleitor (somente números): "))
    mesarioQuestion = int(input("O Eleitor é Mesário? (1 - SIM / 0 - NAO): "))

    mesario = False
    if mesarioQuestion == 1:
        mesario = True


def verificarCPF():
    pass

def verificaDuplicidade():
    pass

def removerEleitor():
    pass

def editarEleitor():
    pass

def listarEleitor():
    pass