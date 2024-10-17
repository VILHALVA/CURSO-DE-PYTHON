#------EXEMPLO DE CLASSE E OBJETO:---------#

class Personagem():
    def __init__(self, nome, cor):
        self.cor = cor
        self.nome = nome
    def __repr__(self):
        return f"Personagem ({self.nome}), ({self.cor})"
    
Mickey = Personagem("Mickey", "Preto")
Mini = Personagem("Mimi", "Branco")
Pluto = Personagem("Pluto", "Amarelo")
Pateta = Personagem("Pateta", "Preto")

print(Mickey)
print(Mini)
print(Pluto)
print(Pateta)

