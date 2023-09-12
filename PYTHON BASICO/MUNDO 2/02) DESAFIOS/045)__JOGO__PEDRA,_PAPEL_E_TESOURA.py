#======JOGO: PEDRA PAPEL E TESOURA:================================
from random import randint

itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0, 2)

print(''' OPÇÕES:
[ 0 ] PEDRA;
[ 1 ] PAPEL;
[ 2 ] TESOURA.''')


jogador = int(input("😎Escolha a sua opção:\n>>>"))
print("_" *35)

if computador == 0:
    if jogador == 0:
        resultado = "🔔EMPATE!"
    elif jogador == 1:
        resultado = "👎VOCÊ PERDEU!"
    elif jogador == 2:
        resultado = "👎VOCÊ PERDEU!"
    else:
        resultado = "⛔JOGADA INVÁLIDA!!!"
        
elif computador == 1:
    if jogador == 0:
        resultado = "👍VOCÊ VENCEU!"
    elif jogador == 1:
        resultado = "🔔EMPATE!"
    elif jogador == 2:
        resultado = "👍VOCÊ VENCEU!"
    else:
        resultado = "⛔JOGADA INVÁLIDA!!!"
        
elif computador == 2:
    if jogador == 0:
        resultado = "👍VOCÊ VENCEU!"
    elif jogador == 1:
        resultado = "👎VOCÊ PERDEU!"
    elif jogador == 2:
        resultado = "🔔EMPATE!"
    else:
        resultado = "⛔JOGADA INVÁLIDA!!!"
else:
    print("😠Valor inválido!!! Tente novamente")
    
print("⭐Você jogou {}!\n⭐Eu joguei {}!\n⭐RESULTADO:{}".format((itens)[jogador], (itens)[computador], resultado))
print("_" *35)