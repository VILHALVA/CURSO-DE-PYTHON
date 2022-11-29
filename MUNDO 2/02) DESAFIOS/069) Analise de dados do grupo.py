#===========ANÁLISE DE DADOS DO GRUPO:=========================
from time import sleep
tot18 = totM = totF20 = 0

while True:
    idade = int(input("😎Digite a idade:\n>>>"))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("😎Digite o sexo[M/F]:\n>>>")).strip().upper()[0]
    
    if idade >= 18:
        tot18 += 1
    if sexo == "M":
        totM += 1
    if sexo == "F" and idade < 20:
        totF20 += 1
        
    resp = " "
    while resp not in "SN":
        resp = str(input("😎Quer continuar?[S/N]\n>>>")).strip().upper()[0]
    if resp == "N":
        break

print("⌛Processando...",end="\r")
sleep(3)
print("_" *35)
print(f"⭐Temos {tot18} Pessoas com mais de 18!\n⭐Temos no total {totM} homens!\n⭐Temos {totF20} mulheres com menos de 20!")
print("_" *35)
