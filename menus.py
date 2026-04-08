import gerenciamentoEleitores
import gerenciamentoCandidatos
import votacao

def menuInicial():
    while True:
        print('--- Menu Inicial ---')
        print('[1] Gerenciamento')
        print('[2] Votação')
        print('[3] Fechar')

        opcao = int(input("Digite a opção que deseja: "))

        match opcao:
            case 1: 
                menuGerenciamento()
                break
            case 2:
                menuVotacao()
                break
            case 3: 
                return
            case _: 
                print('\nOpção Inválida. Tente Novamente...\n')

def menuGerenciamento():
    while True:
        print('\n--- Gerenciamento ---')
        print('[1] Gerenciar Eleitores')
        print('[2] Gerenciar Candidatos')
        print('[0] Voltar')

        opcao = int(input("Digite a opção que deseja: "))

        match opcao:
            case 1: 
                menuEleitores()
                break
            case 2:
                menuCandidatos()
            case 0:
                print('\n')
                menuInicial()
            case _: 
                print('\nOpção Inválida. Tente Novamente...\n')

def menuVotacao():
    while True:

        print('\n--- Votação ---')
        print("[1] Abrir sistema de votação")
        print("[2] Auditoria do sistema de votação")
        print("[3] Resultados da votação")
        print("[0] Voltar")

        opcao = int(input("Digite uma opção: "))
        if opcao == 0:
            break

        else:
            match opcao:
                case 1:
                    votacao.abrirVotacao()
                    break
                case 2:
                    votacao.auditoria()
                    break
                case 3:
                    votacao.resultados()
                    break
                case 0:
                    print('\n')
                    menuInicial
                case _:
                    print("ERRO: opção inválidade. Tente novamente")

def menuEleitores():
    while True:
        print('\n--- Gerenciamento de Eleitores ---')
        print('[1] Cadastrar Eleitor')
        print('[2] Remover Eleitor')
        print('[3] Editar Dados do Eleitor')
        print('[4] Listar Eleitores')
        print('[0] Voltar')

        opcao = int(input("Digite a opção que deseja: "))

        match opcao:
            case 1:
                gerenciamentoEleitores.cadastrarEleitor()
                break
            case 2: 
                gerenciamentoEleitores.removerEleitor()
                break
            case 3:
                gerenciamentoEleitores.editarEleitor
                break
            case 4:
                gerenciamentoEleitores.listarEleitor()
            case 0:
                print('\n')
                menuGerenciamento()
            case _: 
                print('\nOpção Inválida. Tente Novamente...\n')

def menuCandidatos():
    while True:
        print('\n--- Gerenciamento de Candidatos ---')
        print('[1] Cadastrar Candidatos')
        print('[2] Remover Candidatos')
        print('[3] Editar Dados do Candidatos')
        print('[4] Listar Candidatos')
        print('[0] Voltar')

        opcao = int(input("Digite a opção que deseja: "))

        match opcao:
            case 1:
                gerenciamentoCandidatos.cadastrarCandidato()
                break
            case 2: 
                gerenciamentoCandidatos.removerCandidato()
                break
            case 3:
                gerenciamentoCandidatos.editarCandidato
                break
            case 4:
                gerenciamentoCandidatos.listarCandidatos()
            case 0:
                print('\n')
                menuGerenciamento()
            case _: 
                print('\nOpção Inválida. Tente Novamente...\n')