#==========SENO, COSSENO E TANGENTE:==========================
from math import radians, sin, cos, tan
ângulo = float(input("😎Digite o valor que você deseja:\n>>>"))
seno = sin(radians(ângulo))
cosseno = cos(radians(ângulo))
tangente = tan(radians(ângulo))
print("⭐O ângulo de {}:\n⭐De seno tem {:.2f};\n⭐De cosseno é {:.2f}!\n⭐De Tangente {:.2f}!".format(ângulo, seno, cosseno, tangente))