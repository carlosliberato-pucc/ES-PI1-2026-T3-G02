import gerenciamento
import votacao

def menuInicial():

    while True:
        print('--- Menu Inicial ---')
        print('[1] Gerenciamento')
        print('[2] Votação')
        print('[3] Cancelar')

        opcao = int(input("Digite a opção que deseja: "))

        match opcao:
            case 1: 
                gerenciamento.gerenciamento() 
                break
            case 2: 
                votacao.votacao()
                break
            case 3: 
                return
            case _: 
                print('\nOpção Inválida. Tente Novamente...\n')
