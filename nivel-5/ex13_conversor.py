# EX13

print("------ MENU ------")
print("1 - Celsius > Fahrenheit")
print("2 - Fahrenheit > Celsius")
print("3 - Metros > Quilômetros")
print("4 - Quilômetros > Metros")

opcao = int(input("Escolha uma opção: "))

match opcao:
    case 1:
        temp_celsius = float(input("Digite a temperatura: "))
        fahrenheit = (temp_celsius * 9 / 5) + 32
        print(
            f"{temp_celsius:.2f} graus Celsius = "
            f"{fahrenheit:.2f} graus Fahrenheit"
        )

    case 2:
        temp_fahrenheit = float(input("Digite a temperatura: "))
        celsius = (temp_fahrenheit - 32) * 5 / 9
        print(
            f"{temp_fahrenheit:.2f} graus Fahrenheit = "
            f"{celsius:.2f} graus Celsius"
        )

    case 3:
        metros = float(input("Digite o valor em metros: "))
        quilometros = metros / 1000
        print(f"{metros:.2f} metros = {quilometros:.2f} quilômetros")

    case 4:
        quilometros = float(input("Digite o valor em quilômetros: "))
        metros = quilometros * 1000
        print(f"{quilometros:.2f} quilômetros = {metros:.2f} metros")

    case _:
        print("Opção inválida")