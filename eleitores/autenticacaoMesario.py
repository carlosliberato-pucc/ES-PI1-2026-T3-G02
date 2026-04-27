# Desenvolvido por Felipe Miranda

from database.conexao import conectar
import mysql.connector

from . import criptoChaveAcesso
from . import criptoCPF
from . import validacoes


def _normalizar_perfil(perfil):
    return str(perfil).strip().lower().replace("á", "a")


def autenticarMesario():
    """
    Autentica um usuário como mesário para abrir/encerrar votação.

    Returns:
        bool: True se autenticado, False caso contrário
    """

    conexao = None
    cursor = None

    print("\n=== Autenticação de Mesário ===\n")

    titulo = input("Digite o título de eleitor: ").strip()
    while not validacoes.validaTitulo():
        if not validacoes.validaTitulo(titulo):
            print("Erro: Título Inválido. Tente Novamente...\n")
            titulo = input("Digite o Título de Eleitor: ")
    
    while(True):
        cpf_parcial = input("Digite os 4 primeiros dígitos do CPF: ").strip()
        if not cpf_parcial.isdigit() or len(cpf_parcial) != 4:
            print("ERRO: informe exatamente os 4 primeiros dígitos do CPF")
        else:
            break;
    
    while(True):
        chave = input("Digite a chave de acesso: ").strip().upper()
        if not chave:
            print("ERRO: chave de acesso não informada")
        else:
            break;

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        chave_cripto = criptoChaveAcesso.criptografar_hill(chave)

        query = """
            SELECT cpf, perfil, chave_acesso
            FROM eleitores
            WHERE titulo_eleitor = %s
        """
        cursor.execute(query, (titulo,))
        resultado = cursor.fetchone()

        if not resultado:
            print("ERRO: usuário não encontrado")
            return False

        cpf_cripto_db, perfil, chave_db = resultado
        cpf_letras = criptoCPF.descriptografar_hill(cpf_cripto_db)
        cpf_original = criptoCPF.letras_para_cpf(cpf_letras)

        if not cpf_original.startswith(cpf_parcial):
            print("ERRO: CPF não confere")
            return False

        if chave_cripto != chave_db:
            print("ERRO: chave de acesso inválida")
            return False

        if _normalizar_perfil(perfil) != "mesario":
            print("ERRO: usuário não é mesário")
            return False

        print("Mesário autenticado com sucesso!")
        return True

    except mysql.connector.Error as erro:
        print(f"ERRO: falha ao autenticar mesário: {erro}")
        return False

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()
