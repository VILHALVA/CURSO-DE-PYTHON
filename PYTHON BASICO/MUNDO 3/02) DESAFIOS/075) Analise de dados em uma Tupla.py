#==========ANÁLISE DE DADOS EM UMA TUPLA:========================

num = (int(input("😎Digite um número[1/4]:\n>>>")),
       int(input("😎Digite outro número[2/4]:\n>>>")),
       int(input("😎Digite mais número[3/4]:\n>>>")),
       int(input("😎Digite o último número[4/4]:\n>>>")))
print(f"⭐Você digitou os valores {num}!\n⭐O 9 apareceu {num.count(9)} vezes!")

if 3 in num:
    print(f"⭐O 3 apareceu na {num.index(3)+1}ª posição!")
else:
    print("⭐Não temos o valor 3!")    
print("⭐Os valores pares foram", end= " ")  
     
for n in num:
    if n % 2 == 0:
        print(n, end=" ")



