#==========FUNÇÕES PARA SORTEAR E SOMAR:================================
from random import randint
from time import sleep

def sorteia(lista):
    print("=" *35, "\n🌎SORTEANDO OS VALORES DA LISTA:\n", "=" *35)
    for cont in range(0,10):
        n = randint(1, 100)
        lista.append(n)
        lista.append(randint(1,100))
        print(f"{n} ",end="", flush=True)
        sleep(0.5)
    print("\n⛔FIM!!!")
        
def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print("_" *35, f"\n⭐Somoando os valores pares:\n⚡Temos: {lista}\n⭐Sua soma é:\n⚡{soma}", "\n", "_" *35)
    
    
números = list()
sorteia(números)
somaPar(números)