#=========MAIOR E MENOR VALOR DA LISTA:===============================

listanum = []
menor = maior = 0

for c in range(0,5):
    listanum.append(int(input(f"😎Digite um valor para a posição {c}:\n>>>")))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
            
for i, v in enumerate(listanum):
    if v == maior:
        vm = f"{i}"
               
print("_" *35)
print(f"⭐Você digitou os valores {listanum}!\n⭐Maior valor foi {maior}!\n⚡Na posição: {vm}!\n⭐Menor valor foi {menor}!\n⚡Na posição:{vm}!")
print("_" *35)

for i, v in enumerate(listanum):
    if v == menor:
        vm = f"{i}"