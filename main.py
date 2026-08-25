from jogos import plataformas

def menu_jogos():
    opcao = input("Digite 1-Cadastrar 2-Listar: ")
    if (opcao == '1'):
        print("Plataformas:")
        for indice, plataforma in enumerate(plataformas, start=1):
            print(indice, "-", plataforma)
        plataforma_escolhida = int(input("Escolha: ")) - 1
        titulo = input("Informe o título do jogo: ")
        genero = input("Informe o gênero: ")
        valor = input("Inform o valor de locação: ")
        

def menu_clientes():
    pass

def menu_locacoes():
    pass

def menu():
    while (True):
        print("=== Menu de opções ===")
        print("1-Jogos\n2-Clientes\n3-Locações\n4-Sair")
        opcao = input("Digite a opção: ")

        if (opcao == '1'):
            menu_jogos()
        elif (opcao == '4'):
            break


menu()