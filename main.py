# Desenvolvido por Carlos Liberato
import menus
import database.conexao as conexao
# para instalar as bibliotecas rode no terminal: 
# pip install -r requirements.txt

def main():
    print("\n====== LAD.py - Sistema de Votação Digital ======")
    conexao.conectar() # conecta com o banco de dados antes de printar o menu 
    menus.menuInicial()

if __name__ == "__main__":
    main()