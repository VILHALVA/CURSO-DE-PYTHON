#==========FUNÇÃO QUE CALCULA ÁREA:====================================

def área(l, c):
    a = l * c
    print("_" *30, f"\n⭐Área do terreno {l}×{c} é de {a}m²!\n", "_" *30)

print("^" *20,"\n😈CONTROLE DE TERRENO:\n", "^" *20)
l = float(input("😎Digite a largura(m):\n>>>"))
c = float(input("😎Digite a altura(m):\n>>>"))
área(l, c)