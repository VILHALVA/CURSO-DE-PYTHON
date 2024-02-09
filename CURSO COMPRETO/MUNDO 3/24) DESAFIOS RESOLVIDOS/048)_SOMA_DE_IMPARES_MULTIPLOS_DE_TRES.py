#==============SOMA ÍMPARES MÚLTIPLOS DE TRÊS:===============================
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print("⭐A soma de todos os {} valor solicitados é {}!".format(cont, soma))
