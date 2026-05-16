#Desenvolvido por Bruno Terra

from database.conexao import conectar
import utils

def boletimUrna():

    """
    Exibe o boletim de urna com os votos consolidados por candidato em ordem
    alfabética e declara o vencedor da eleição ao final.
 
    Args:
        Nenhum.
 
    Returns:
        None
    """

    print("\n===============================")
    print("         BOLETIM DE URNA")
    print("===============================")


    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
 
    try:
        sql = """
            SELECT c.id_candidato, c.nome_candidato, c.partido,
                   COUNT(v.id_voto) AS total_votos
            FROM candidatos c
            LEFT JOIN votos v ON c.id_candidato = v.id_candidato
            GROUP BY c.id_candidato, c.nome_candidato, c.partido
            ORDER BY c.nome_candidato ASC
        """
        cursor.execute(sql)
        candidatos = cursor.fetchall()


        if not candidatos:
            print("\nNenhum candidato cadastrado.")
            return


        vencedor = None
        for candidato in candidatos:
            print(f"\nNome: {candidato['nome_candidato']}")
            print(f"Número: {candidato['id_candidato']}")
            print(f"Partido: {candidato['partido']}")
            print(f"Total de votos: {candidato['total_votos']}")
            print("-" * 40)


            if vencedor is None or candidato['total_votos'] > vencedor['total_votos']:
                vencedor = candidato



        if vencedor:
            print("========================================")
            print("        VENCEDOR DA ELEIÇÃO")
            print("=" * 40)
            print(f"Nome: {vencedor['nome_candidato']}")
            print(f"Número: {vencedor['id_candidato']}")
            print(f"Partido: {vencedor['partido']}")
            print(f"Total de votos: {vencedor['total_votos']}")
            print("========================================")


    except Exception as e:
        print(f"\nErro ao gerar boletim de urna: {e}")
 
    finally:
        cursor.close()
        conexao.close()


def resultados() -> None:
    """
    Exibe o menu de resultados da votação com as opções disponíveis.
 
    Args:
        Nenhum.
 
    Returns:
        None
    """
    while True:
        print("\n===== Resultados da Votação =====")
        print("[1] Boletim de Urna")
        print("[0] Voltar")
 
        try:
            opcao = int(input("Digite uma opção: "))
            utils.limparTela()
        except ValueError:
            print("Opção inválida. Tente novamente.")
            continue
 
        match opcao:
            case 0:
                return
            case 1:
                boletimUrna()
            case _:
                print("Opção inválida. Tente novamente.")




