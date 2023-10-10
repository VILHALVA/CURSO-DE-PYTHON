#========VALIDANDO EXPRESSÕES MATEMÁTICAS:=================================
expr = str(input("😎Digite a sua explessão matemática:\n>>>")).strip()
pilha = []

for símb in expr:
    if símb == "(":
        	pilha.append("(")
    elif símb == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break

if len(pilha) == 0:
    print("👍Sua expressão está correta!")
else:
    print("👎Sua expressão está errada!")
    