#========LISTAS COM PARES E ÍMPARES:==================================
num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f"😎Digite o [{c}ª/7ª] valor:\n>>>"))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

num[0].sort()
num[1].sort()
print("_" *30)
print(f"⭐Os valores Pares:\n⚡{num[0]}\n⭐Valores Ímpares:\n⚡{num[1]}")
print("_" *30)