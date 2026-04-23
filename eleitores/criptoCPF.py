
# MATRIZ CHAVE
CHAVE = [[3, 3],
         [2, 5]]

# MATRIZ INVERSA (já calculada mod 26)
CHAVE_INV = [[15, 17],
             [20, 9]]


def texto_para_numeros(texto):
    # Converte letras para números (A=0, B=1, ..., Z=25)
    return [ord(c) - 65 for c in texto]


def numeros_para_texto(numeros):
    # Converte números para letras
    return ''.join([chr(n + 65) for n in numeros])


def preparar_texto(texto):
    # Garante que o texto tenha tamanho par (necessário na cifra de Hill)
    if len(texto) % 2 != 0:
        texto += 'X'
    return texto

def multiplicar_matriz(matriz, vetor):
    # Multiplicação manual de matriz 2x2 por vetor 2x1
    return [
        (matriz[0][0]*vetor[0] + matriz[0][1]*vetor[1]) % 26,
        (matriz[1][0]*vetor[0] + matriz[1][1]*vetor[1]) % 26
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

        decifrado = multiplicar_matriz(CHAVE_INV, bloco)
        resultado.extend(decifrado)

    return numeros_para_texto(resultado)

def cpf_para_letras(cpf):
    # Converte CPF numérico para letras (necessário para Hill)
    mapa = {
        '0':'A','1':'B','2':'C','3':'D','4':'E',
        '5':'F','6':'G','7':'H','8':'I','9':'J'
    }
    return ''.join(mapa[d] for d in cpf)


def letras_para_cpf(texto):
    # Converte letras de volta para CPF numérico
    mapa = {
        'A':'0','B':'1','C':'2','D':'3','E':'4',
        'F':'5','G':'6','H':'7','I':'8','J':'9'
    }
    return ''.join(mapa[l] for l in texto if l in mapa)