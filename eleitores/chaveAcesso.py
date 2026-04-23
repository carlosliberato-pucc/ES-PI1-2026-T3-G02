import random
import string

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
