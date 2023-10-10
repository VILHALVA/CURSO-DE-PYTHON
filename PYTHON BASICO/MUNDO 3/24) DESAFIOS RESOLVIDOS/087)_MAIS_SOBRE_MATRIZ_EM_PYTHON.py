#=========MAIS SOBRE MATRIZ EM PYTHON:==============================

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"😎Digite um valor[{l+1}/{c+1}]:\n>>>"))
print("_" *30)

for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]",end="")
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
    
for l in range(0,3):
    scol += matriz[l][2]
    
for c in range(0, 3):
    if c == 0 or matriz[1][c] > mai:
        mai = matriz[1][c]
   
print("_" *30)
print(f"⭐A soma dos pares é {spar}\n⭐A soma da 3ª coluna é {scol}\n⭐O maior valor da 2ª linha é {mai}")
print("_" *30)
