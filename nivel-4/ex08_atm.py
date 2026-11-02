# EX8

saldo = float(input("Digite seu saldo: "))
saque = float(input("Digite o valor que deseja sacar: "))

if saque <= 0:
    print("Valor inválido")
elif saldo >= saque:
    print("Saque autorizado")
else:
    print("Saque negado, saldo insuficiente")