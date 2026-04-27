# Desenvolvido por Gabriel Coutinho

from database.conexao import conectar
import mysql.connector
import eleitores.validacoes as validacoes
import menus
import eleitores.criptoCPF as criptoCPF
import eleitores.chaveAcesso as chaveAcesso
import eleitores.criptoChaveAcesso as criptoChaveAcesso

def buscarEleitor():
    # Conecta ao banco de dados e cria um cursor que retorna resultados como dicionário
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    # Exibe o menu de opções para escolher o tipo de busca
    print("\n::: Buscar Eleitor :::\n")
    print("[1] Buscar por CPF")
    print("[2] Buscar por Título de Eleitor")
    print("[3] Buscar por Nome")
    print("[0] Voltar")

    # Loop para garantir que a opção seja um número inteiro válido
    while True:
        try:
            opcao = int(input("Digite a opção desejada: "))
            break
        except ValueError:
            print("\nERRO: digite apenas números. Tente novamente.\n")
    
    # Busca por CPF
    if opcao == 1:
        cpf = input("- Digite o CPF (somente números): ")
        while not validacoes.validaCPF(cpf):
            # validação do cpf
            if not validacoes.validaCPF(cpf):
                print("--Erro: CPF Inválido. Tente Novamente...\n")
                cpf = input("- Digite o CPF (somente números): ")
        
        # Converte o CPF para letras e criptografa usando a mesma lógica de armazenamento
        cpf_convertido = criptoCPF.cpf_para_letras(cpf)
        cpf_criptografado = criptoCPF.criptografar_hill(cpf_convertido)
        sql = '''
            SELECT id_eleitor, nome_eleitor, cpf, titulo_eleitor, perfil, chave_acesso, flag_voto
            FROM eleitores
            WHERE cpf = %s
        '''
        params = (cpf_criptografado,)

    # Busca por Título de Eleitor
    elif opcao == 2:
        titulo = input("- Digite o Título de Eleitor (somente números): ")
        while not validacoes.validaTitulo(titulo):
            # chamando função de validação
            if not validacoes.validaTitulo(titulo):
                print("--Erro: Título Inválido. Tente Novamente...\n")
                titulo = input("- Digite o Título de Eleitor (somente números): ")
        
        sql = '''
            SELECT id_eleitor, nome_eleitor, cpf, titulo_eleitor, perfil, chave_acesso, flag_voto
            FROM eleitores
            WHERE titulo_eleitor = %s
        '''
        params = (titulo,)

    # Busca por Nome
    elif opcao == 3:
        nome = input("Digite o nome completo ou parte do nome: ").strip()
        if not nome:
            print("Busca cancelada: Nome inválido.")
            cursor.close()
            conexao.close()
            return
        
        # Usa LIKE para permitir busca por partes do nome
        sql = '''
            SELECT id_eleitor, nome_eleitor, cpf, titulo_eleitor, perfil, chave_acesso, flag_voto
            FROM eleitores
            WHERE nome_eleitor LIKE %s
        '''
        params = (f'%{nome}%',)

    elif opcao == 0:
        menus.menuGerenciamento()
    # Opção inválida
    else:
        print("Opção de busca inválida.")
        cursor.close()
        conexao.close()
        return
    
    # Executa a consulta e salva os registros encontrados
    cursor.execute(sql, params)
    registros = cursor.fetchall()

    if not registros:
        print("\nNenhum eleitor encontrado.")
    else:
        print("\nResultados da busca: ")
        for eleitor in registros:
            # Descriptografa CPF e chave de acesso antes de mostrar
            cpf_decodificado = criptoCPF.letras_para_cpf(criptoCPF.descriptografar_hill(eleitor['cpf']))
            chave_acesso_decodificada = criptoChaveAcesso.descriptografar_hill(eleitor['chave_acesso'])
            print(f"Nome: {eleitor['nome_eleitor']}")
            print(f"CPF: {cpf_decodificado}")
            print(f"Título: {eleitor['titulo_eleitor']}")
            print(f"Perfil: {eleitor['perfil']}")
            print(f"Chave de Acesso: {chave_acesso_decodificada}")
            print(f"Votou: {'Sim' if eleitor['flag_voto'] else 'Não'}")
    
    # Fecha cursor e conexão ao final da função
    cursor.close()
    conexao.close()

    menus.menuGerenciamento()
