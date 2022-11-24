#==========FUNÇÃO DE CONTADOR:========================================
from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    print("=" *30, f"\ncontagem de {i} até {f} de {p} em {p}:")
    sleep(2)
    
    if i < f:
        cont = i
        while cont <= f:
            print(f"{cont} ",end="", flush=True)
            sleep(0.5)
            cont += p
        print("\n⛔FIM")
    else:
        cont = i
        while cont >= f:
            print(f"{cont} ",end="", flush=True)
            sleep(0.5)
            cont -= p   
        print("\n⛔FIM\n", "=" *30)
 
        
contador(0, 10, 1)
contador(10, 0, 2)

print("😈Agora é sua vez...")
sleep(1)
ini = int(input("😎Digite o início:\n>>>"))
fim = int(input("😎Digite o fim:\n>>>"))
pas = int(input("😎Digite o passo:\n>>>"))
contador(ini, fim, pas)