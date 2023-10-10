#=======ANALISADOR DE NOME:======================
from time import sleep

nome = str(input("😎Digite o seu nome completo:\n>>>")).strip()
print("⏳Processando...",end="\r")
sleep(3)

print("⭐Seu nome em maiúsculo é {}!".format(nome.upper()))
print("⭐Seu nome em minúsculo é {}!".format(nome.lower()))
print("⭐Seu nome tem {} letras!".format(len(nome)-nome.count(" ")))
separa = nome.split()
print("⭐Seu primeiro nome é {}!; Ele tem {} letras!".format(separa[0], len(separa[0])))