# Desenvolvido por Carlos Liberato
# Desenvolvido por Bruno Terra
# Desenvolvido por Felipe Miranda

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

    '''Desenvolvido por Bruno Terra 
    
    
    validaCPF(cpf)
    Essa função verifica se um CPF é válido ou não usando os dígitos verificadores.

    Parâmetros:
    cpf (str): string com os 11 dígitos do CPF.

    Retorno:
    bool: retorna True se o CPF for válido, ou False se não for.

    Primeiro, a função pega os 9 primeiros dígitos do CPF e separa os 2 últimos, que são os dígitos verificadores.

    Depois, calcula o primeiro dígito verificador (dv1). Para isso, multiplica cada número pelos valores
    de 10 até 2, soma tudo e aplica a conta (soma * 10) % 11. Se o resultado for 10, vira 0.
    Em seguida, calcula o segundo dígito verificador (dv2), parecido com o primeiro,
    mas agora os pesos vão de 11 até 2 e também soma o dv1 multiplicado por 2 no final.

    Por último, compara os dígitos calculados com os que vieram no CPF. Se forem iguais, o CPF é válido.
'''

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

