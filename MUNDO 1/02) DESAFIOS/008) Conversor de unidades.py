#========= CONVERSOR DE MEDIDAS: ====================
import time

medida = float(input("😎Digite uma distância em metros:\n>>>"))

cm = medida * 100
nm = medida * 1000

print("⏳Processando...",end="\r")
time.sleep(5)
print("⭐A medida de {}m corresponde a {:.0f}cm e {:.0f}nm".format(medida, cm, nm))