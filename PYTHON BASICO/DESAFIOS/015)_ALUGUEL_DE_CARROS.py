#========ALUGUEL DE CARROS:=============================================================

print("😎Considerando que que o carro custa R$60 por dia, mais R$0,15 por km rodado!")
dias = int(input("😎Quantos dias foi alugado?\n>>>"))
km = float(input("😎Quantos km você andou?\n>>>"))
pagar = (dias * 60) + (km * 0.15)
print("😎O total a pagar é R${:.2f}!".format(pagar))