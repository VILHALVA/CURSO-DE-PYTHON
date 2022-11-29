#==============LISTA DE PREÇOS EM TUPLAS:================================

listagem = ("Lápis", 1.75,
            "Borracha", 2.00,
            "Caderno", 15.90,
            "Estojo", 25.00,
            "Transferidor", 4.20,
            "Compasso", 9.90,
            "Mochila", 120.32,
            "Canetas", 22.30,
            "Livros", 34.90)

print("_" *30)
print(f"{'LISTAGEM DE PREÇOS:':^30}")
print("_" *30)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f"{listagem[pos]:.<15}",end=" ")
    else:
        print(f"R${listagem[pos]:.>3.2f}")
        
print("_" *30)