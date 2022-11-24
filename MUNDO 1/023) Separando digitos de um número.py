#========SEPARANDO DIGITO DE UM NÚMERO:================
num = int(input("😎Informe um número:\n>>>"))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print("⭐Analisando o número {}!".format(num))
print("⭐Unidade: {}!".format(u))
print("⭐Dezena: {}!".format(d))
print("⭐Centena: {}!".format(c))
print("⭐Milhar: {}!".format(m))