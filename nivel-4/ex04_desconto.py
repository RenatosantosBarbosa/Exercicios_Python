# EX4 

valor_compra = float(input("Digite o valor da compra: "))

if valor_compra <= 100:
    desconto = 0
elif valor_compra <= 300:
    desconto = valor_compra * 0.10
elif valor_compra <= 500:
    desconto = valor_compra * 0.15
else:
    desconto = valor_compra * 0.20

valor_final = valor_compra - desconto

print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor final: R$ {valor_final:.2f}")