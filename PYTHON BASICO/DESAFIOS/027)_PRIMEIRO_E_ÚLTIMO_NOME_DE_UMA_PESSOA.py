#===========PRIMEIRO E ÚLTIMO NOME DE UMA PESSOA:===========================
n = str(input("😎Qual é o seu nome completo?\n>>>")).strip().upper()
nome = n.split()
print("⭐Prazer em te conhecer!")
print("⭐Seu primeiro nome é {}!".format(nome[0]))
print("⭐Seu último sobrenome é {}!".format(nome[len(nome)-1]))