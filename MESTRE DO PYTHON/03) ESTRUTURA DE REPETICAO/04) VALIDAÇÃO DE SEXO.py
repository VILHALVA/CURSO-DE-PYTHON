sexo = input("😎Informe o seu sexo[M/F]:\n>>>").strip().upper()[0]
while sexo not in "MmFf":
    sexo = input("😠Dados inválidos!!!\n😬Por favor, informe seu sexo[M/F]:\n>>>").strip().upper()[0]
    if sexo in "Mm":
       sexo = "HOMEM"
       break
    if sexo in "Ff":
       sexo = "MULHER"
       break
print(f"🌝Isso significa que você é {sexo}!!!")