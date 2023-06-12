#==============LISTA COMPOSTA E ANÁLISE DE DADOS:===================================
temp = []
princ = []
mai = men = 0

while True:
    temp.append(str(input("😎Digite o nome:\n>>>")))
    temp.append(float(input("😎Digite o peso:\n>>>")))
    if len(princ) == 0:
        mai = men = temp[1]
    else: 
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
        
    resp = str(input("⚡Você quer continuar?\n>>>")).strip().upper()[0]
    princ.append(temp[:])
    temp.clear()
    if resp in "Nn":
        break
for p in princ:
    if p[1] == mai:
        maior = p[0]
    if p[1] == men:
        menor = p[0]

print("_" *30)
print(f"⭐Os dados foram:\n⚡{princ}\n⭐Você cadastrou:\n⚡{len(princ)} pessoas!\n⭐Os mais pesado foi:\n⚡{maior}\n⭐O maior peso foi:\n⚡{mai} kg\n⭐O menos pesado foi:\n⚡{menor}\n⭐O menor peso foi:\n⚡{men} kg")
print("_" *30)