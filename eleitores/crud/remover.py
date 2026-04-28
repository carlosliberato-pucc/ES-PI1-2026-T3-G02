#feito por Bruno Terra
#feito por Carlos Liberato
from database.conexao import conectar
import mysql.connector
import eleitores.validacoes as validacoes
import menus
import eleitores.criptoCPF as criptoCPF
import eleitores.chaveAcesso as chaveAcesso
import eleitores

def removerEleitor():
    #remove um eleitor do bando de dados a partir do cpf informado

    conexao = conectar()
    cursor = conexao.cursor()
  #o cpf é validado usando um módulo existente
    cpf = input("Insira o CPF do eleitor que deseja remover: ")

    if not validacoes.validaCPF(cpf):
        print("O CPF informado é inválido")

        menus.menuGerenciamento()
        return
    
    #criptografa o cpf antes de ser usado no banco
    cpf_cripto = criptoCPF.criptoCPF(cpf)

    #agora ocorre a verificação se existe
    cursor.execute("SELECT  * FROM eleitores WHERE cpf = %s", cpf(cpf_cripto,))
    eleitor = cursor.fetchone()

    if eleitor is None:

        print("Eleitor não encontrado")
        menus.menuGerenciamento()
        return
    
    #confirmação da remoção do eleitor
    confirmacao = input("Tem certeza que deseja remover esse eleitor: (s/n)")

    if confirmacao.lower != 's':
        print("Confirmação cancelada")
        menus.menuGerenciamento()
        return
    
    #remove o eleitor

    cursor.execute("DELETE FROM eleitores WHERE CPF = %s", cpf_cripto)
    conexao.commit()


    print("Eleitor foi removido com sucesso")

    cursor.close()

    conexao.close()

    menus.menuGerenciamento()