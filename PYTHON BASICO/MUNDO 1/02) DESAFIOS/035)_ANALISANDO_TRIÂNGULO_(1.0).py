#=========ANALISANDO TRIÂNGULO:=============================
r1 = float(input("😎Digite o primeiro segmento:\n>>>"))
r2 = float(input("😎Digite o segundo segmento:\n>>>"))
r3 = float(input("😎Digite o terceiro segmento:\n>>>"))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    triângulo = "👍SIM"
else:
    triângulo = "👎NÃO"

print("-" *35)
print("⭐Os valores digitados foram {},{},{}!\n⭐Forma triângulo?:{}!".format(r1, r2, r3, triângulo))
print("-" *35)