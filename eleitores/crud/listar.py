from database.conexao import conectar
import mysql.connector
import eleitores.validacoes as validacoes
import menus
import eleitores.criptoCPF as criptoCPF
import eleitores.chaveAcesso as chaveAcesso
import eleitores.criptoChaveAcesso as criptoChaveAcesso

def listarEleitor():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = """
        SELECT id_eleitor, nome_eleitor, cpf, titulo_eleitor, perfil, chave_acesso, flag_voto
        FROM eleitores
        ORDER BY nome_eleitor
    """

    cursor.execute(sql)
    eleitores = cursor.fetchall()

    print("\n::: Lista de Eleitores :::\n")

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

    menus.menuGerenciamento()