#==========ENTRADA DE DADOS MONETÁRIOS:=========================

#-----------MOEDA.PY:----------------------------------
def aumentar(preço=0, taxa=0, formato=False):
    res = preço + (preço * taxa / 100)
    return res if formato is False else moeda(res)
    
def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa / 100)
    return res if formato is False else moeda(res)

def dobro(preço=0, formato=False):
    res = preço * 2
    return res if not formato else moeda(res)
    
def metade(preço=0, formato=False):
    res = preço / 2
    return res if not formato else moeda(res)
    
def moeda(preço=0, moeda="R$"): 
    return f"{moeda}{preço:>4.2f}".replace(".", ",")
    
def resumo(preço=0, taxaa=10, taxar=5):
    print("_" *35)
    print("🎂RESUMO DO VALOR:".center(30))
    print("-" *35)
    print(f"⭐Preço analisado: \t{moeda(preço)}")
    print(f"⭐Dobro do preço: \t{dobro(preço, True)}")
    print(f"⭐Metade do preço: \t{metade(preço, True)}")
    print(f"⭐Com {taxaa}% de aumento: \t{aumentar(preço, taxaa, True)}")
    print(f"⭐Com {taxar}% de redução: \t{diminuir(preço, taxar, True)}")
    print("_" *35)
    
#--------------DADO.PY:-----------------------------------------------
def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(",", ".").strip()
        if entrada.isalpha() or entrada == "":
            print(f"\033[0;31m⛔ERRO!: \'{entrada}\' é valor inválido!!!\033[m")
        else:
            válido = True
            return float(entrada)
    
#----------PROGRAMA PRINCIPAL:-------------------------------
#from ex111.ultilidades import moeda, dado
#from ex111.utilidadescev import moeda
#from ex112.utilidadescev import dado

p = leiaDinheiro("😎Digite o preço:\n>>>")
#p = dado.leiaDinheiro("😎Digite o preço:\n>>>") #<Esse seria o correto se o aplicativo permitisse o uso de pacotes.

resumo(p)
resumo(p, 50, 30)