# Desenvolvido por Carlos Liberato
import eleitores.crud.buscar as buscar
import eleitores.crud.cadastrar as cadastrar
import eleitores.crud.editar as editar
import eleitores.crud.listar as listar
import eleitores.crud.remover as remover
import votacao.votacao as votacao
import votacao.auth as auth
import votacao.auditoria as auditoria
import candidatos.crud.cadastrarCandidato as cadastrarCandidato
import candidatos.crud.editarCandidato as editarCandidato
import sys
from utils import limparTela




def menuInicial():
    while True:
        limparTela()
        print('\n--- Menu Inicial ---')
        print('[1] Gerenciamento')
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


def menuGerenciamento():
    while True:
        limparTela()
        print('\n--- Gerenciamento ---')
        print("[1] Gerenciamento de Eleitores")
        print("[2] Gerenciamento de Candidatos")
        print("[0] Voltar")

        opcao = int(input("Digite uma opção: "))
        match opcao:
            case 0:
                return 
                #volta ao menu inicial
            case 1:
                menuGerenciamentoEleitores()
            case 2:
                menuGerenciamentoCandidatos()
def menuVotacao():
    while True:
        limparTela()
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
                if auth.autenticarMesario():
                    votacao.abrirVotacao()
            case 2:
                menuAuditoria()
            case 3:
                votacao.resultados()
            case _:
                print("ERRO: opção inválida. Tente novamente")

def menuOperarVotacao():
    while True:
        limparTela()
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

def menuGerenciamentoEleitores():
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



def menuGerenciamentoCandidatos():
    while True:
        limparTela()
        print('\n--- Gerenciamento de Candidatos ---')
        print('[1] Cadastrar Candidato')
        print('[2] Editar Candidato')
        print('[0] voltar')
        opcao = int(input("Digite uma opção: "))
        match opcao:
            case 0:
                return
            case 1:
                cadastrarCandidato.cadastrarCandidato()
            case 2:
                editarCandidato.editarCandidato()
            case _:
                print('\nOpção inválida. Tente novamente')


def menuAuditoria():

    while True:


        print('\n--- Auditoria ---')
        print('[1] Exibição de Logs de Ocorrências')
        print('[2] Exibição de Protocolos de Votação')
        print('[0] Voltar')

        opcao = int(input("Digite uma opção: "))
        match opcao:
            case 0:
                return
            case 1:
                auditoria.exibirLogs()
            case 2:
                auditoria.exibirProtocolos()
            case _:
                print("ERRO: opção inválida. Tente novamente")

def menuCandidatos():

    while True:
        
        
        print('\n--- Gerenciamento de Candidatos---')
        print('[1] Cadastrar Candidato')
        print('[0] Voltar')
        
        opcao = int(input("Digite uma opção: "))
        match opcao:
            case 0:
                return
            case 1:
                cadastrarCandidato.cadastrarCandidato()
            case _:
                print("ERRO: opção inválida. Tente novamente")





