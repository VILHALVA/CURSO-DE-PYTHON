#=========AUMENTOS MÚLTIPLOS:======================================
salário = float(input("😎Qual é o salário do funcionário:\n>>>"))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
    aumento = 15
else:
    novo = salário + (salário * 10 / 100)
    aumento = 10

print("-" *35)
print("⭐Quem ganhava: R${:.2f};\n⭐Com aumento de {:.0f}%;\n⭐Passa a ganhar: R${:.2f}".format(salário, aumento, novo))
print("-" *35)