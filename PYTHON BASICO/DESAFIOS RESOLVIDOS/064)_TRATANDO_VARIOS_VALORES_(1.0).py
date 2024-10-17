#========TRATANDO VÁRIOS VALORES:==============================

num = cont = soma = 0
num = int(input("😎Digite 999 para PARAR:\n>>>"))

while num != 999:
    soma += num
    cont += 1
    num = int(input("😠Valor inválido!!!Tente novamente:\n>>>"))
    
print("_" *35)
print("👏PARABÉNS!!!\n🌚VOCÊ CONSEGUIU!!!\n⭐Você digitou {} números!!!\n⭐A soma entre eles foi {}!\n⛔FIM!!!".format(cont, soma))
print("_" *35)