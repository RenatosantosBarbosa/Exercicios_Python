#EX1

# nota = float(input("Digite a sua nota (0 a 10): "))

# if nota < 0 or nota > 10:
#     print("Nota inválida")
# elif nota >= 7:
#     print("Aprovado")
# elif nota >= 5:
#     print("Recuperação")
# else:
#     print("Reprovado")

#EX2

# idade = int(input("Digite sua idade: "))

# if idade < 0:
#     print("Idade Invalida")
# elif idade <= 12:
#     print("Criança")
# elif idade <= 17:
#     print("Adolescente")
# elif idade <= 59:
#     print("Adulto")
# else:
#     print("Idoso")

#EX3

# num1 = float(input("Digite o primeiro numero: "))
# num2 = float(input("Digite o segundo numero: "))
# num3 = float(input("Digite o terceiro numero: "))

# if num1 == num2 == num3:
#     print("Todos os numeros são iguais")
# elif num1 >= num2 and num1 >= num3:
#     print(f"O maior numero é {num1}")
#     if num1 == num2 or num1 == num3:
#         print("Há empate no maior valor.")
# elif num2 >= num1 and num2 >= num3:
#     print(f"O maior numero é {num2}")
#     if num2 == num1 or num2 == num3:
#         print("Há empate no maior valor.")
# else:
#     print(f"O maior numero é {num3}")
#     if num3 == num1 or num3 == num2:
#         print("Há empate no maior valor.")

#EX4

# valor_compra = float(input("Digite o valor da compra: "))

# if valor_compra <= 100:
#     desconto = 0
# elif valor_compra <= 300:
#     desconto = valor_compra * 0.10
# elif valor_compra <= 500:
#     desconto = valor_compra * 0.15
# else:
#     desconto = valor_compra * 0.20

# valor_final = valor_compra - desconto

# print(f"Desconto: R$ {desconto:.2f}")
# print(f"Valor final: R$ {valor_final:.2f}")

#EX5

# velocidade = float(input("Digite a velocidade do veiculo: "))

# if velocidade <= 60:
#     print("Dentro do limite")
# elif velocidade <= 80:
#     print("Multa leve")
# elif velocidade <= 100:
#     print("Multa media")
# else:
#     print("Multa grave")

#EX6

# peso = float(input("Qual seu peso?: "))
# altura = float(input("Qual sua altura: "))

# imc = peso / (altura ** 2)

# if imc < 18.5:
#     print("Abaixo do peso")
# elif imc <= 24.9:
#     print("Normal")
# elif imc <= 29.9:
#     print("Sobrepeso")
# else:
#     print("Obesidade")

#EX7

# usuario_correto = "admin"
# senha_correta = 12345

# usuario = input("Digite seu usuario: ")
# senha = int(input("Digite sua senha: "))

# if usuario == usuario_correto and senha == senha_correta:
#     print("Usuario e senha corretos")
# elif usuario == usuario_correto and senha != senha_correta:
#     print("Usuario correto, senha errada")
# elif usuario != usuario_correto and senha == senha_correta:
#     print("Usuario errado, senha correta")
# else:
#     print("Usuario e senha errados")

#EX8

# saldo = float(input("Digite seu saldo: "))
# saque = float(input("Digite o valor que deseja sacar: "))

# if saque <= 0:
#     print("Valor invalido")
# elif saldo >= saque:
#     print("Saque autorizado")
# else:
#     print("Saque negado, saldo insuficiente")

#EX9

# print("-------MENU------- \n 1 - Cadastrar \n 2 - Consultar \n 3 - Editar \n 4 - Excluir \n 5 - Sair")

# opcao = int(input("Escolha uma opção: "))

# match opcao:
#     case 1:
#         print("Cadastrar selecionado")
#     case 2:
#         print("Consultar selecionado")
#     case 3:
#         print("Editar selecionado")
#     case 4:
#         print("Excluir selecionado")
#     case 5:
#         print("Sair selecionado")
#     case _:
#         print("Opção invalida")

#EX10

# dia = int(input("Digite um numero (1 a 7): "))

