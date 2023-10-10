#=========CONTANDO VOGAIS EM TUPLA:==========================

words = ("aprender", "programar", "linguagem", "python",
         "curso", "gratis", "estudar", "praticar", 
         "trabalhar", "mercado", "programa", "futuro")

for p in words:
    print(f"\n⭐No termo {p.upper()} temos: ",end="")
    for letra in p:
        if letra.lower() in "aeiou":
            print(letra,end=" ")