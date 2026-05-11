#Desenvolvido por Carlos Liberato
#Desenvolvido por Gabriel Coutinho
#Desenvolvido por Bruno Terra
#Desenvolvido por Nicolas Guimarães
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

    titulo_eleitor = auth.autenticarEleitor()

    if titulo_eleitor:
        print("\n")
        print(':'*29)
        print("::::::: ELEIÇÕES 2026 :::::::")
        print(':'*29)

        votos_confirmados = []
        confirmacao = False
        while not confirmacao:
            while True:
                try:
                    voto = int(input("Digite o número: "))
                    candidato = candidatos.imprimirCandidato(voto)
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
                        confirmacao = True
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
        # Após confirmar tudo, gera o protocolo e salva o registro.
        protocolo = gerarProtocolo()
        if salvarVotos(votos_confirmados, protocolo, titulo_eleitor):
            print("Voto registrado com sucesso.")
            print(f"Protocolo de confirmação (criptografado): {protocolo}")
        gerarDataHora()

def gerarDataHora():
    agora = datetime.now()
    print(f"Data e Hora: {agora}")


def encerrarVotacao():

    """

    Realiza o encerramento oficial da votação mediante autenticação do mesário

    e dupla confirmação de identidade.



    O fluxo segue os requisitos RF002.01.07.01 a RF002.01.07.06:

    1. Autentica o mesário (título, CPF parcial e chave de acesso).

    2. Solicita confirmação explícita de encerramento (Sim/Não).

    3. Exige uma segunda inserção da chave de acesso como protocolo final.

    4. Encerra a votação definitivamente se todas as validações forem aprovadas.



    Args:

        Nenhum.



    Returns:

        bool: True se a votação foi encerrada com sucesso, False caso contrário.

    """

    print("\n=== Encerramento da Votação ===\n")
        

    # Autentica o mesário
    if not auth.autenticarMesario():
        print("ERRO: Encerramento cancelado. Falha na autenticação do mesário.")
        return False

    # Pergunta de confirmação
    print("\nDeseja realmente encerrar a votação?")
    print("[1] Sim")
    print("[0] Não")
    try:
        confirmacao = int(input("Digite sua opção: "))
    except ValueError:
        print("ERRO: Opção inválida. Encerramento cancelado.")
        return False

    if confirmacao != 1:
        print("Encerramento cancelado. Retornando ao menu...")
        return False

    # Segunda inserção da chave de acesso como dupla confirmação
    print("\nConfirmação final necessária.")
    chave_confirmacao = input("Digite novamente sua chave de acesso: ").strip().upper()

    if not chave_confirmacao:
        print("ERRO: Chave de acesso não informada. Encerramento cancelado.")
        return False

    # Valida a segunda chave e encerra definitivamente
    chave_cripto = criptoChaveAcesso.criptografar_hill(chave_confirmacao)

    conexao = None
    cursor = None

    try:
        # Conecta ao banco de dados para validar a segunda chave

        conexao = conectar()
        cursor = conexao.cursor()

        # Busca a chave criptografada no banco para confirmar a identidade do mesário

        cursor.execute(
            "SELECT chave_acesso FROM eleitores WHERE chave_acesso = %s",
            (chave_cripto,)
        )
        resultado = cursor.fetchone()

        # Se a chave não for encontrada, cancela o encerramento

        if not resultado:
            print("ERRO: Chave de acesso incorreta. Encerramento cancelado.")
            return False

        # Encerramento confirmado com sucesso

        print("\n" + "=" * 40)
        print("  VOTAÇÃO ENCERRADA COM SUCESSO!")
        print("=" * 40)
        gerarDataHora()
        return True

    except Exception as e:

        print(f"ERRO ao encerrar votação: {e}")
        return False

    finally:
        if cursor:
            cursor.close()

        if conexao and conexao.is_connected():
            conexao.close()
    