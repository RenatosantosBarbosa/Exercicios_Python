# EX3

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if num1 == num2 == num3:
    print("Todos os números são iguais")
elif num1 >= num2 and num1 >= num3:
    print(f"O maior número é {num1}")
    if num1 == num2 or num1 == num3:
        print("Há empate no maior valor.")
elif num2 >= num1 and num2 >= num3:
    print(f"O maior número é {num2}")
    if num2 == num1 or num2 == num3:
        print("Há empate no maior valor.")
else:
    print(f"O maior número é {num3}")
    if num3 == num1 or num3 == num2:
        print("Há empate no maior valor.")