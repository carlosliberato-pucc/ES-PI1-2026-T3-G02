#Desenvolvido por Bruno Terra

import os

def limparTela():
    """
    
    Serve para limpar o terminal quando usada.
    
    Args:
        Nenhum
    
    Returns:
        None
        """
    os.system('cls' if os.name == 'nt' else 'clear')