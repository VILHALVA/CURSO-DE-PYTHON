#===========GRUPO DE MAIORIDADE:====================================
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0

for pess in range(1, 8):
    nasc = int(input("😎Em que ano {}° a pessoa nasceu?\n>>>".format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print("⭐Ao todo tivemos {} pessoas de MAIOR!\n⭐As de MENOR são {}!".format(totmaior, totmenor))
