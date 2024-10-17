#========= [ 04 ] VARIAVEL COMPOSTA: LISTA ==================

MATRIZ = [[0,0,0], [0,0,0], [0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        MATRIZ[l][c] = int(input(f"😎Digite o [{c+1}/{l+1}] valor:\n>>>"))
for l in range(0,3):
    for c in range(0,3):
        print(f"[{MATRIZ[l][c]}]",end="")
    print()