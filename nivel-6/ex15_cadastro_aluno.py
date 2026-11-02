# EX15

nome = input("Digite o nome do aluno: ")
idade = int(input("Digite a idade do aluno: "))

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    situacao = "Aprovado"
elif media >= 5:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

print(f"\nNome: {nome}")
print(f"Idade: {idade}")
print(f"Média: {media:.2f}")
print(f"Situação: {situacao}")