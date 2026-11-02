# EX7

usuario_correto = "admin"
senha_correta = 12345

usuario = input("Digite seu usuário: ")
senha = int(input("Digite sua senha: "))

if usuario == usuario_correto and senha == senha_correta:
    print("Usuário e senha corretos")
elif usuario == usuario_correto and senha != senha_correta:
    print("Usuário correto, senha errada")
elif usuario != usuario_correto and senha == senha_correta:
    print("Usuário errado, senha correta")
else:
    print("Usuário e senha errados")