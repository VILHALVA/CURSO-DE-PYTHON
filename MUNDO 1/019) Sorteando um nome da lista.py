#==========SORTEANDO UM NOME DA LISTA:===========================
from random import choice

n1 = str(input("😎Primeiro aluno:\n>>>"))
n2 = str(input("😎Segundo aluno:\n>>>"))
n3 = str(input("😎Terceiro aluno:\n>>>"))
n4 = str(input("😎Quarto aluno:\n>>>"))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print("😎O aluno escolhido foi {}!".format(escolhido))