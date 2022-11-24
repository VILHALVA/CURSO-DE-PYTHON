#=========INTERROMPENDO REPETIÇÕES WHILE:==============================
cont = 1
while cont <= 10:
    print(cont,"»", end="")
    cont += 1
print("⛔FIM!!!")

#======================================{={
n = s = cont = 0
while True:
    n = int(input("😎Digite um número!!!\n⭐Envie 999 caso queira parar:\n>>>"))
    if n == 999:
        break
    cont += 1
    s += n

#////////////print("⭐Foram {} valores!!!\n⭐A soma Vale: {}!!!".format(cont, s)) #<🔔Essa é antiga formatação do Python 3.6!!!
print(f"⭐Foram {cont} valores!!!\n⭐A soma vale: {s}!!!") #<🔔Essa é a nova formação do Python 3.7!!!

#⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬
nome = str(input("😎Digite o seu nome:\n>>>"))
idade = int(input("😎Digite a sua idade:\n>>>"))

print("⭐Seu nome é %s!!!\n⭐Sua idade é %d!!!" % (nome, idade)) #>PYTHON 2!!!
print("⭐Seu nome é {}!!!\n⭐Sua idade {}!!!".format(nome, idade)) #>PYTHON 3.6+
print(f"⭐Seu nome é {nome}!!!\n⭐Sua idade é {idade}!!!") #>PYTHON 3.7+

    
