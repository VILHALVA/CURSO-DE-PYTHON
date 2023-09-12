#==========VALIDAÇÃO DE DADOS:===============================

sexo = str(input("😎Informe o seu sexo[M/F]:\n>>>")).strip().upper()[0]
while sexo not in "MmFf":
     sexo = str(input("😠Dados inválidos. Por favor, informe seu sexo[M/F]:\n>>>")).strip().upper()[0]
if sexo == "M":
    sexo = "MASCULINO"
if sexo == "F":
    sexo = "FEMININO"
print("⭐Sexo {} registrado com sucesso!!!".format(sexo))