#===========LISTAS:=========================================
num = [2, 5, 9, 1]
print(num) #>Exibe a lista inteira.
num[2] = 3 #>Diferente da tupla, a lista pode ser modificada
num.append(7) #>Adiciona o 7 a lista. 
num.sort() #> Coloca a lista em ordem;
num.sort(reverse=True)
num.insert(2, 0) #>Adiciona o valor "2" na posição 0.
num.pop() #> Elimina o último elemento da lista.
num.pop(2) #>Elimina o segundo elemento da lista.
num.remove(2) #> Remove o primeiro elemento "2".
if 4 in num: #> Só irá remover o valor 4, se o encontrar.
    num.remove(4)
else:
    print("😈O 4 não foi encontrado")
print(num) #> Agora exibe a lista modificada
print(f"⭐Essa lista tem {len(num)} elementos!")

#===========ADICIONAR ELEMENTOS:===============================
valores = []
valores.append(5) 
valores.append(9)
valores.append(4)
for v in valores:
    print(f"⭐{v}...")

valores = list()
for cont in range(0,5):
    valores.append(int(input("😎Digite o valor:\n>>>")))
    
for c, v in enumerate(valores):
    print(f"⭐Na posição {c} encontrei o valor {v}!")
print("🎂FIM")


a = [2, 3, 4, 7]
b = a #> O B faz conexão com a lista de B
b = a[:] #> O B faz cópia de A.
b[2] = 8
print(f"⭐Lista A: {a}!\n⭐Lista B: {b}!")