#Desenvolvido por Bruno Terra
#Desenvolvido por Carlos Liberato
import os
import sys
import time

def limparTela():
    """
    
    Serve para limpar o terminal quando usada.
    
    Args:
        Nenhum
    
    Returns:
        None
        """
    os.system('cls' if os.name == 'nt' else 'clear')

def pontilhado(palavra : str, tempo : int):
    """
    Exibe uma animação de pontos crescentes no terminal por um determinado tempo.
 
    Args:
        palavra (str): Texto a ser exibido antes dos pontos.
        tempo (int): Quantidade de iterações da animação.
 
    Returns:
        None
    """


    for i in range(tempo):
        print(f"\r{palavra+'.' * i}", end="")
        sys.stdout.flush()
        time.sleep(0.5)

def contagem_regressiva(palavra : str, tempo : int):
    """
    Exibe uma contagem regressiva no terminal a partir do valor informado até zero.
 
    Args:
        palavra (str): Texto a ser exibido antes do número da contagem.
        tempo (int): Valor inicial da contagem regressiva.
 
    Returns:
        None
    """

    # range(inicio, fim, passo) -> começa em 5, vai até 0, diminuindo 1 por vez
    for i in range(tempo, -1, -1):
        # \r volta ao início, end="" evita pular linha
        print(f"\r{palavra} {i}...", end="", flush=True)
        time.sleep(1)
    