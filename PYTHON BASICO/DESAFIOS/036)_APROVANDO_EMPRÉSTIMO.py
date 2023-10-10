#=========APROVANDO EMPRÉSTIMO:==========================
casa = float(input("😎Qual é o valor da casa(R$)?\n>>>"))
salário = float(input("😎Qual é o valor do seu salário(R$)?\n>>>"))
anos = int(input("😎Quantos anos de financiamento?\n>>>"))

prestação = casa / (anos * 12)
mínimo = salário * 30 / 100

print("_" *30)
if prestação <= mínimo:
    resultado = "👍APROVADO"
else:
    resultado = "👎NEGADO" 
    
print("⭐Pagar uma casa de R${:.2f};\n⭐Com salário de R${:.2f};\n⭐Em {} anos;\n⭐Prestação será de R${:.2f};\n⭐Valor mínimo R${:.2f};\n⭐EMPRÉSTIMO:{}!".format(casa, salário, anos, prestação, mínimo, resultado))
print("_" *30)