#========CALCULADORA:===================

n1 = float(input("😎Digite o primeiro número:\n>>>"))
n2 = float(input("😎Digite o segundo número:\n>>>"))
sinal = str(input("😎Digite o sinal aritmético(+-×÷):\n>>>"))

if sinal == "+":
    print("➕{:.2f}!".format(n1+n2))
elif sinal == "-":
    print("➖{:.2f}!".format(n1-n2))
elif sinal == "×":
    print("✖️{:.2f}!".format(n1*n2))
elif sinal == "÷":
    print("➗{:.2f}!".format(n1/n2))
else:
    print("😠Sinal incorreto.Tente novamente!!!")