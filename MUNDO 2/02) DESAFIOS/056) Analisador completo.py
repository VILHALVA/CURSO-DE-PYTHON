#==========ANALISADOR COMPLETO:======================
somaridade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = ""
totmulher20 = 0

for p in range(1,5):
    print("--------{}° PESSOA: -----------".format(p))
    nome = str(input("😎Digite nome:\n>>>")).strip()
    idade = int(input("😎Digite a idade:\n>>>"))
    sexo = str(input("😎Digite sexo[M/F]:\n>>>")).strip()
    somaridade += idade
    if p == 1 and sexo in "Mm":
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Mn" and idade > maioridade:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Ff" and idade < 20:
        totmulher20 += 1

médiaidade = somaridade / 4

print("⭐A média de idade do grupo é de {} anos!\n⭐O homem mais velho tem {} anos e se chama {}!\n⭐Ao todo são {} mulheres com menos de 20 anos!".format(médiaidade, maioridadehomem, nomevelho, totmulher20))