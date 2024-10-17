from random import randint

print("-=-" *10)
print("😎Vou pensar em número entre 0 e 10. Tente adivinhar!!!")
print("-=-" *10)
computador = randint(0, 10)

jogador = int(input("😎Em que número pensei?\n>>>"))
if jogador == computador:
   print("😵PARABÉNS!!! Você acertou!!!")
else:
   print("😡VOCÊ PERDEU!!! O número é {}!!!".format(computador))
print("⛔GAME OVER.")