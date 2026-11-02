# EX5

velocidade = float(input("Digite a velocidade do veículo: "))

if velocidade < 0:
    print("Velocidade inválida")
elif velocidade <= 60:
    print("Dentro do limite")
elif velocidade <= 80:
    print("Multa leve")
elif velocidade <= 100:
    print("Multa média")
else:
    print("Multa grave")