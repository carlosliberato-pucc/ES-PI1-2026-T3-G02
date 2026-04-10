eleitores = []

def verificarCPF(cpf):
    return cpf.isdigit() and len(cpf) ==11


def verificacaoDeDuplicidade(cpf, titulo):
    for eleitor in eleitores:
        if eleitor["cpf"] == cpf and eleitor["titulo"]== titulo:
            return True
    return False


def cadastrarEleitor():

    print('\n::: Cadastro de Eleitor :::\n')
    nome = input("Digite o nome completo do eleitor: ")
    titulo = input("Digite o Título do Eleitor (somente números): ")
    cpf = input("Digite o CPF do Eleitor (somente números): ")#aqui eu tirei o int para o cadastro do CPF, 
    #pois caso iniciasse com 0, esse 0 ia ser apagado
    mesarioQuestion = int(input("O Eleitor é Mesário? (1 - SIM / 0 - NAO): "))

    if not verificarCPF(cpf):
        print("--ERRO:  CPF inválido, são necessários terem 11 dígitos.")
        return
    
    if verificacaoDeDuplicidade(cpf, titulo):
        print("--ERRO: esse cpf e título já foram cadastrados")
        return
    

    mesario = False
    if mesarioQuestion == 1:
        mesario = True

    eleitor = {
        "nome": nome, "titulo": titulo, "cpf": cpf, "mesario": mesario

    }
    eleitores.append(eleitor)
    print("Eleitor cadastrado com sucesso!")


    def listarEleitores():
        print(":::ELEITORES CADASTRADOS:::")
        if len(eleitores) == 0:
            print("Não existem eleitores cadastrados")
            return
        
        for eleitor in eleitores:
            print(f"Nome: {eleitor['nome']}")
            print(f"Título: {eleitor['titulo']}")
            print(f"CPF: {eleitor['cpf']}")
            print(f"Mesário: {eleitor['mesario']}")
            print("-------------------------------------------------------------")