# match dia:
#     case 1:
#         print("Domingo")
#     case 2:
#         print("Segunda-feira")
#     case 3:
#         print("Terça-feira")
#     case 4:
#         print("Quarta-feira")
#     case 5:
#         print("Quinta-feira")
#     case 6:
#         print("Sexta-feira")
#     case 7:
#         print("Sabado")
#     case _:
#         print("Numero invalido")

#EX11

# mes = int(input("Digite um numero (1 a 12): "))

# match mes:
#     case 1:
#         print("Janeiro")
#     case 2:
#         print("Fevereiro")
#     case 3:
#         print("Março")
#     case 4:
#         print("Abril")
#     case 5:
#         print("Maio")
#     case 6:
#         print("Junho")
#     case 7:
#         print("Julho")
#     case 8:
#         print("Agosto")
#     case 9:
#         print("Setembro")
#     case 10:
#         print("Outubro")
#     case 11:
#         print("Novembro")
#     case 12:
#         print("Dezembro")
#     case _:
#         print("Numero invalido")

#EX12

# num1 = float(input("Digite um numero: "))
# num2 = float(input("Digite outro numero: "))
# operacao = input("Operação (+, -, *, /): ")

# match operacao:
#     case "+":
#         print(num1 + num2)
#     case "-":
#         print(num1 - num2)
#     case "*":
#         print(num1 * num2)
#     case "/":
#         if num2 == 0:
#             print("Não é possivel dividir por zero.")
#         else:
#             print(num1 / num2)
#     case _:
#         print("Operação invalida")

#EX13

# print("------MENU------ \n1 - Celsius > Fahrenheit \n2 - Fahrenheit > Celsius \n3 - Metros > Quilômetros \n4 - Quilômetros > Metros")
# opcao = int(input("Escolha uma opção: "))

# match opcao:
#     case 1:
#         temp_celsius = float(input("Digite a temperatura: "))
#         fahrenheit = (temp_celsius * 9/5) + 32
#         print(f"{temp_celsius:.2f} Graus celsius convertido é {fahrenheit:.2f} graus fahrenheit")
#     case 2:
#         temp_fahrenheit = float(input("Digite a temperatura: "))
#         celsius = (temp_fahrenheit - 32) * 5/9
#         print(f"{temp_fahrenheit:.2f} Graus fahrenheit convertido é {celsius:.2f} graus celsius")
#     case 3:
#         metros = float(input("Digite o valor em metros: "))
#         mt_conv = metros / 1000
#         print(f"{metros:.2f} metros são {mt_conv:.2f} quilômetros")
#     case 4:
#         quilometros = float(input("Digite o valor em quilômetros: "))
#         km_conv = quilometros * 1000
#         print(f"{quilometros:.2f} em metros são {km_conv:.2f} metros")
#     case _:
#         print("Opção invalida")
    

#EX14

# print("--ESCOLHA-DE-PERSONAGEM-- \n1 - Guerreiro \n2 - Mago \n3 - Arqueiro \n4 - Assassino")
# opcao = int(input("Escolha a classe do personagem: "))

# match opcao:
#     case 1:
#         print("Guerreiro")
#         print("Vida: 100")
#         print("Ataque: 90")
#         print("Defesa: 100")
#     case 2:
#         print("Mago")
#         print("Vida: 100")
#         print("Ataque: 90")
#         print("Defesa: 90")
#     case 3:
#         print("Arqueiro")
#         print("Vida: 100")
#         print("Ataque: 90")
#         print("Defesa: 80")
#     case 4:
#         print("Assassino")
#         print("Vida: 100")
#         print("Ataque: 100")
#         print("Defesa: 90")
#     case _:
#         print("Opção invalida")

#EX15

# nome = input("Digite o nome do aluno: ")
# idade = int(input("Digite a idade do aluno: "))

# nota1 = float(input("Nota 1: "))
# nota2 = float(input("Nota 2: "))
# nota3 = float(input("Nota 3: "))

# media = (nota1 + nota2 + nota3) / 3

# if media >= 7:
#     situacao = "Aprovado"
# elif media >= 5:
#     situacao = "Recuperação"
# else:
#     situacao = "Reprovado"

# print(f"\nNome: {nome}")
# print(f"Idade: {idade}")
# print(f"Media: {media:.2f}")
# print(f"Situação: {situacao}")

#EX16

