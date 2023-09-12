#==========MÉDIA ARITMÉTICA:====================================

import time

n1 = float(input("😎Digite a sua primeira nota:\n>>>"))
n2 = float(input("😎Digite a sua segunda nota:\n>>>"))
m = (n1+n2)/2.

print("⏳Processando...",end="\r")
time.sleep(3)
print("😎A média entre {:.1f} e {:.1f} é igual {:.1f}.".format(n1, n2, m))
time.sleep(2)

if 7 > m >=5:
    print("⭐Você está reprovado!!!")
else:
    print("⭐Você está aprovado!!!")