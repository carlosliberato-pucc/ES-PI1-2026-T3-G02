# Desenvolvido por Carlos Liberato
import eleitores.crud.buscar as buscar
import eleitores.crud.cadastrar as cadastrar
import eleitores.crud.editar as editar
import eleitores.crud.listar as listar
import eleitores.crud.remover as remover
import votacao.votacao as votacao

def menuInicial():
    while True:
        print('\n--- Menu Inicial ---')
        print('[1] Gerenciamento de Eleitores')
        print('[2] Votação')
        print('[0] Fechar')

        opcao = int(input("Digite a opção que deseja: "))
        # redireciona a função de acordo com a opção
        match opcao:
            case 1: 
                menuGerenciamento()
                break
            case 2:
                menuVotacao()
                break
            case 0: 
                return
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

def menuOperarVotacao():
    while True:
        print('\n--- Operar Votação ---')
        print("[1] Votar")
        print("[2] Encerrar Votação")
        # redireciona a função de acordo com a opção
        opcao = int(input("Digite uma opção: "))
        match opcao:
            case 1:
                votacao.abrirVotacao()
                break
            case 2:
                votacao.auditoria()
                break
            case 0:
                menuInicial()
                break
            case _:
                print("ERRO: opção inválidade. Tente novamente")
                break

def menuGerenciamento():
    while True:
        print('\n--- Gerenciamento de Eleitores ---')
        print('[1] Cadastrar Eleitor')
        print('[2] Remover Eleitor')
        print('[3] Editar Dados do Eleitor')
        print('[4] Listar Eleitores')
        print('[5] Buscar Eleitor')
        print('[0] Voltar')

        opcao = int(input("Digite a opção que deseja: "))
        # redireciona a função de acordo com a opção
        match opcao:
            case 1:
                cadastrar.cadastrarEleitor()
                break
            case 2: 
                remover.removerEleitor()
                break
            case 3:
                editar.editarEleitor()
                break
            case 4:
                listar.listarEleitor()
                break
            case 5:
                buscar.buscarEleitor()
                break
            case 0:
                menuInicial()
            case _: 
                print('\nOpção Inválida. Tente Novamente...\n')
