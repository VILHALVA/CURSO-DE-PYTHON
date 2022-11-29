#===========ESTRUTURA DE REPETIÇÃO FOR:===============================

i = int(input("😎INÍCIO:\n>>>"))
f = int(input("😎FIM:\n>>>"))
p = int(input("😎PASSO:\n>>>"))

for valor in range(i, f+1, p):
    print(valor)
print("🔔FIM!!!")

#==============================================
s = 0
for num in range(0, 4):
    n = int(input("😎Digite um valor:\n>>>"))
    s += n
print("⭐O somatório de todos os valores foi {}!".format(s))