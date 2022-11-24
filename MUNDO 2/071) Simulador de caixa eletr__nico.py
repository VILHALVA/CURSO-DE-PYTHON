#============SIMULADOR DE CAIXA ELETRÔNICO:=========================
from time import sleep

print("=" *30)
print("{:^10}".format("🏦BANCO CEV"))
print("=" *30)

valor = int(input("😎Digite o valor a sacar(R$):\n>>>"))
total = valor
céd = 50
totcéd = 0

print("⌛Processando...",end="\r") 
sleep(3)
print("💰" *20)

while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f"⭐Total de {totcéd} cédulas de R${céd}!")
        if céd == 200:
            céd = 100
        elif céd == 100:
            céd = 50
        elif céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 5
        elif céd == 5:
            céd = 2
        elif céd == 2:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print("💰" *20)

 