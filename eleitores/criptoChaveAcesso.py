# Desenvolvido por Carlos Luciano

"""
 texto_para_numeros(texto)
 Converte cada caractere de uma string no seu índice numérico correspondente baseado no ALFABETO.
 Parâmetros de Entrada (Args):
 texto (str): A sequência de caracteres a ser convertida.
 Retorno (Returns):list: Uma lista de números inteiros (int) representando as posições dos caracteres.
 
 numeros_para_texto(numeros)
 Realiza o inverso da função anterior, transformando índices numéricos de volta em caracteres.
 Parâmetros de Entrada (Args):
 numeros (list): Uma lista de números inteiros (int).
 Retorno (Returns):
 str: Uma string contendo os caracteres correspondentes do ALFABETO.
 
 preparar_texto(texto)
 Ajusta o comprimento da string para que seja múltiplo de 2, adicionando um preenchimento ('X') se necessário.
 Parâmetros de Entrada (Args):
 texto (str): O texto original.
 Retorno (Returns):
 str: O texto com comprimento par.
 
 multiplicar_matriz(matriz, vetor)
 Realiza o cálculo matemático central da Cifra de Hill: multiplica uma matriz 2x2 por um vetor 2x1 sob aritmética modular (módulo 36).
 Parâmetros de Entrada (Args):
 matriz (list): Uma lista de listas representando uma matriz 2x2.
 vetor (list): Uma lista com 2 números inteiros representando um bloco de texto.
 Retorno (Returns):list: Uma lista com 2 novos números inteiros (int) resultantes da operação.
 
 criptografar_hill(texto)
 Orquestra o processo de cifragem, tratando o texto e aplicando a multiplicação pela matriz CHAVE.
 Parâmetros de Entrada (Args):
 texto (str): O texto em formato legível (plaintext).
 Retorno (Returns):
 str: O texto criptografado (ciphertext).
 
 descriptografar_hill(texto)
 Realiza o processo de decifragem utilizando a CHAVE_INVERSA e remove o caractere de preenchimento final.
 Parâmetros de Entrada (Args):
 texto (str): O texto criptografado.
 Retorno (Returns):
 str: O texto original recuperado (sem o último caractere de ajuste).
"""


CHAVE = [[5,2],
        [7,3]]
    
CHAVE_INVERSA = [[3,34],
                [29,5]]

ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def texto_para_numeros(texto):
    # Converte letras para números (A=0, B=1, ..., Z=25)
    return [ALFABETO.index(c.upper()) for c in texto]


def numeros_para_texto(numeros):
    # Converte números para letras
    return ''.join([ALFABETO[n] for n in numeros])


def preparar_texto(texto):
    # Garante que o texto tenha tamanho par (necessário na cifra de Hill)
    if len(texto) % 2 != 0:
        texto += 'X'
    return texto

def multiplicar_matriz(matriz, vetor):
    # Multiplicação manual de matriz 2x2 por vetor 2x1
    return [
        (matriz[0][0]*vetor[0] + matriz[0][1]*vetor[1]) % 36,
        (matriz[1][0]*vetor[0] + matriz[1][1]*vetor[1]) % 36
    ]
def criptografar_hill(texto):
    # Aplica a cifra de Hill
    texto = preparar_texto(texto)
    numeros = texto_para_numeros(texto)

    resultado = []

    for i in range(0, len(numeros), 2):
        bloco = [numeros[i], numeros[i+1]]

        cifrado = multiplicar_matriz(CHAVE, bloco)
        resultado.extend(cifrado)

    return numeros_para_texto(resultado)

def descriptografar_hill(texto):
    # Reverte a cifra de Hill
    numeros = texto_para_numeros(texto)

    resultado = []

    for i in range(0, len(numeros), 2):
        bloco = [numeros[i], numeros[i+1]]

        decifrado = multiplicar_matriz(CHAVE_INVERSA, bloco)
        resultado.extend(decifrado)

    return numeros_para_texto(resultado)[:-1]






