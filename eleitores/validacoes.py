# Desenvolvido por Carlos Liberato
# Desenvolvido por Bruno Terra
# Desenvolvido por Felipe Miranda
from database.conexao import conectar
import random
import string


def validaTitulo(titulo):
    # Desenvolvido por Carlos Luciano
    """
    validaTitulo(titulo)
    Verifica a autenticidade de um número de Título de Eleitor com base na quantidade de dígitos, código da Unidade Federativa (UF) e cálculo dos dois dígitos verificadores (DV).
    Parâmetros de Entrada (Args):
    titulo (str): Uma string contendo os 12 dígitos do título de eleitor.
    Retorno (Returns):
    bool: Retorna True se o título for válido (os dígitos verificadores calculados batem com os informados) ou False caso contrário.
    """

    if len(titulo) != 12:
        print("--ERRO:  Título inválido, são necessários 12 dígitos.")
        return

    sequencia = titulo[:8]
    uf = titulo[8:10]
    digitoVerificadores = titulo[10:12]

    if int(uf)< 1 or int(uf)> 28:
        return False

    soma1 = 0
    multiplicador = 2
    for i in sequencia:

        soma1 += int(i) * multiplicador
        multiplicador+=1
    
    dv1 = soma1 % 11
    if dv1 == 10:
        dv1 = 0
    elif dv1 == 0 and (uf == '01' or uf == '02'):
        dv1 = 1

    soma2 = (int(uf[0])*7) + (int(uf[1])*8) + (dv1*9)
    dv2 = soma2 % 11
    if dv2 == 10:
        dv2 = 0
    elif dv2 == 0 and (uf == '01' or uf == '02'):
        dv2 = 1

    return digitoVerificadores == f'{dv1}{dv2}'

def validaCPF(cpf):

    if len(cpf) != 11:
        print("--ERRO:  CPF inválido, são necessários 11 dígitos.")
        return

    sequencia = cpf[:9]
    digitoVerificadores = cpf[9:11]
    soma1 = 0
    multiplicador = 10

    for i in sequencia:
        soma1+=int(i) * multiplicador
        multiplicador -= 1
    dv1 =(soma1 * 10) %11
    if dv1 == 10:
        dv1 = 0
        
    soma2 = 0
    multiplicador = 11
    for i in sequencia:
        soma2 +=int(i) * multiplicador
        multiplicador -= 1

    soma2 += dv1 * 2

    dv2 = (soma2 * 10) % 11
    if dv2 == 10:
        dv2 = 0
    return digitoVerificadores == f'{dv1}{dv2}'

