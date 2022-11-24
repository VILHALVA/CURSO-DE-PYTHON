#==========FORMATANDO MOEDAS 2:=========================

#-----------FUNCÕES:----------------------------------
def aumentar(preço=0, formato=False):
    res = preço + (preço * preço / 100)
    return res if formato is False else moeda(res)
    
def diminuir(preço=0, formato=False):
    res = preço - (preço * preço / 100)
    return res if formato is False else moeda(res)

def dobro(preço=0, formato=False):
    res = preço * 2
    return res if not formato else moeda(res)
    
def metade(preço=0, formato=False):
    res = preço / 2
    return res if not formato else moeda(res)
    
def moeda(preço=0, moeda="R$"): 
    return f"{moeda}{preço:>4.2f}".replace(".", ",")
    
#----------PROGRAMA PRINCIPAL:-------------------------------
#from moeda import metade, dobro, aumentar, diminuir 

p = float(input("😎Digite o preço:\n>>>"))
print("_" *35, f"\n⭐O aumento de {moeda(p)} é {moeda(aumentar(p))}!\n⭐O diminuto de {moeda(p)} é {moeda(diminuir(p))}!\n⭐O dobro de {moeda(p)} é {moeda(dobro(p))}!\n⭐A metade de {moeda(p)} é {moeda(metade(p))}!\n", "_" *35)

#🔺Quando se usa a modularisação, para que aja a formação (R$), é necessário implementar o "True" em "{moeda(função(p, True))}".