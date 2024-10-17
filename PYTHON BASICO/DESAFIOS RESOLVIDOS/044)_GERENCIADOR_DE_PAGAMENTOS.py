#==========GERENCIADOR DE PAGAMENTOS:==============================
print("{:=^40}".format(" LOGAS GUANABARA "))
preço = float(input("😎Digite o preço das compras(R$):\n>>>"))
print('''FORMAS DE PAGAMENTO:
[ 1 ] À vista dinheiro/Cheque;
[ 2 ] À vista no cartão;
[ 3 ] 2× no cartão;
[ 4 ] 3× ou mais no cartão.''')
opção = int(input("😎Qual é a sua opção?:\n>>>"))


if opção == 1:
    total = preço - (preço * 10 / 100)
    print("_" *35)
elif opção == 2:
    total = preço - (preço * 5 / 100)
    print("_" *35)
elif opção == 3:
    total = preço
    parcela = total / 2
    print("_" *35)
    print("⭐Será parcelada em 2× de R${:.2f}!".format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input("😎Quantas parcelas?\n>>>"))
    parcela = total / totparc
    print("_" *35)
    print("⭐Será parcelada em {:.0f}×;\n⭐No valor de R${:.2f}!".format(totparc, parcela))
else:
    total = preço
    print("_" *35)
    print("😠Valor inválido! Tente novamente!")  
    
print("⭐Sua compra de R${:.2f}!\n⭐Vai custar R${:.2f}!".format(preço, total))
print("_" *35)