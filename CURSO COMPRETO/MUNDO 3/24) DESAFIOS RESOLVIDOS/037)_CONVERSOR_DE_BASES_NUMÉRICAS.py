#=========CONVERSOR DE BASES NUMÉRICAS:============================
from time import sleep

num = int(input("😎Digite um número inteiro:\n>>>"))
sleep(2)
print("😎Escolha uma das bases para conversão:")

print("_" *35)
menu = print('''
[ 1 ] Converter para BINÁRIO;
[ 2 ] Converter para OCTAL;
[ 3 ] Converter para HEXADECIMAL;''')
print("_" *35)

sleep(3)
opção = int(input("😎Escolha a sua opção:\n>>>"))
print("⏳Processando...",end= "\r")
sleep(3)

print("-" *35)
if opção == 1:
    print("⭐Valor: {:.0f};\n⭐Em BINÁRIO: {}!".format(num, bin(num)[2:]))
elif opção == 2:
    print("⭐Valor: {:.0f};\n⭐Em OCTAL: {}!".format(num, oct(num)[2:]))
elif opção == 3: 
    print("⭐Valor: {:.0f};\n⭐Em HEXADECIMAL: {}!".format(num, hex(num)[2:]))
else:
    print("😡VALOR INVÁLIDO!!!")
print("-" *35)