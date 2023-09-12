from CLASSE import *

p1 = Professor('ROBERTO', 22)
p2 = Aluno('LUCAS', 14)
p3 = Pessoa("JOÃO", 56)

print(p1.nome, p1.idade)
print(p2.nome, p2.idade)

p1.falar("PITAGORAS")
p2.falar("PUBERDADE")
p3.falar("PERDA DO BV")

p1.dando_aula("MATEMATICA")
p2.estudando("POLINONIMOS")
