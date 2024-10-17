#============BOLETIM COM LISTAS COMPOSTAS:===================================
from time import sleep

ficha = list()
while True:
    nome = str(input("😎Digite o nome:\n>>>")).strip()
    nota1 = float(input("😎Digite nota 1:\n>>>"))
    nota2 = float(input("😎Digite nota 2: \n>>>"))
    média = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], média])
    resp = str(input("😎Você quer continuar[S/N]?\n>>>")).strip().upper()[0]
    if resp in "Nn":
        break
print("_" *35)
print(f"{'Nª':<4}{'NOME':<10}{'MEDIA':>8}")
print("-" *30)
for i, a in enumerate(ficha):
    print(f"{i:<4}{a[0]:<10}{a[2]:8.1f}")
    print("-" *30)
print("_" *35)

while True:
    opc = int(input("😎Você quer mostar as notas de quem?\n⚡Envie 999 para interromper:\n>>>"))
    if opc == 999:
        for c in range(0, 125, 25): 
            print(f"⌛finalizando({c})%...",end="\r")
            sleep(1)
        print("\n⛔FIM")
        break
    if opc <= len(ficha) -1:
        print(f"⭐Notas de {ficha[opc][0]} são {ficha[opc][1]}")
print("<<< 😬ATÉ NUNCA MAIS!!! >>>")

