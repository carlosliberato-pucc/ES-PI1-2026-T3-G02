# Desenvolvido por Felipe Miranda

from database.conexao import conectar
import mysql.connector

from eleitores import criptoChaveAcesso
from eleitores import criptoCPF
from eleitores import validacoes
import utils
from votacao.auditoria import registrarLog

def _normalizar_perfil(perfil):
    """
    Normaliza o perfil do eleitor removendo espaços e acentos para comparação.
 
    Args:
        perfil (str): Perfil do eleitor retornado do banco de dados.
 
    Returns:
        str: Perfil normalizado em letras minúsculas e sem acentos.
    """

    return str(perfil).strip().lower().replace("á", "a")


def autenticarMesario():
    """
    Autentica um usuário como mesário para abrir/encerrar votação.
    Args:
        Nenhum.

    Returns:
        bool: True se autenticado, False caso contrário
    """

    conexao = None
    cursor = None

    print("\n===== AUTENTICAÇÃO DO MESÁRIO =====\n")

    titulo = input("- Digite o título de eleitor: ").strip()
    while not validacoes.validaTitulo(titulo):
        print("Erro: Título Inválido. Tente Novamente...\n")
        titulo = input("- Digite o Título de Eleitor: ")
    
    while(True):
        cpf_parcial = input("- Digite os 4 primeiros dígitos do CPF: ").strip()
        if not cpf_parcial.isdigit() or len(cpf_parcial) != 4:
            print("--ERRO: informe exatamente os 4 primeiros dígitos do CPF\n")
        else:
            break
    
    while(True):
        chave = input("- Digite a chave de acesso: ").strip().upper()
        if not chave:
            print("ERRO: chave de acesso não informada")
        else:
            break

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

        print("")
        utils.pontilhado("Verificando Dados", 4)
        print("\n")
        if not resultado:
            print("ERRO: usuário não encontrado")
            registrarLog("ALERTA: Tentativa de acesso negado")
            return False

        cpf_cripto_db, perfil, chave_db = resultado
        cpf_letras = criptoCPF.descriptografar_hill(cpf_cripto_db)
        cpf_original = criptoCPF.letras_para_cpf(cpf_letras)

        if not cpf_original.startswith(cpf_parcial):
            print("ERRO: CPF não confere")
            registrarLog("ALERTA: Tentativa de acesso negado")
            return False

        if chave_cripto != chave_db:
            print("ERRO: chave de acesso inválida")
            registrarLog("ALERTA: Tentativa de acesso negado")
            return False

        if _normalizar_perfil(perfil) != "mesario":
            print("ERRO: usuário não é mesário")
            registrarLog("ALERTA: Tentativa de acesso negado")
            return False

        print("\nMesário autenticado com sucesso!")
        return True

    except mysql.connector.Error as erro:
        print(f"ERRO: falha ao autenticar mesário: {erro}")
        registrarLog("ALERTA: Tentativa de acesso negado")
        return False

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()

def autenticarEleitor():
    """
    Autentica um usuário.
    Args:
        Nenhum.
    Returns:
        str or None: título de eleitor se autenticado, None caso contrário
    """

    conexao = None
    cursor = None

    print("\n===== AUTENTICAÇÃO DO ELEITOR =====\n")

    titulo = input("- Digite o título de eleitor: ").strip()
    while not validacoes.validaTitulo(titulo):
        if not validacoes.validaTitulo(titulo):
            print("Erro: Título Inválido. Tente Novamente...\n")
            titulo = input("- Digite o Título de Eleitor: ")
    
    while(True):
        cpf_parcial = input("- Digite os 4 primeiros dígitos do CPF: ").strip()
        if not cpf_parcial.isdigit() or len(cpf_parcial) != 4:
            print("ERRO: informe exatamente os 4 primeiros dígitos do CPF")
        else:
            break
    
    while(True):
        chave = input("- Digite a chave de acesso: ").strip().upper()
        if not chave:
            print("ERRO: chave de acesso não informada")
        else:
            break

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        chave_cripto = criptoChaveAcesso.criptografar_hill(chave)

        query = """
            SELECT cpf, flag_voto, chave_acesso
            FROM eleitores
            WHERE titulo_eleitor = %s
        """
        cursor.execute(query, (titulo,))
        resultado = cursor.fetchone()

        print("")
        utils.pontilhado("Verificando Dados", 3)
        print("\n")
        if not resultado:
            print("ERRO: usuário não encontrado")
            registrarLog("ALERTA: Tentativa de acesso negado")
            return None

        cpf_cripto_db, flag_voto, chave_db = resultado
        cpf_letras = criptoCPF.descriptografar_hill(cpf_cripto_db)
        cpf_original = criptoCPF.letras_para_cpf(cpf_letras)

        if not cpf_original.startswith(cpf_parcial):
            print("ERRO: CPF não confere")
            registrarLog("ALERTA: Tentativa de acesso negado")
            return None

        if chave_cripto != chave_db:
            print("ERRO: chave de acesso inválida")
            registrarLog("ALERTA: Tentativa de acesso negado")
            return None

        if flag_voto:
            print("ERRO: usuário já votou")
            registrarLog("ALERTA: Tentativa de voto duplo")
            return None

        print("Eleitor autenticado com sucesso!")
        # Retorna o título do eleitor para o fluxo de votação continuar.
        return titulo

    except mysql.connector.Error as erro:
        print(f"ERRO: falha ao autenticar eleitor: {erro}")
        return None

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()
