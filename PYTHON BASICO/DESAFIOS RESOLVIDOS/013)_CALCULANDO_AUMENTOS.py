#==========CALCULANDO AUMENTOS: ================
import time

preço = float(input("😎Digite o seu preço atual(R$):\n>>>"))
aumento = float(input("😎Digite o seu aumento(%):\n>>>"))
pagar = preço + (preço * aumento /100)

print("⏳Processando...",end="\r")
time.sleep(3)
print("⭐O preço atual é R${:.2f};\n⭐Com aumento de {:.0f}%;\n⭐O valor a pagar é R${:.2f}!".format(preço, aumento, pagar))