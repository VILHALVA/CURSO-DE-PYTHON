#===========FUNÇÃO PARTE 2:============================================
	
#============DOCSTRINGS:====================================================================

#print(input.__doc__)
#help(input) #<Ambos servem para emitir manual (Docstrings) do comando "input" no terminal. Você pode digitar "help()" no terminal para acessar.

def contador(i, f, p):
    """
    »Faz contagem e mostra na tela.
    :★"I": Significa inicio;
    :★"F": Significa FIM;
    :★"P": Significa passo.
    """   
    c = i
    while c <= f:
        print(f"{c}, ",end=" ")
        c += p
    print("\n⛔FIM!")

contador(2, 10, 2)
help(contador) #>Exibe o manual do comando "contador".

#============PARÂMETROS OPCIONAIS:========================={{==={
	
def somar(a=0, b=0, c=0, d=0, e=0): #<Se exitir apenas 2 parâmetros, o cálculo será feito usando os parâmetros restantes.
    s = a + b + c + d + e
    print(f"⚡A soma vale {s}")

somar(3, 2, 5)
somar(8, 9)
somar(23, 56, 89, 64, 34)
somar()
somar(b=4, c=2) #<Como não informei o "a", ele será 0.

#===========ESCOPO DE VARIÁVEIS:==================================

def teste():
    x = 8 #>Variável local.
    print(f"⭐Na função teste, n vale {n}")
    print(f"⭐Na função teste, x vale {x}")

n = 2 #>É uma variável global.
print(f"⭐No programa principal, n vale {n}")
teste()

#print(f"⭐No programa principal, x vale {x}") #<Vai dar erro devido o x ter sido declarado apenas na função "teste".


def teste(b): #<Escopo local: b = 9, c = 2, a = 5.
    global a #>Irá anular o "a = 5" do escopo global, e aceitar "a = 8" para todos os escopos.
    a = 8 #<Nesse escopo local, a = 8; Enquanto no escopo global, a = 5.
    b += 4
    c = 2
    print(f"⭐A vale {a}")
    print(f"⭐B vale {b}")
    print(f"⭐C vale {c}")

a = 5 #<Escolpo global: a = 5. Só funciona aqui se ela for declarada.
teste(a) #<🔶O escopo global só irá funcionar dentro da função, se o escopo local for igual a 0.

print(f"⭐A vale {a}") #<Irá funcionar, pois "A" já foi declarada no escopo global.
#print(f"⭐B vale {b}") #<Não irá funcionar, pois "B" não foi declarada no escopo global.
#print(f"⭐C vale {c}") #<Não irá funcionar, pois "C" não foi declarada no escopo global.

#=============RETORNO DE VALORES:==============================================================

def somar(a=0, b=0, c=0, d=0, e=0): 
    s = a + b + c + d + e
    return s #>Isso te ajuda a dar um print do resultado personalizado, sem precisar usar estrutura de repetição (for ou while).

r1 = somar(3, 2, 5)
r2 = somar(8, 9)
r3 = somar(23, 56, 89, 64, 34)
r4 = somar(4)
print(f"⭐Os meus cálculos deram: {r1}, {r2}, {r3}, {r4}!")
print(f"⭐Somando tudo, temos: {r1+r2+r3+r4}!")

#============EXERCÍCIO: FATORIAL DE UM NÚMERO:========================================================================================
	
def fatorial(num=1):
    f = 1
    for c in range (num, 0, -1):
        f *= c
    return f

n = int(input("😬Digite um número:\n>>>"))
print(f"⭐O fatorial de {n} é igual a {fatorial(n)}")


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input("😬Digite um número:\n>>>"))
if par(num):
    print(f"😈O {num} é PAR!")
else:
    print(f"😈O {num} é IMPAR!")

