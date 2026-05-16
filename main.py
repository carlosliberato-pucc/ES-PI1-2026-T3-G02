# Desenvolvido por Carlos Liberato
import menus
import database.conexao as conexao
# para instalar as bibliotecas rode no terminal: 

def main():
    """Conecta ao banco de dados e inicializa o sistema exibindo o menu principal.

    Args:
        Nenhum.

    Returns:
        Nenhum.
    """
    conexao.conectar() # conecta com o banco de dados antes de printar o menu 
    menus.menuInicial()

if __name__ == "__main__":
    main()