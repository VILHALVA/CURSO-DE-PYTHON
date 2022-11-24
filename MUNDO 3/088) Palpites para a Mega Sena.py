#===========PALPITES PARA MEGA SENA:===============================
from time import sleep
from random import randint
lista = list()
jogos = list()

print("-" *30)
print("     JOGO DA MEGA SENA       ")
print ("-" *30)

quant = int(input("😎Quantos jogos você quer para ser sorteado?\n>>>"))
tot = 1
while tot <= quant:
    cont = 1
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 7:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print("-" *5, f"SORTEANDO {quant} JOGOS:", "-" *5)
print("_" *35)
for i, l in enumerate(jogos):
    print(f"⭐{i+1}ª JOGO: {l}")
    sleep(1)
print("_" *35)
print("-" *5, "  BOA SORTE!   ", "-" *5)
