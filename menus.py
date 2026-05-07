# Desenvolvido por Carlos Liberato
import eleitores.crud.buscar as buscar
import eleitores.crud.cadastrar as cadastrar
import eleitores.crud.editar as editar
import eleitores.crud.listar as listar
import eleitores.crud.remover as remover
import votacao.votacao as votacao
import votacao.auth as auth
import sys

def menuInicial():
    while True:
        print('\n--- Menu Inicial ---')
        print('[1] Gerenciamento de Eleitores')
        print('[2] Votação')
        print('[0] Fechar')

        opcao = int(input("Digite a opção que deseja: "))
        match opcao:
            case 1:
                menuGerenciamento()  # entra no submenu, ao retornar volta aqui
            case 2:
                menuVotacao()        # idem
            case 0:
                sys.exit()
            case _:
                print('\nOpção Inválida. Tente Novamente...\n')

def menuVotacao():
    if auth.autenticarMesario():
        while True:
            print('\n--- Votação ---')
            print("[1] Abrir sistema de votação")
            print("[2] Auditoria do sistema de votação")
            print("[3] Resultados da votação")
            print("[0] Voltar")

            opcao = int(input("Digite uma opção: "))
            match opcao:
                case 0:
                    return  # volta para menuInicial
                case 1:
                    votacao.abrirVotacao()
                case 2:
                    votacao.auditoria()
                case 3:
                    votacao.resultados()
                case _:
                    print("ERRO: opção inválida. Tente novamente")

def menuOperarVotacao():
    while True:
        print('\n--- Operar Votação ---')
        print("[1] Votar")
        print("[2] Encerrar Votação")
        print("[0] Voltar")

        opcao = int(input("Digite uma opção: "))
        match opcao:
            case 0:
                return  # volta para quem chamou
            case 1:
                votacao.operarVotacao()
            case 2:
                if votacao.encerrarVotacao():
                    return  # votação encerrada, sai do menu
            case _:
                print("ERRO: opção inválida. Tente novamente")

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
        match opcao:
            case 0:
                return  # volta para menuInicial
            case 1:
                cadastrar.cadastrarEleitor()
            case 2:
                remover.removerEleitor()
            case 3:
                editar.editarEleitor()
            case 4:
                listar.listarEleitor()
            case 5:
                buscar.buscarEleitor()
            case _:
                print('\nOpção Inválida. Tente Novamente...\n')