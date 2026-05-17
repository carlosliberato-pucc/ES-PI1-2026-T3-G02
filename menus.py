# Desenvolvido por Carlos Liberato
import eleitores.crud.buscar as buscar
import eleitores.crud.cadastrar as cadastrar
import eleitores.crud.editar as editar
import eleitores.crud.listar as listar
import eleitores.crud.remover as remover
import votacao.votacao as votacao
import votacao.auth as auth
from votacao.auditoria import exibirLogs, exibirProtocolos
import votacao.resultados as resultados
import candidatos.crud.cadastrarCandidato as cadastrarCandidato
import candidatos.crud.removerCandidato as removerCandidato
import candidatos.crud.editarCandidato as editarCandidato
import candidatos.crud.listarCandidatos as listarCandidatos
import candidatos.crud.buscarCandidato as buscarCandidato
import sys
from utils import limparTela
import utils

def menuInicial():
    """Exibe e gerencia o menu principal do sistema de votação digital.

    Args:
        Nenhum.

    Returns:
        Nenhum.
    """
    while True:
        limparTela()
        print("====== LAD.py - Sistema de Votação Digital ======")
        print('\n===== Menu Inicial =====')
        print('[1] Gerenciamento')
        print('[2] Votação')
        print('[0] Fechar')
        opcao = int(input("Digite a opção que deseja: "))
        limparTela()
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
    """Exibe e gerencia as opções do menu de gerenciamento do sistema.

    Args:
        Nenhum.

    Returns:
        Nenhum.
    """
    while True:
        print('\n===== Gerenciamento =====')
        print("[1] Gerenciamento de Eleitores")
        print("[2] Gerenciamento de Candidatos")
        print("[0] Voltar")
        opcao = int(input("Digite uma opção: "))
        limparTela()
        match opcao:
            case 0:
                return 
                #volta ao menu inicial
            case 1:
                menuGerenciamentoEleitores()
            case 2:
                menuGerenciamentoCandidatos()
        
def menuVotacao():
    """Exibe e gerencia as opções do menu de controle de votação.

    Args:
        Nenhum.

    Returns:
        Nenhum.
    """
    while True:
        print('\n===== Votação =====')
        print("[1] Abrir sistema de votação")
        print("[2] Auditoria do sistema de votação")
        print("[3] Resultados da votação")
        print("[0] Voltar")
        opcao = int(input("Digite uma opção: "))
        limparTela()
        match opcao:
            case 0:
                return  # volta para menuInicial
            case 1:
                if auth.autenticarMesario():
                    utils.contagem_regressiva("Iniciando em", 3)
                    limparTela()
                    votacao.abrirVotacao()
            case 2:
                menuAuditoria()
            case 3:
                resultados.resultados()
            case _:
                print("ERRO: opção inválida. Tente novamente")

def menuOperarVotacao():
    """Exibe e gerencia as ações práticas da operação de uma votação em andamento.

    Args:
        Nenhum.

    Returns:
        Nenhum.
    """
    while True:
        print('\n===== Operar Votação =====')
        print("[1] Votar")
        print("[2] Encerrar Votação")
        print("[0] Voltar")
        opcao = int(input("Digite uma opção: "))
        limparTela()
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
    """Exibe e gerencia o menu de CRUD para o controle de eleitores.

    Args:
        Nenhum.

    Returns:
        Nenhum.
    """
    while True:
        print('\n===== Gerenciamento de Eleitores =====')
        print('[1] Cadastrar Eleitor')
        print('[2] Remover Eleitor')
        print('[3] Editar Dados do Eleitor')
        print('[4] Listar Eleitores')
        print('[5] Buscar Eleitor')
        print('[0] Voltar')
        opcao = int(input("Digite a opção que deseja: "))
        limparTela()
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
    """Exibe e gerencia o menu de CRUD para o controle de candidatos.

    Args:
        Nenhum.

    Returns:
        Nenhum.
    """
    while True:
        print('\n===== Gerenciamento de Candidatos =====')
        print('[1] Cadastrar Candidato')
        print('[2] Remover Candidato')
        print('[3] Editar Candidato')
        print('[4] Listar Candidatos')
        print('[5] Buscar Candidato')
        print('[0] Voltar')
        opcao = int(input("Digite uma opção: "))
        limparTela()
        match opcao:
            case 0:
                return
            case 1:
                cadastrarCandidato.cadastrarCandidato()
            case 2:
                removerCandidato.removerCandidato()
            case 3:
                editarCandidato.editarCandidato()
            case 4:
                listarCandidatos.listarCandidatos()
            case 5:
                buscarCandidato.buscarCandidato()

            case _:
                print('\nOpção inválida. Tente novamente')


def menuAuditoria():
    """Exibe e gerencia as ferramentas de auditoria e logs do sistema.

    Args:
        Nenhum.

    Returns:
        Nenhum.
    """
    while True:
        print('\n===== Auditoria =====')
        print('[1] Exibição de Logs de Ocorrências')
        print('[2] Exibição de Protocolos de Votação')
        print('[0] Voltar')

        opcao = int(input("Digite uma opção: "))
        match opcao:
            case 0:
                return
            case 1:
                exibirLogs()
            case 2:
                exibirProtocolos()
            case _:
                print("ERRO: opção inválida. Tente novamente")

