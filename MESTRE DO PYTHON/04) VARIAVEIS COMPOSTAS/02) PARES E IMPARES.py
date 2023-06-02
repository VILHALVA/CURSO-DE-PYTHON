#========= [ 04 ] VARIAVEL COMPOSTA: LISTA ==================

VALOR = [[], []]
cont = 1
while True:
    num = int(input(f"😎Digite o {cont}ª valor:\n>>>"))
    cont += 1
    if num % 2 == 0:
        VALOR[0].append(num)
    elif num % 2 == 1:
        VALOR[1].append(num)
    res = str(input(f"😠Voce quer digitar o {cont}ª valor?[S/N]:\n>>>")).strip().upper()[0]
    if res in "Ss":
        continue
    elif res in "Nn":
        break
    else:
        print("⛔Não compreendo...")

VALOR[0].sort()
VALOR[1].sort()
print(f"⭐Analisando {cont} valores:\n⚡PARES: {VALOR[0]}\n⚡IMPARES: {VALOR[1]}")