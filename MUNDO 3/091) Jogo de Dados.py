#============JOGO DE DADOS:================================
from random import randint
from operator import itemgetter
from time import sleep

jogo = {"JOGADOR 1": randint(1,6),
        "JOGADOR 2": randint(1,6),
        "JOGADOR 3": randint(1,6),
        "JOGADOR 4": randint(1,6)}
ranking = list()

print("-" *5,"⚡VALORES SORTEADOS:","-" *5)
for c in range(0, 120, 20):
    print(f"⌛Processando({c})%...",end="\r")
    sleep(1)
print("_" *35)
for k, v in jogo.items():
    print(f"{k} tirou {v} no dado!\n", "-" *35)
    sleep(2)
print("_" *35)
sleep(1)
for c in range(0, 125, 25):
    print(f"⌛Processando({c})%...",end="\r")
    sleep(1)
print("-" *5,"⚡RANKING DOS JOGADORES:","-" *5)
print("_" *35)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f"{i+1}ª LUGAR: {v[0]} com {v[1]}!\n", "-" *35)
    sleep(2) 
print("_" *35)  

print("      ⛔FIM!!!     ")
    
