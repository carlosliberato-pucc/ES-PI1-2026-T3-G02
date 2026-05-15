#Desenvolvido por Gabriel Coutinho

CHAVE_PROTOCOLO = [[7, 3],
                   [6, 5]]

CHAVE_PROTOCOLO_INV = [[13, 21],
                       [6, 11]]

ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


def texto_para_numeros(texto):
    return [ALFABETO.index(c.upper()) for c in texto]


def numeros_para_texto(numeros):
    return ''.join(ALFABETO[n] for n in numeros)


def preparar_texto(texto):
    if len(texto) % 2 != 0:
        texto += 'X'
    return texto


def multiplicar_matriz(matriz, bloco):
    return [
        (matriz[0][0] * bloco[0] + matriz[0][1] * bloco[1]) % len(ALFABETO),
        (matriz[1][0] * bloco[0] + matriz[1][1] * bloco[1]) % len(ALFABETO)
    ]


def criptografar_protocolo(texto):
    texto = preparar_texto(texto)
    numeros = texto_para_numeros(texto)

    resultado = []
    for i in range(0, len(numeros), 2):
        bloco = [numeros[i], numeros[i + 1]]
        cifrado = multiplicar_matriz(CHAVE_PROTOCOLO, bloco)
        resultado.extend(cifrado)

    return numeros_para_texto(resultado)


def descriptografar_protocolo(texto):
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
