# EX14

print("-- ESCOLHA DE PERSONAGEM --")
print("1 - Guerreiro")
print("2 - Mago")
print("3 - Arqueiro")
print("4 - Assassino")

opcao = int(input("Escolha a classe do personagem: "))

match opcao:
    case 1:
        print("Guerreiro")
        print("Vida: 100")
        print("Ataque: 90")
        print("Defesa: 100")

    case 2:
        print("Mago")
        print("Vida: 100")
        print("Ataque: 90")
        print("Defesa: 90")

    case 3:
        print("Arqueiro")
        print("Vida: 100")
        print("Ataque: 90")
        print("Defesa: 80")

    case 4:
        print("Assassino")
        print("Vida: 100")
        print("Ataque: 100")
        print("Defesa: 90")

    case _:
        print("Opção inválida")