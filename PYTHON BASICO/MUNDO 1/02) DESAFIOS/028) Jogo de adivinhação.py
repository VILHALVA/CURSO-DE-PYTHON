#==========JOGO DE ADIVINHAÇÃO:==========================
from time import sleep
from random import randint

print("-=-" *10)
print("😎Vou pensar em número entre 0 e 10. Tente adivinhar!!!")
print("-=-" *10)

computador = randint(0, 10) #>Faz o computador "PENSAR"

jogador = int(input("😎Em que número pensei?\n>>>")) #>Jogador tenta "ADVINHAR"
print("⏳Processando...",end="\r")
sleep(3)
if jogador == computador:
   print("😵PARABÉNS!!! Você acertou!!!")
else:
   print("😡VOCÊ PERDEU!!! O número é {}!!!".format(computador))
print("⛔GAME OVER.")
    