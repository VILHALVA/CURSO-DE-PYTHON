#==========MAIOR OU MENOR VALOR:===============================
a = int(input("😎Digite o primeiro valor inteiro:\n>>>"))
b = int(input("😎Digite o segundo valor inteiro:\n>>>"))
c = int(input("😎Digite o terceiro valor inteiro:\n>>>"))

#Verificando quem é o menor: 
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

#Verificando quem é o maior:
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print("-" *35)
print("⭐Você digitou: {:.0f}, {:.0f}, {:.0f}!\n⭐O menor valor digitado foi {:.0f}!\n⭐O maior valor digitado foi {:.0f}!".format(a, b, c, menor, maior))
print("-" *35)