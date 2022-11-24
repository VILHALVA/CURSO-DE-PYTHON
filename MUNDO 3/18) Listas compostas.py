#=========LISTAS COMPOSTAS:============================

teste = list() #>Lista 0
teste.append("Gustavo") #>Adiciona Gustavo a lista.
teste.append(40) #> Adiciona "40" a lista.
print(teste) 
galera = list() #>Lista 1
galera.append(teste[:]) #>Adiciona a lista "Galera" dentro de "teste" (1c0).
print(galera)

#==========ADICIONANDO LISTA DENTRO DE OUTRA:===============================
teste[0] = "Maria"
teste[1] = 22
galera.append(teste[:])
print(galera)

galera = [["João", 19], ["Ana", 31], ["Joaquim", 13], ["Maria", 45]]
print(galera)
print(galera[0]) #>Exibe apenas: "[João, 19]".
print(galera[0][0]) #>Exibe apenas "João".
print(galera[2][1]) #>Exibe apenas "13".

for p in galera: #>Elimina os colchetes.
    print(p[0]) #> Exibe apenas os itens "0" de todas as listas, no caso os nomes da galera.
    print(p[1]) #> Exibe apenas os itens "1" de todas as listas, no caso as idades da galera.
    print(f"⚡O {p[0]} tem {p[1]} anos de idade!") #>Exibe o nomes das pessoas e suas idades personalizadas.
    
#==========USUÁRIO PERSONALIZA A LISTA COMPOSTA:=================================================================

galera = list()
dado = list()
  
for c in range (0, 3):
    dado.append(str(input(f"😎Digite um nome[{c}/2]:\n>>>")))
    dado.append(int(input(f"😎Digite a idade[{c}/2]:\n>>>")))
    galera.append(dado[:])
    dado.clear()
print(galera)

totmaior = totmenor = 0
for p in galera:
    if p[1] >= 21:
        print(f"⭐{p[0]} é maior de idade!")
        totmaior += 1
    else:
        print(f"⭐{p[0]} é menor de idade!")
        totmenor += 1
print(f"⭐Temos {totmaior} maiores e {totmenor} menores!")