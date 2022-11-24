#======= PITANDO A PAREDE: =========================
import time

base = float(input("😎Digite a largura da sua parede:\n>>"))
altura = float(input("😎Digite a altura da parede:\n>>>"))

área = base * altura
tinta = área / 2

print("⏳Processando...",end="\r")
time.sleep(3)
print("⭐A sua parede tem uma dimensão de {:.0f}×{:.0f}m;".format(base, altura))
print("⭐Para você pintar uma parede de {:.0f}m²,você precisará usar {} litros de tinta!".format(área, tinta))
