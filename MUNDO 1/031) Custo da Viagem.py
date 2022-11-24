#=======CUSTO DA VIAGEM:=====================
distância = float(input("😎Qual é a distância da sua viagem(km)?\n>>>"))
preço = float(input("😎Qual é o preço por km?\n>>>"))

pagar = distância * preço

print("-" *35)
print("⭐Com a distância de {:.0f}km;\n⭐Preço por km sendo R${:.2f};\n⭐Valor a pagar é R${:.2f}!".format(distância, preço, pagar))
if pagar <= 200:
    print("😎MUITO BOM!!!")
else:
    print("💸QUE ABSURDO!!!")
print("-" *35)