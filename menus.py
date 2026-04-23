# Desenvolvido por Carlos Liberato
import eleitores.gerenciamentoEleitores as eleitores
import candidatos.gerenciamentoCandidatos as candidatos
import votacao

def menuInicial():
    while True:
        print('\n--- Menu Inicial ---')
        print('[1] Gerenciamento')
        print('[2] Votação')
        print('[3] Fechar')

        opcao = int(input("Digite a opção que deseja: "))
        # redireciona a função de acordo com a opção
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
        # redireciona a função de acordo com a opção
        match opcao:
            case 1: 
                menuEleitores()
                break
            case 2:
                menuCandidatos()
            case 0:
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
        # redireciona a função de acordo com a opção
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
                    menuInicial()
                    break
                case _:
                    print("ERRO: opção inválidade. Tente novamente")
                    break

def menuEleitores():
    while True:
        print('\n--- Gerenciamento de Eleitores ---')
        print('[1] Cadastrar Eleitor')
        print('[2] Remover Eleitor')
        print('[3] Editar Dados do Eleitor')
        print('[4] Listar Eleitores')
        print('[0] Voltar')

        opcao = int(input("Digite a opção que deseja: "))
        # redireciona a função de acordo com a opção
        match opcao:
            case 1:
                eleitores.cadastrarEleitor()
                break
            case 2: 
                # eleitores.removerEleitor()
                break
            case 3:
                # eleitores.editarEleitor
                break
            case 4:
                # eleitores.listarEleitor()
                break
            case 0:
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
        print('[5] Buscar Eleitor')
        print('[0] Voltar')

        opcao = int(input("Digite a opção que deseja: "))
        # redireciona a função de acordo com a opção
        match opcao:
            case 1:
                candidatos.cadastrarCandidato()
                break
            case 2: 
                candidatos.removerCandidato()
                break
            case 3:
                candidatos.editarCandidato()
                break
            case 4:
                candidatos.listarCandidatos()
                break
            case 5:
                eleitores.buscarEleitor()
                break
            case 0:
                menuGerenciamento()
                break
            case _: 
                print('\nOpção Inválida. Tente Novamente...\n')