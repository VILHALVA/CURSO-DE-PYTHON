#=========ESTRUTURA DE REPETIÇÃO WHILE:=========================
c = 1
while c < 11:
    print(c)
    c = c + 1
print("STOP")

#============================================================================
r = "S"
while r == "S":
    n = int(input("😎Digite um valor:\n>>>"))
    r = str(input("😎Quer continuar[S/N]?\n>>>")).upper().strip()
print("STOP")

#======================================================================
n = 1
par = impar = 0
while n != 0:
    n = int(input("😎Digite um valor:\n>>>"))
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
print("⭐Você digitou {} n° pares e {} n° impares!".format(par, impar))