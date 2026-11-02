# EX6

peso = float(input("Qual seu peso?: "))
altura = float(input("Qual sua altura?: "))

if peso <= 0 or altura <= 0:
    print("Peso ou altura inválidos")
else:
    imc = peso / (altura ** 2)

    if imc < 18.5:
        print("Abaixo do peso")
    elif imc <= 24.9:
        print("Normal")
    elif imc <= 29.9:
        print("Sobrepeso")
    else:
        print("Obesidade")