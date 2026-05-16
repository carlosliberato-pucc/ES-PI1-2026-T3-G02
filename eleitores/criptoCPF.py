
# MATRIZ CHAVE
CHAVE = [[3, 3],
         [2, 5]]

# MATRIZ INVERSA (já calculada mod 26)
CHAVE_INV = [[15, 17],
             [20, 9]]


def texto_para_numeros(texto):
    """
    Converte letras para números (A=0, B=1, ..., Z=25).
 
    Args:
        texto (str): Texto composto apenas por letras maiúsculas.
 
    Returns:
        list: Lista de inteiros representando cada letra.
    """

    return [ord(c) - 65 for c in texto]


def numeros_para_texto(numeros):
    """
    Converte uma lista de números de volta para letras maiúsculas.
 
    Args:
        numeros (list): Lista de inteiros entre 0 e 25.
 
    Returns:
        str: Texto formado pelas letras correspondentes.
    """
    return ''.join([chr(n + 65) for n in numeros])


def preparar_texto(texto):
    """
    Garante que o texto tenha tamanho par, necessário para a cifra de Hill.
    Adiciona 'X' ao final caso o tamanho seja ímpar.
 
    Args:
        texto (str): Texto a ser preparado.
 
    Returns:
        str: Texto com tamanho par.
    """
    if len(texto) % 2 != 0:
        texto += 'X'
    return texto

def multiplicar_matriz(matriz, vetor):
    """
    Realiza a multiplicação manual de uma matriz 2x2 por um vetor 2x1 mod 26.
 
    Args:
        matriz (list): Matriz 2x2 representada como lista de listas.
        vetor (list): Vetor 2x1 representado como lista de dois inteiros.
 
    Returns:
        list: Resultado da multiplicação como lista de dois inteiros.
    """
    return [
        (matriz[0][0]*vetor[0] + matriz[0][1]*vetor[1]) % 26,
        (matriz[1][0]*vetor[0] + matriz[1][1]*vetor[1]) % 26
    ]

def criptografar_hill(texto):
    """
    Aplica a cifra de Hill para criptografar um texto.
 
    Args:
        texto (str): Texto em letras maiúsculas a ser criptografado.
 
    Returns:
        str: Texto criptografado.
    """
    texto = preparar_texto(texto)
    numeros = texto_para_numeros(texto)

    resultado = []

    for i in range(0, len(numeros), 2):
        bloco = [numeros[i], numeros[i+1]]

        cifrado = multiplicar_matriz(CHAVE, bloco)
        resultado.extend(cifrado)

    return numeros_para_texto(resultado)

def descriptografar_hill(texto):
    """
    Reverte a cifra de Hill para descriptografar um texto.
 
    Args:
        texto (str): Texto criptografado em letras maiúsculas.
 
    Returns:
        str: Texto original descriptografado.
    """
    numeros = texto_para_numeros(texto)

    resultado = []

    for i in range(0, len(numeros), 2):
        bloco = [numeros[i], numeros[i+1]]

        decifrado = multiplicar_matriz(CHAVE_INV, bloco)
        resultado.extend(decifrado)

    return numeros_para_texto(resultado)

def cpf_para_letras(cpf):
    """
    Converte um CPF numérico para letras, necessário para aplicar a cifra de Hill.
 
    Args:
        cpf (str): CPF composto apenas por dígitos numéricos.
 
    Returns:
        str: CPF convertido para letras maiúsculas.
    """
    mapa = {
        '0':'A','1':'B','2':'C','3':'D','4':'E',
        '5':'F','6':'G','7':'H','8':'I','9':'J'
    }
    return ''.join(mapa[d] for d in cpf)


def letras_para_cpf(texto):
    """
    Converte letras de volta para dígitos numéricos do CPF.
 
    Args:
        texto (str): Texto em letras maiúsculas representando um CPF.
 
    Returns:
        str: CPF em formato numérico.
    """
    mapa = {
        'A':'0','B':'1','C':'2','D':'3','E':'4',
        'F':'5','G':'6','H':'7','I':'8','J':'9'
    }
    return ''.join(mapa[l] for l in texto if l in mapa)