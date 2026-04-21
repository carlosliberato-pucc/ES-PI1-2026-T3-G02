# Desenvolvido por Carlos Liberato
# Desenvolvido por Bruno Terra
from database.conexao import conectar
import random
import string


def verificaTitulo(titulo):
    sequencia = titulo[:8] # atribui a variavel os 8 primeiros digitos do titulo
    uf = titulo[8:10] # atribui a variavel os digitos das posições9 e 10 do titulo
    digitoVerificadores = titulo[10:12] # atribui a variavel os ultimos dois digitos

    if int(uf)< 1 or int(uf)> 28:
        return False

    soma1 = 0
    multiplicador = 2
    for i in sequencia:
        # soma com o digito e multiplica na iteração e incrementa +1 na variavel multiplicadora

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

def verificaCPF(cpf):
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

def verificacaoDeDuplicidade(documento):
    if len(documento) == 11:
        #cpf
        pass
    elif len(documento) == 12:
        #titulo
        pass
    else:
        print('--erro')

def gerarChaveAcesso(nome):
    # Gera a chave de acesso do eleitor baseada no nome fornecido.

    partes = nome.strip().upper().split()

    primeiras_duas = partes[0][:2] # Pega as duas primeiras letras do primeiro nome

    if len(partes) >= 2:
        primeira_segunda = partes[1][0] # Caso normal: pega a 1ª letra do segundo nome
    
    else:
        # Caso o eleitor tenha apenas um nome: usa a 3ª letra do nome,
        # ou 'X' se o nome tiver menos de 3 caracteres

        primeira_segunda = partes[0][2] if len(partes[0]) > 2 else 'X'  

    digitos = ''.join(random.choices(string.digits, k=4)) # Gera 4 dígitos numéricos aleatórios para garantir unicidade da chave

    return primeiras_duas + primeira_segunda + digitos