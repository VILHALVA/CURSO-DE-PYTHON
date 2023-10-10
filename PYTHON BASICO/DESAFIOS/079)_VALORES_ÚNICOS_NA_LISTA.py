#==========VALORES ÚNICOS NA LISTA:==============================
números = list()
while True:
    n = int(input("😎Digite um valor:\n>>>"))
    if n not in números:
        números.append(n)
        print("😠Valor adicionado com sucesso!!!")
    else:
        print("😬Valor duplicado!Não vou adicionar!")
        
    r = str(input("😎Quer continuar[S/N]?:\n>>>")).strip().upper()[0]
    if r in "Nn":
        break

print("_" *35)
números.sort()
print(f"⭐Você digitou os valores:\n⚡{números}")
print("_" *35)