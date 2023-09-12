#===========FUNÇÃO QUE DESCOBRE O MAIOR VALOR:===============================
from time import sleep

def maior(*num):
    cont = maior = 0
    print("😎Analisando os valores passados...")
    for valor in num:
        print(f"{valor} ",end="", flush=True)
        sleep(0.5)
        if cont == 0 or valor > maior:
            maior = valor
        cont += 1
    sleep(0.7)
    print("\n", "_" *35, f"\n⭐Foram informados {cont} valores!\n⭐O maior foi {maior}!\n", "\n", "_" *35)
        
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()