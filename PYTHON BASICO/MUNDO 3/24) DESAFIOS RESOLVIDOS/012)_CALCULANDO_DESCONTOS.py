#===== CALCULANDO DESCONTOS: =============
import time

preço = float(input("😎Digite o seu preço(R$):\n>>>"))
porcentagem = float(input("😎Digite a sua porcentagem(%):\n>>>"))

pagar = preço - (preço * porcentagem /100)

print("⏳Processando...",end="\r")
time.sleep(3)

print("⭐Preço de R${:.2f};\n⭐Com desconto de {:.0f}%;\n⭐Valor a pagar é {:.2f}!".format(preço, porcentagem, pagar))
exit()