#========INFICE DE MASSA CORPORAL:========================
peso = float(input("😎Digite o seu peso(kg):\n>>>"))
altura = float(input("😎Digite a sua altura(m):\n>>>"))

imc = peso / (altura **2)

if imc < 18.5:
    estado = "⚡ABAIXO!"
elif  18.5 <= imc < 25:
    estado = "⚡IDEAL!"
elif 25 <= imc < 30:
    estado = "⚡SOBREPESO!"
elif 30 >= imc < 40:
    estado = "⚡OBESIDADE!"
else:
    estado = "⚡MOBIRTA!"

print("_" *35)
print("⭐PESO: {:.2f}!\n⭐ALTURA: {:.2f}!\n⭐IMC: {:.2f}!\n⭐ESTADO: {}".format(peso, altura, imc, estado))
print("_" *35)