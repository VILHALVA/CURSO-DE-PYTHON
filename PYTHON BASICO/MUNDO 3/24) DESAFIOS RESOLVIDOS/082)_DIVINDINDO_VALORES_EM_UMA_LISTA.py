#===========DIVIDINDO VALORES EM VÁRIAS LISTAS:=================================
valores = list()
pares = list()
ímpares = list()

while True:
    valores.append(int(input("😎Digite um número:\n>>>")))
    resp = str(input("😎Você quer continuar[S/N]?\n>>>")).strip().upper()[0]
    
    if resp in "Nn":
        break
   
for i, v in enumerate(valores):
    if v % 2 == 0:
        pares.append(v)
    else:
        ímpares.append(v)

print("_" *35)
print(f"⭐A lista completa é:\n⚡{valores}\n⭐A lista de pares é:\n⚡{pares}\n⭐A lista de ímpares é:\n⚡{ímpares}")
print("_" *35)
