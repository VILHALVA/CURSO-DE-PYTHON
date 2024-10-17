#==========FORMATANDO MOEDAS:=========================

#-----------FUNCÕES:----------------------------------
def aumentar(preço=0):
    res = preço + (preço * preço / 100)
    return res
    
def diminuir(preço=0):
    res = preço - (preço * preço / 100)
    return res

def dobro(preço=0):
    res = preço * 2
    return res
    
def metade(preço=0):
    res = preço / 2
    return res  
    
def moeda(preço=0, moeda="R$"): 
    return f"{moeda}{preço:>4.2f}".replace(".", ",")
    
#----------PROGRAMA PRINCIPAL:-------------------------------
#from moeda import metade, dobro, aumentar, diminuir 

p = float(input("😎Digite o preço:\n>>>"))
print("_" *35, f"\n⭐O aumento de {moeda(p)} é {moeda(aumentar(p))}!\n⭐O diminuto de {moeda(p)} é {moeda(diminuir(p))}!\n⭐O dobro de {moeda(p)} é {moeda(dobro(p))}!\n⭐A metade de {moeda(p)} é {moeda(metade(p))}!\n", "_" *35)