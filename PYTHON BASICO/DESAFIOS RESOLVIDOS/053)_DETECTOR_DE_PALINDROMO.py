#==================DETECTOR DE PALÍNDROMO:===============================
frase = str(input("😎Digite uma frase:\n>>>")).strip().upper()
palavras = frase.split()
junto = "*".join(palavras)
inverso = ""

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    resultado = "👍SIM!!!"
else:
    resultado = "👎NÃO!!!"
print("_" *35)
print("⭐Você inscreveu: {}!\n⭐Inverso é {}!\n⭐É Palíndromo?:{}".format(junto, inverso, resultado))
print("_" *35)