#=========MAIOR E MENOR VALORES:==============================
resp = "S"
soma = quant = média = maior = menor = 0

while resp in "Ss":
    num = int(input("😎Digite valor:\n>>>"))
    soma += num
    quant += 1
    
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resp = str(input("😎Deseja continuar?[S/N]:\n>>>")).upper().strip()[0]
média = soma / quant

print("_" *35)
print("⭐Você digitou {} números!\n⭐A média foi {:.2f}!\n⭐Maior valor foi {}!\n⭐Menor valor foi {}!".format(quant, média, maior, menor))
print("_" *35)
print("⛔FIM!!!")