# EX9

print("------- MENU -------")
print("1 - Cadastrar")
print("2 - Consultar")
print("3 - Editar")
print("4 - Excluir")
print("5 - Sair")

opcao = int(input("Escolha uma opção: "))

match opcao:
    case 1:
        print("Cadastrar selecionado")
    case 2:
        print("Consultar selecionado")
    case 3:
        print("Editar selecionado")
    case 4:
        print("Excluir selecionado")
    case 5:
        print("Sair selecionado")
    case _:
        print("Opção inválida")
