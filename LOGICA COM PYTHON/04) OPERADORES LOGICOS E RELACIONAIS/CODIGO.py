# Simulação de um sistema de login

# Definindo nome de usuário e senha corretos
usuario_correto = "usuario123"
senha_correta = "senha123"

# Solicitando nome de usuário e senha ao usuário
nome_usuario = input("Digite seu nome de usuário: ")
senha = input("Digite sua senha: ")

# Verificando se as credenciais fornecidas estão corretas
if nome_usuario == usuario_correto and senha == senha_correta:
    print("Login bem-sucedido! Bem-vindo,", nome_usuario)
else:
    print("Credenciais inválidas. Verifique seu nome de usuário e senha.")
