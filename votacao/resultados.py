#Desenvolvido por Bruno Terra

from database.conexao import conectar
import utils

def verificarIntegridadeVotos():
    """
    Verifica a integridade dos votos comparando o número total de votos registrados na tabela de votos
    com o número total de eleitores que votaram (flag_voto = TRUE) na tabela de eleitores.

    Args:
        Nenhum.
    Returns:
        None.
    """
    
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    try:
        sql = """
            SELECT 
                (SELECT COUNT(*) FROM votos) AS total_votos,
                (SELECT COUNT(*) FROM eleitores WHERE flag_voto = TRUE) AS total_eleitores_votaram;
        """
        cursor.execute(sql)
        resultados = cursor.fetchone()

        total_votos = resultados['total_votos']
        total_eleitores_votaram = resultados['total_eleitores_votaram']

        if total_votos != total_eleitores_votaram:
            print("\nALERTA: Número de votos registrado no banco de dados é diferente do número de eleitores que votaram.")
            print(f"Total de votos registrados: {total_votos}")
            print(f"Total de eleitores que votaram: {total_eleitores_votaram}")     
        else:
            print("\nNenhum problema de integridade de votos encontrado. Integridade dos votos está OK.")
    except Exception as e:
        print(f"\nErro ao verificar integridade dos votos: {e}")

    finally:
        cursor.close()
        conexao.close()

def estatisticasDeComparecimento():
    """
    Exibe estatísticas de comparecimento dos eleitores, mostrando o número total de eleitores cadastrados,
    o número de eleitores que votaram e a porcentagem de comparecimento.

    Args:
        Nenhum.
    Returns:
        None.
    """
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    try:
        sql = """
            SELECT 
                (SELECT COUNT(*) FROM eleitores) AS total_eleitores,
                (SELECT COUNT(*) FROM eleitores WHERE flag_voto = TRUE) AS total_eleitores_votaram;
        """
        cursor.execute(sql)
        resultados = cursor.fetchone()

        total_eleitores = resultados['total_eleitores']
        total_eleitores_votaram = resultados['total_eleitores_votaram']

        if total_eleitores > 0:
            porcentagem_comparecimento = (total_eleitores_votaram / total_eleitores) * 100
        else:
            porcentagem_comparecimento = 0

        print("\n===== Estatísticas de Comparecimento =====")
        print(f"Total de eleitores cadastrados: {total_eleitores}")
        print(f"Total de eleitores que votaram: {total_eleitores_votaram}")
        print(f"Porcentagem de comparecimento: {porcentagem_comparecimento:.2f}%")

    except Exception as e:
        print(f"\nErro ao exibir estatísticas de comparecimento: {e}")

    finally:
        cursor.close()
        conexao.close()

def VotosPorPartido():
    """
    Exibe o número total de votos recebidos por cada partido político, 
    ordenando os resultados por número de votos.

    Args:
        Nenhum.
    Returns:
        None
    """
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    try:
        sql = """
            SELECT c.partido, COUNT(v.id_voto) AS total_votos
            FROM candidatos c
            LEFT JOIN votos v ON c.id_candidato = v.id_candidato
            GROUP BY c.partido
            ORDER BY total_votos DESC;
        """
        cursor.execute(sql)
        resultados = cursor.fetchall()

        print("\n===== Votos por Partido =====")
        for resultado in resultados:
            print(f"Partido: {resultado['partido']} - Total de votos: {resultado['total_votos']}")

    except Exception as e:
        print(f"\nErro ao exibir votos por partido: {e}")

    finally:
        cursor.close()
        conexao.close()

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


def resultados():
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
        print("[2] Verificar Integridade dos Votos")
        print("[3] Estatísticas de Comparecimento")
        print("[4] Votos por Partido")
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
            case 2:
                verificarIntegridadeVotos()
            case 3:
                estatisticasDeComparecimento()
            case 4:
                VotosPorPartido()
            case _:
                print("Opção inválida. Tente novamente.")




