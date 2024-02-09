#==========PROGRESSÃO ARITMÉTICA (2.0):==============================
n = int(input("😎Digite o número:\n>>>"))
r = int(input("😎Digite a razão:\n>>>"))

termo = n
cont = 1

while cont <= 10:
    print("›{}".format(termo), end = "")
    termo += r
    cont += 1
print("\n⛔FIM!!!")