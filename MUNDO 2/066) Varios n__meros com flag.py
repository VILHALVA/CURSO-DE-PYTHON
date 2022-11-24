#==========VÁRIOS NÚMEROS COM FLAG:==========================
n = s = cont = 0
while True:
    n = int(input("😎Digite um número!!!\n⭐Envie 999 caso queira parar:\n>>>"))
    if n == 999:
        break
    cont += 1
    s += n

print(f"⭐Foram {cont} valores!!!\n⭐A soma vale: {s}!!!")
