#==============MÓDULOS E PACOTES:====================================

#-------------ARQUIVO 1:--------------------------------------------
def fatorial(n):
    f = 1
    for c in range(1,n+1):
        f *= c
    return f

def dobro(n):
    return n * 2

def triplo(n):
    return n * 3
 
#-----------ARQUIVO 2:----------------------------------------
#from úteis import fatorial #>Semelhante as bibliotecas do python, eu posso importar funções específicas (def).
import úteis

num = int(input("😎Digite um valor:\n>>>"))
fat = fatorial(num)
print("_" *35, f"\n⭐O fatorial de {num} é {fat}\n⭐O dobro de {num} é {úteis.dobro(num)}\n⭐O triplo de {num} é {úteis.triplo(num)}\n", "_" *35)

#🔺Devido ao fato de não ter computador, e os apps para Android não terem a função de "pacotes" a aula ficou por aqui. O única maneira de praticar, e colocar tudo em arquivo; Como antes.