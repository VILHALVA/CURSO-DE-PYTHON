from random import randint
from time import sleep

computador = randint(0,10)
print("😠Acabei de pensar em um número entre 0 e 10!")
sleep(2)

acertou = False
palpites = 0

while not acertou:
    jogador = int(input("😎Qual é o seu palpite:\n>>>"))
    palpites += 1
    if jogador == computador:
        acertou = True
        resultado = "👍ACERTOU com {} Tentativas!".format(palpites)
    else:
        if jogador < computador:
            print("👎ERRADO!!!➕VALOR É MAIOR QUÊ {}!!!".format(jogador))
        elif jogador > computador:
            print("👎ERRADO!!!➖VALOR É MENOR QUÊ {}!!!".format(jogador))
            
print("_" *35)
print("⭐Eu pensei no n°{}!\n⭐Você digitou:{}!\n⭐RESULTADO:{}".format(computador, jogador, resultado))
print("_" *35)
