#feito por Bruno Terra
#feito por Carlos Liberato
from database.conexao import conectar
import mysql.connector
import eleitores.validacoes as validacoes
import menus
import eleitores.criptoCPF as criptoCPF
import eleitores.chaveAcesso as chaveAcesso
import eleitores
import utils

def removerEleitor():
    """
    remove um eleitor do bando de dados a partir do cpf informado
        O CPF é validado e criptografado antes de ser usado na consulta.
 
    Args:
        Nenhum.
 
    Returns:
        None

"""
    conexao = conectar()
    cursor = conexao.cursor()
  #o cpf é validado usando um módulo existente
    print("===== Remover Eleitor =====\n")
    cpf = input("Insira o CPF do eleitor que deseja remover: ")

    if not validacoes.validaCPF(cpf):
        print("\nO CPF informado é inválido")
        return
    
    #criptografa o cpf antes de ser usado no banco
    cpf_letras = criptoCPF.cpf_para_letras(cpf)
    cpf_cripto = criptoCPF.criptografar_hill(cpf_letras)
    #agora ocorre a verificação se existe
    cursor.execute(
        "SELECT * FROM eleitores WHERE cpf = %s",
        (cpf_cripto,)
    )

    eleitor = cursor.fetchone()
    

    if eleitor is None:
        print("\nEleitor não encontrado")
        
        return
    
    #confirmação da remoção do eleitor
    confirmacao = int(input("\nTem certeza que deseja remover esse eleitor: [1- Sim / 0 - Não]: "))

    if confirmacao == 0:
        print("\nConfirmação cancelada.")
        return
    
    #remove o eleitor

    cursor.execute(
        "DELETE FROM eleitores WHERE cpf = %s",
        (cpf_cripto,)
)
    conexao.commit()

    print("\n")
    utils.pontilhado("Removendo", 5)
    print("\nO Eleitor foi removido com sucesso!\n")
    utils.contagem_regressiva("Limpando em", 3)
    utils.limparTela()

    cursor.close()
    conexao.close()

    