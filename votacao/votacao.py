#Desenvolvido por Carlos Liberato
#Desenvolvido por Gabriel Coutinho
#Desenvolvido por Bruno Terra
import random
import votacao.auth as auth
import votacao.zeresima as zeresima
import menus as menus
import candidatos.listarCandidato as candidatos
from database.conexao import conectar
from eleitores import criptoChaveAcesso
from datetime import datetime

def abrirVotacao():
    
    zeresima.zeresima()

    menus.menuOperarVotacao()

def gerarProtocolo():
    # Gera um código numérico aleatório e aplica a cifra de Hill
    # para produzir o protocolo de confirmação criptografado.
    codigo = ''.join(str(random.randint(0, 9)) for _ in range(8))
    protocolo = criptoChaveAcesso.criptografar_hill(codigo)
    return protocolo


# Desenvolvido por Bruno Terra
def salvarVotos(votos, protocolo, titulo_eleitor):
    """
    salvarVotos(votos, protocolo, titulo_eleitor)
    Armazena os votos no banco de dados junto com o protocolo de confirmação
    e atualiza o status do eleitor para indicar que já votou.

    Parâmetros de Entrada (Args):
    votos (list): Lista com IDs dos candidatos votados.
    protocolo (str): Protocolo criptografado da votação.
    titulo_eleitor (str): Título do eleitor autenticado.

    Retorno (Returns):
    bool: True se sucesso, False em caso de erro.
    """

    conexao = None
    cursor = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        # comando SQL para inserir votos
        sql = """
        INSERT INTO votos (id_candidato, data_hora, protocolo_confirmacao)
        VALUES (%s, NOW(), %s)
        """

        # salva cada voto com o mesmo protocolo
        for id_candidato in votos:
            cursor.execute(sql, (id_candidato, protocolo))

        # atualiza eleitor como já votou
        cursor.execute(
            "UPDATE eleitores SET flag_voto = TRUE WHERE titulo_eleitor = %s",
            (titulo_eleitor,)
        )

        # confirma alterações
        conexao.commit()

        return True

    except Exception as e:
        print("Erro ao salvar votos:", e)

        if conexao:
            conexao.rollback()

        return False

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()

def operarVotacao():

    cargos = ["Deputado Estadual", "Deputado Federal", "Senador", "Governador", "Presidente"]
    titulo_eleitor = auth.autenticarEleitor()

    if titulo_eleitor:
        print("\n")
        print(':'*29)
        print("::::::: ELEIÇÕES 2026 :::::::")
        print(':'*29)

        votos_confirmados = []

        for cargo in cargos:
            while True:
                try:
                    print(f"\n{cargo.upper()}")
                    voto = int(input("Digite o número: "))
                    candidato = candidatos.imprimirCandidato(voto, cargo)
                    if not candidato:
                        print("--Erro: Número de candidato inválido. Tente novamente.")
                        continue
                    break
                except ValueError:
                    print("--Erro: Entrada Inválida. Tente Novamente..")

            while True:
                print("1 - [CONFIRMAR]")
                print("0 - [CANCELAR]")

                try:
                    opcao = int(input("Digite a opção: "))
                    if opcao == 1:
                        votos_confirmados.append(candidato['id_candidato'])
                        print("Voto Confirmado")
                        break
                    elif opcao == 0:
                        print("Voto Cancelado")
                        break
                    else:
                        print("\nOpção Inválida. Tente Novamente")
                except ValueError:
                    print("--Erro: Digite 0 ou 1.")

        print("\n")
        # Após confirmar todos os cargos, gera o protocolo e salva o registro.
        protocolo = gerarProtocolo()
        if salvarVotos(votos_confirmados, protocolo, titulo_eleitor):
            print("Voto registrado com sucesso.")
            print(f"Protocolo de confirmação (criptografado): {protocolo}")
        gerarDataHora()


def gerarDataHora():
    agora = datetime.now()
    print(f"Data e Hora: {agora}")

def encerrarVotacao():
    pass