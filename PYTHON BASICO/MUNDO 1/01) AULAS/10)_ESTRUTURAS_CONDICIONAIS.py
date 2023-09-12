#========CONDIÇÕES:===============================
#----------IDADE DO CARRO:------------------------------
tempo = int(input("😎Quantos anos tem o seu carro?\n>>>"))
if tempo <=3:
    print("😵Seu carro é novo!!!")
else:
    print("😡Seu carro é velho!!!")
print("⛔FIM")


#---------SEU NOME:------------------------------------------
nome = str(input("😎Qual é o seu nome?\n>>>")).strip().upper()
if nome == "SAMUEL":
    print("😵Que nome lindo você tem!!!")
else:
    print("😡Que nome horrível!!!")
print("☀️Bom dia, {}!!!".format(nome))


#----------CALCULANDO A MÉDIA:---------------------------------------
n1 = float(input("😎Digite a primeira nota:\n>>>"))
n2 = float(input("😎Digite a segunda nota:\n>>>"))
m = (n1+n2)/2
print("⭐A sua média foi {:.1f}!!!".format(m))
if m >=7:
    print("😵Sua média foi boa! Parabéns!!!")
else:
    print("😡Sua média está horrível! Estude mais!!!")
