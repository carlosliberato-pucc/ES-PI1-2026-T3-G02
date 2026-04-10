# Desenvolvido por Carlos Liberato
from database.conexao import conectar

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
    pass

def verificacaoDeDuplicidade(documento):
    if len(documento) == 11:
        #cpf
        pass
    elif len(documento) == 12:
        #titulo
        pass
    else:
        print('--erro')
