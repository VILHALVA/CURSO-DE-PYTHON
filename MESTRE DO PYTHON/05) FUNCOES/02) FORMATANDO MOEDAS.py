from MOEDAS import moeda, metade, dobro, aumentar, diminuir 

def VALOR_FLOAT(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError, IndexError):
            print("🔺VALOR INVÁLIDO!")
            continue
        else:
            return n
            

p = VALOR_FLOAT("😎Digite o preço:\n>>>")

print("_" *35, f"\n⭐O aumento de {moeda(p)} é {moeda(aumentar(p))}!\n⭐O diminuto de {moeda(p)} é {moeda(diminuir(p))}!\n⭐O dobro de {moeda(p)} é {moeda(dobro(p))}!\n⭐A metade de {moeda(p)} é {moeda(metade(p))}!\n", "_" *35)

#🔺Quando se usa a modularisação, para que aja a formação (R$), é necessário implementar o "True" em "{moeda(função(p, True))}".