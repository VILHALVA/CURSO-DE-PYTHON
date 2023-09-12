class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__
        
    def falar(self, assunto):
        print(f"O {self.nomeclasse} QUE SE CHAMA {self.nome} ESTÁ FALANDO SOBRE {assunto}!")
        
class Professor(Pessoa):
    def dando_aula(self, materia):
        print(f"O {self.nomeclasse} QUE SE CHAMA {self.nome} ESTÁ DANDO AULA SOBRE {materia}!")

class Aluno(Pessoa):
    def estudando(self, materia):
        print(f"O {self.nomeclasse} QUE SE CHAMA {self.nome} ESTÁ ESTUDANDO {materia}!")

    