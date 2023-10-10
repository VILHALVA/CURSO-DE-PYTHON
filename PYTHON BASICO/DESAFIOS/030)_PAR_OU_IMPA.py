#==========PAR OU IMPAR:=============================
número = int(input("😎Digite um número qualquer:\n>>>"))
resultado = número % 2
if resultado == 0:
    print("😎O número {} é PAR!".format(número))
elif resultado == 1:
    print("😎O número {} é IMPAR!".format(número))