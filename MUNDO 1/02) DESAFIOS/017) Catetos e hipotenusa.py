#==========CATETOS E HIPOTENUSA: ======================
CO = float(input("😠Digite o comprimento do cateto oposto:\n>>>"))
CA = float(input("😠Digite o complemento do cateto adjacente:\n>>>"))
HP = (CO**2 + CA**2) ** (1/2)
print("⭐A hipotenusa mede {:.2f}!".format(HP))

#==========OU:=========================================================
from math import hypot
CO = float(input("😠Digite o comprimento do cateto oposto:\n>>>"))
CA = float(input("😠Digite o complemento do cateto adjacente:\n>>>"))
HP = hypot(CO, CA)
print("⭐A hipotenusa mede {:.2f}!".format(HP))
