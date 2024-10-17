#==========TABUADA 2.0:====================================
num = int(input("😎Digite o número para ver a sua tabuada:\n>>>"))
opr = str(input("😎Digite operador:\n>>>"))

for c in range(1, 11):
    if opr == "×":
        print("{} × {:2} = {}".format(num, c, num*c))
    elif opr == "+":
        print("{} + {:2} = {}".format(num, c, num+c))
    elif opr == "÷":
        print("{} ÷ {:2} = {}".format(num, c, num/c))
    elif opr == "-":
        print("{} - {:2} = {}".format(num, c, num-c))