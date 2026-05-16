from database.conexao import conectar
import mysql.connector
import candidatos.crud.listarCandidatos as listarCandidatos
import utils
def zeresima():
    
    """
    zerezima()
    Deleta dados da tabela Votos no banco de dados e chava função que imprime a mesma tabela atualizada.

    Parâmetros de entrada (Args):
        Nenhum,

    Retorno (Returns):
    NULL
    """

    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    print("\n:::::::::::: Zerésima ::::::::::::\n")
    utils.pontilhado("Excluindo Votos", 3)
    cursor.execute("TRUNCATE TABLE votos;")

    listarCandidatos.listarVotosCandidato()
