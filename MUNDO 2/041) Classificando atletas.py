#==========CLASSIFICANDO ATLETAS:====================
from time import sleep
import datetime

atual = datetime.date.today().year
nascimento = int(input("😎Em que ano você nasceu?\n>>>"))
idade = atual - nascimento

print("⏳Processando...",end="\r")
sleep(3)

print("_" *35)
if idade <= 9:
    classificação = "😺MIRIM!"
elif idade <= 14:
    classificação = "🌜INFANTIL!"
elif idade <= 19:
    classificação = "🌞JUNIOR!"
elif idade <= 25:
    classificação = "😎SÊNIOR!"
else:
    classificação = "😠MASTER!"

print("⭐Para quem nasceu em {:.0f};\n⭐Tem {:.0f} anos;\n⭐CLASSIFICAÇÃO:{}!".format(nascimento, idade, classificação))
print("_" *35)