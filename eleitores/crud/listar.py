from database.conexao import conectar
import mysql.connector
import eleitores.validacoes as validacoes
import eleitores.criptoCPF as criptoCPF
import eleitores.chaveAcesso as chaveAcesso
import eleitores.criptoChaveAcesso as criptoChaveAcesso
import utils
import menus

def listarEleitor():
    """
    Lista todos os eleitores cadastrados no banco de dados em ordem alfabética,
    exibindo seus dados com CPF e chave de acesso descriptografados.
 
    Args:
        Nenhum.
 
    Returns:
        None
    """

    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = """
        SELECT id_eleitor, nome_eleitor, cpf, titulo_eleitor, perfil, chave_acesso, flag_voto
        FROM eleitores
        ORDER BY nome_eleitor
    """

    cursor.execute(sql)
    eleitores = cursor.fetchall()

    print("\n===== LISTA DE ELEITORES =====\n")

    if not eleitores:
        print("Nenhum eleitor cadastrado.")
    else:
        for eleitor in eleitores:
            cpf_decodificado = criptoCPF.letras_para_cpf(
                criptoCPF.descriptografar_hill(eleitor["cpf"])
            )

            chave_decodificada = criptoChaveAcesso.descriptografar_hill(
                eleitor["chave_acesso"]
            )

            print(f"ID: {eleitor['id_eleitor']}")
            print(f"Nome: {eleitor['nome_eleitor']}")
            print(f"CPF: {cpf_decodificado}")
            print(f"Título: {eleitor['titulo_eleitor']}")
            print(f"Perfil: {eleitor['perfil']}")
            print(f"Chave de Acesso: {chave_decodificada}")
            print(f"Votou: {'Sim' if eleitor['flag_voto'] else 'Não'}")
            print("-" * 40)

    cursor.close()
    conexao.close()

    escolha = menus.lerOpcaoInteira('Digite "0" para voltar para o menu: ')
    while True:
        if escolha == 0:
            utils.limparTela()
            break
    

    