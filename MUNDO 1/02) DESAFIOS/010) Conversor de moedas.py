#========== CONVERSOR DE MOEDAS: =========================

real = float(input("😎Quanto você tem na carteira(R$)?\n>>>"))
dolar = real / 3.27
print("Com R${:.2f} você pode comprar US${:.2f}".format(real, dolar))