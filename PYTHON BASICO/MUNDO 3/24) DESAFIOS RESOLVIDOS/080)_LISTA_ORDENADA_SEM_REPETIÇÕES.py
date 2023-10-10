#============LISTA ORDENADA SEM REPETIÇÕES:===================================
lista = []
for c in range(0, 5+1):
    n = int(input(f"😎Digite o valor[{c}/5]:\n>>>"))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print(f"😬[{n}] adicionado no final da lista!")
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos,n)
                print(f"😬[{n}] adicionado na posição: {pos}!")
                break
            pos += 1

print("_" *35)
print(f"⭐Os valores digitados foram:\n⚡{lista}")
print("_" *35)