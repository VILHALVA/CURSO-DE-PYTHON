#=======RADAR ELETRÔNICO:=========================
from time import sleep

velocidade = float(input("😎Qual é a velocidade do seu carro?\n>>>"))
limite = float(input("😎Qual é o limite de velocidade?\n>>>"))
print("⏳Processando...",end="\r")
sleep(3)
if velocidade > limite:
    print("😡MULTADO! Você excedeu o limite permitido; Que é {:.2f}km/h!!!".format(limite))
    sleep(2)
    valor = float(input("😤Para saber quanto você deve pagar, digite o valor da multa(R$) por cada km acima do limite:\n>>>"))
    multa = (velocidade-limite)*valor
    print("⏳Processando...",end="\r")
    sleep(3)
    print("-" *35)
    print("⭐Com velocidade do carro: {:.0f}km/h;\n⭐Sendo o limite de {:.0f}km/h;\n⭐Valor da multa por km é: R${:.2f};\n⭐Valor a pagar é: R${:.2f}!!!".format(velocidade, limite, valor, multa))
    print("-" *35)
    sleep(2)
else:
    print("😎PARABÉNS!!! Você não excedeu o limite de velocidade!!!")
    sleep(2)
print("😎Desejo boa sorte!!!")
    