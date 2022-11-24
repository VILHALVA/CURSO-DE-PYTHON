#==============FUNÇÕES PARTE 1:===========================================

#---------FORMA TRADICIONAL DE INSCREVER O CÓDIGO: ---------------------------;;

a = 4
b = 5
s = a + b
print(s)
a = 8
b = 9
s = a + b
print(s)
a = 2
b = 1
s = a + b
print(s)

#↑Repare acima a eterna repetição de uma única rotina.

#----------FORMA OTIMIZADA DE INSCREVER MESMO PROGRAMA, USANDO FUNÇÃO:

def soma(a, b):  #«Definindo uma função/comando.
    s = a + b
    print(s)
    
soma(4, 5)  #«Programa principal com a chamada de função.
soma(8, 9)
soma(2, 1)
soma(a=9, b=7)
#soma(5) #<Vai dar erro, pois o def eu definir 2 parâmetros (a,b).

def soma(a, b): #<Forma personalizada.
    print(f"⭐A = {a} e B = {b}!")
    s = a + b
    print(f"⚡A soma de A+B é {s}!")
    
soma(4, 5)
soma(8, 9)
soma(2, 1)
soma(a=9, b=7)
soma(b=9, a=7) #<Trocando a ordem dos valores, o def irá considerar ao exibir o conceito (Como na lista e dicionário).
#soma(12, 9, 11) #<Vai dá erro. Pois no def definir somente a soma de 2 parâmetros. Para resolver isso, devemos definir EMPACOTAMENTO.

#-------EMPACOTAMENTO DE PARÂMETROS:-------------------------

def contador(*num):
    print(num)
    
contador(2, 1, 7) #<Irá exibir os valores como Tuplas.
contador(3, 2)
contador(9, 8, 6, 4, 12, 19)


def contador(*num):
    for valor in num: #<Eliminar: "{[(".
        print(f" {valor}  ",end="")
    print("⛔FIM")
    
contador(2, 1, 7) #<Irá exibir os valores sem os pareteses.
contador(3, 2)
contador(9, 8, 6, 4, 12, 19)


def contador(*num):
    tam = len(num)
    print(f"Recebi os valores {num} e são ao todo {tam} caracteres;")
    
contador(2, 1, 7) #<Irá exibir os valores como Tuplas.
contador(3, 2)
contador(9, 8, 6, 4, 12, 19)

#---------USANDO FUNÇÕES COM LISTAS:------------------------------
def dobra(lista):	
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1
        
valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

#-------DESINPACOTAMENTO:------------------------------
	
def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f"⚡Somando os números {valores} temos {s}")
    
soma(5, 2)
soma(9, 8, 7, 4)





    
