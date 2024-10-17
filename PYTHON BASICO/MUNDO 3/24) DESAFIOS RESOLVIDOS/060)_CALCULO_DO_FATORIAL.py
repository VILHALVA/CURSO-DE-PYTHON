#===========CÁLCULO DO FATORIAL:============================
from math import factorial

n = int(input("😎Digite o valor; Para fazer o cálculo fatorial:\n>>>"))
f = factorial(n)
print("⭐O factorial de {} é {}!".format(n, f))

#============OU:=======================================================
n = int(input("😎Digite o valor:\n>>>"))
c = n
f = 1
print("⭐Calculando {}!=".format(n), end = "")
while c > 0:
    print("{}".format(c), end= "")
    print("×" if c > 1 else "=", end = "")
    f *= c
    c -= 1
print("{}.".format(f))
