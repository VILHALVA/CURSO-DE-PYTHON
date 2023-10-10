#==========MAIOR OU MENOR DA SEQUÊNCIA:======================================
maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input("😎Digite o peso da {}° Pessoa:\n>>>".format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print("⭐O maior peso lido foi de {}kg".format(maior))
print("⭐O menor peso lido foi de {}km!".format(menor))