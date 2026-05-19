# Desenvolvido por Nicolas Guimarães
from database.conexao import conectar
from datetime import datetime
import os
import mysql.connector
import votacao.criptoProtocolo as criptoProtocolo

LOG_FILE = "logs.txt"

def registrarLog(mensagem):
    """
    Registra um evento no arquivo de log com timestamp no formato [YYYY-MM-DD HH:MM:SS].

    Args:
        mensagem (str): Descrição do evento a ser registrado.

    Returns:
        None
    """
    try:

        with open(LOG_FILE, "a", encoding="utf-8") as f:
            timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
            f.write(f"{timestamp} {mensagem}\n")
            
    except Exception as e:
        print(f"Erro ao escrever log: {e}")

def exibirLogs():
    """
    Exibe todo o conteúdo do arquivo de logs no terminal.
    Caso o arquivo não exista, informa que não há logs registrados.

    Args:
        Nenhum.

    Return:
        None
    """
    print("\n===== LOGS DE OCORRÊNCIAS =====\n")

    if not os.path.exists(LOG_FILE):

        print("Nenhum log registrado até o momento.")
        return

    try:

        with open(LOG_FILE, "r", encoding="utf-8") as f:
            logs = f.read()

            if logs.strip():
                print(logs)

            else:
                print("Arquivo de log está vazio.")

    except Exception as e:
        print(f"Erro ao ler o arquivo de log: {e}")

def exibirProtocolos():
    """
    Lista todos os protocolos de votação armazenados no banco de dados,
    descriptografando‑os e exibindo em ordem alfabética (case‑insensitive).

    Args:
        Nenhum.

    Return:
        None
    """
    print("\n===== PROTOCOLOS DE VOTAÇÃO =====\n")

    conexao = conectar()
    cursor = conexao.cursor()

    try:

        cursor.execute("SELECT protocolo_confirmacao FROM votos ORDER BY protocolo_confirmacao")
        registros = cursor.fetchall()

        if not registros:
            print("Nenhum protocolo de votação encontrado.")
            return

        protocolos_originais = []

        for (protocolo_cripto,) in registros:

            try:
                protocolo_original = criptoProtocolo.descriptografar_protocolo(protocolo_cripto)
                protocolos_originais.append(protocolo_original)

            except Exception as e:
                print(f"Erro ao descriptografar protocolo {protocolo_cripto}: {e}")

        # Ordem alfabética (case‑insensitive)
        protocolos_originais.sort(key=lambda x: x.upper())

        for p in protocolos_originais:
            print(p)

    except mysql.connector.Error as e:
        print(f"Erro ao consultar protocolos: {e}")

    finally:
        cursor.close()
        conexao.close()