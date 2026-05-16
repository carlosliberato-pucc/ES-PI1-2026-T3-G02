#Desenvolvido por Gabriel Coutinho

CHAVE_PROTOCOLO = [[7, 3],
                   [6, 5]]

CHAVE_PROTOCOLO_INV = [[13, 21],
                       [6, 11]]

ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


def texto_para_numeros(texto):
    """
    Converte cada caractere do texto para seu índice no alfabeto estendido.
 
    Args:
        texto (str): Texto composto por letras maiúsculas e/ou dígitos.
 
    Returns:
        list: Lista de inteiros representando cada caractere.
    """


    return [ALFABETO.index(c.upper()) for c in texto]


def numeros_para_texto(numeros):
    """
    Converte uma lista de índices de volta para caracteres do alfabeto estendido.
 
    Args:
        numeros (list): Lista de inteiros representando índices no alfabeto.
 
    Returns:
        str: Texto formado pelos caracteres correspondentes.
    """

    return ''.join(ALFABETO[n] for n in numeros)


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


def multiplicar_matriz(matriz, bloco):
    """
    Realiza a multiplicação de uma matriz 2x2 por um vetor 2x1 mod tamanho do alfabeto.
 
    Args:
        matriz (list): Matriz 2x2 representada como lista de listas.
        bloco (list): Vetor 2x1 representado como lista de dois inteiros.
 
    Returns:
        list: Resultado da multiplicação como lista de dois inteiros.
    """

    return [
        (matriz[0][0] * bloco[0] + matriz[0][1] * bloco[1]) % len(ALFABETO),
        (matriz[1][0] * bloco[0] + matriz[1][1] * bloco[1]) % len(ALFABETO)
    ]


def criptografar_protocolo(texto):
    """
    Aplica a cifra de Hill para criptografar o protocolo de votação.
 
    Args:
        texto (str): Protocolo original em letras maiúsculas e dígitos.
 
    Returns:
        str: Protocolo criptografado.
    """

    texto = preparar_texto(texto)
    numeros = texto_para_numeros(texto)

    resultado = []
    for i in range(0, len(numeros), 2):
        bloco = [numeros[i], numeros[i + 1]]
        cifrado = multiplicar_matriz(CHAVE_PROTOCOLO, bloco)
        resultado.extend(cifrado)

    return numeros_para_texto(resultado)


def descriptografar_protocolo(texto):
    """
    Reverte a cifra de Hill para descriptografar o protocolo de votação.
    Remove o caractere 'X' de padding ao final, se houver.
 
    Args:
        texto (str): Protocolo criptografado em letras maiúsculas e dígitos.
 
    Returns:
        str: Protocolo original descriptografado.
    """

    numeros = texto_para_numeros(texto)

    resultado = []
    for i in range(0, len(numeros), 2):
        bloco = [numeros[i], numeros[i + 1]]
        decifrado = multiplicar_matriz(CHAVE_PROTOCOLO_INV, bloco)
        resultado.extend(decifrado)

    texto_decifrado = numeros_para_texto(resultado)
    if texto_decifrado.endswith('X'):
        texto_decifrado = texto_decifrado[:-1]
    return texto_decifrado
