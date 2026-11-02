# EX12

num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
operacao = input("Operação (+, -, *, /): ")

match operacao:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        if num2 == 0:
            print("Não é possível dividir por zero.")
        else:
            print(num1 / num2)
    case _:
        print("Operação inválida")