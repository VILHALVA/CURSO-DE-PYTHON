#===========TUPLAS:================================================

#>TUPLAS: Se refere a variáveis compostas e o seu fatiamento (É semelhante as listas)!

lanche = ("Hambúrguer", "Suco", "Pizza", "Pudim", "Batata Frita")
#>FATIAMENTO(+):  0,      1,      2,       3,        4.
#>FATIAMENTO(-): -5,     -4,     -3,      -2        -1

print(lanche) #>Todo o lanche/Toda a Tupla em ordem cronológica (Usando paretenses).
print(lanche[1]) #>Somente o "Suco".
print(lanche[-2]) #>Somente a "Pizza".
print(lanche[1:3]) #>Do "Suco" até a "Pizza".
print(lanche[2:]) #>Da "Pizza até o "Pudim".
print(lanche[:2]) #>Do "Hambúrguer" até o "Suco".
print(lanche[-2:]) #>Vai da "Pizza" até o "Pudim".
print(lanche[-3:]) #>Vai do "Suco" até o "Pudim".
print(len(lanche)) #>Vai contar a quantidade de objetos na Tupla; No caso, são 5!
print(sorted(lanche)) #> Irá exibir todos os itens em ordem alfabética (Usando colchetes/listas).

#--------AJUDA ELIMINAR PARETENSES:--------------------
for cont in range(0, len(lanche)): #>Primeira maneira de usar o "for"!
    #print(cont) #>Irá fazer a contagem numérica dos itens da Tupla, começando em 0!
    print(lanche[cont]) #>Irá mencionar todos os itens da Tupla sem parentes!
    print(f"😬Eu vou comer {lanche[cont]}!") #>"For" irá citar todos os objetos da Tupla com a frase personalizada!
    print(f"😬Eu vou comer {lanche[cont]} na posição {cont}!") #>"For" irá citar todos os objetos da Tupla com a frase personalizada e sua posição numérica!
print("😈Comir pra caralho!")

for pos, comida in enumerate(lanche): #>Esse é o híbrido entre 1° e 2° maneira de se usar o "for"!
    print(f"😬Eu vou comer {comida} na posição {pos}!") #>"For" irá citar todos os objetos da Tupla com a frase personalizada e sua posição numérica!
print("😈Comir pra caralho!")

for comida in lanche: #>Segunda maneira de usar o "for"!
    print(f"😬Eu vou comer {comida}!") #>"For" irá citar todos os objetos da Tupla com a frase personalizada!
print("😈Comir pra caralho!")

#---------TUPLAS SÃO IMUTÁVEIS:-------------------------------
#lanche[1] = ("Refrigerante")#>Você só trocar objeto da Tupla quando o programa estiver parado.
#print(lanche[1]) #>Vai dá erro. O objeto não pode ser atribuído ("Refrigerante" não substitui "Suco"!).

pessoa = ("Samuel", "25", "M", "122") #>Diferente do Java, no python é permitido ter elementos diferentes (str com int) na mesma Tupla!
print(pessoa)
#del(pessoa) #>Única coisa que é permitido, é apenas apagar a Tupla inteira (Não pode apagar um elemento da Tupla)!

#===========VARIAS TUPLAS:=========================================
a = (2, 5, 4)
b = (5, 8, 1, 2)

print(a) #>Exibe apenas a Tupla "a" em ordem real!
print(b) #>Exibe apenas a Tupla "b" em ordem real!

c1 = a + b #>Jutando as duas Tuplas na ordem "a" com "b"!
c2 = b + a #>Jutando as duas Tuplas na ordem "b" com "a"!

print(c1) #>Irá concatenar as duas Tuplas!
print(len(c2)) #>Exibe a quantidade de elementos, no caso são 7!
print(c2.count(5)) #>Exibe a quantidade de vezes que o número "5" aparece em "c", no caso 2!
print(c1.index(8)) #>Exibe a posição numérica do "8"!
print(c1.index(2, 4)) #>Exibe a posição numérica do "2", apartir da posição 4 (Nesse caso, temos dois números 2)!

