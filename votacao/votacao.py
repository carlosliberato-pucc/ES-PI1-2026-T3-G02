#Desenvolvido por Carlos Liberato
import votacao.auth as auth
import votacao.zeresima as zeresima
import menus as menus
import candidatos.listarCandidato as candidatos
from datetime import datetime
def abrirVotacao():
    
    zeresima.zeresima()

    menus.menuOperarVotacao()

def operarVotacao():

    cargos = ["Deputado Estadual", "Deputado Federal", "Senador", "Governador", "Presidente"]

    if(auth.autenticarEleitor() == True):
        print("\n")
        print(':'*29)
        print("::::::: ELEIÇÕES 2026 :::::::")
        print(':'*29)

        for cargo in cargos:
            confirmado = False
            
            while not confirmado:

                while True:
                    try:
                        print(f"\n{cargo.upper()}")
                        voto = int(input("Digite o número: "))
                        candidatos.imprimirCandidato(voto, cargo)
                        break
                    except ValueError:
                        print("--Erro: Entrada Inválida. Tente Novamente..")
                    

                while True:
                    print("1 - [CONFIRMAR]")
                    print("0 - [CANCELAR]")

                    try:
                        opcao = int(input("Digite a opção: "))
                        if opcao == 1:
                            confirmado = True
                            break
                        elif opcao == 0:
                            print("Voto Cancelado")
                            break
                        else:
                            print("\nOpção Inválida. Tente Novamente")
                            break
                    except ValueError:
                        print("--Erro: Digite 0 ou 1.")

                if confirmado:
                    print("Voto Confirmado")
                    #salvar no banco de dados e dar flag_voto = True (tabela eleitores)
                    break
        print("\n")
        gerarDataHora()
        
def gerarDataHora():
    agora = datetime.now()
    print(f"Data e Hora: {agora}")

def encerrarVotacao():
    pass