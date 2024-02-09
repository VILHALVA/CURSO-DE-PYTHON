#==========EXTRAINDO DADOS DA LISTA:==============================
valores = []

while True:
    valores.append(int(input("😎Digite um valor:\n>>>")))
    resp = str(input("😎Quer continuar[S/N]?:\n>>>")).strip().upper()[0]
    
    if 5 in valores:
        cinco = "👍SIM"
    else:
        cinco = "👎NÃO"
        
    if resp in "Nn":
        break

print("_" *35)
valores.sort(reverse=True)
print(f"⭐Você digitou: {len(valores)} valores!\n⭐Na ordem decrescente são:\n⚡{valores}!\n⭐Temos o número 5?: {cinco}")
print("_" *35)