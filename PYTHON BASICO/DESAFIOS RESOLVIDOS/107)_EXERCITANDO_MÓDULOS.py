#==========EXERCITANDO OS MÓDULOS:=========================

#-----------FUNCÕES:----------------------------------
def aumentar(preço):
    res = preço + (preço * preço / 100)
    return res
    
def diminuir(preço):
    res = preço - (preço * preço / 100)
    return res

def dobro(preço):
    res = preço * 2
    return res
    
def metade(preço):
    res = preço / 2
    return res   
    
#----------PROGRAMA PRINCIPAL:--------------------------------
#from moeda import metade, dobro, aumentar, diminuir 

p = float(input("😎Digite o preço:\n>>>"))
print("_" *35, f"\n⭐O aumento de {p} é {aumentar(p)}!\n⭐O diminuto de {p} é {diminuir(p)}!\n⭐O dobro de {p} é {dobro(p)}!\n⭐A metade de {p} é {metade(p)}!\n", "_" *35)