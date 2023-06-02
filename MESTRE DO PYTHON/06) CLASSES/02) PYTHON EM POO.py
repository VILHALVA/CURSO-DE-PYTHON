#--------------- CLASSE GLOBAL: ---------------------------------------
class Pessoa():
    def __init__(self, nome, idade, comendo = False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
        
    def falar(self, assunto):
        if self.comendo:
            print(f"{self.nome} não pode falar comendo!")
            return
        if self.falando:
            print(f"{self.nome} já está falando!")
        else:
            print(f"{self.nome} Está falando sobre {assunto}!")
            self.falando = True
            
    def parar_falar(self):
        if not self.falando:
            print(f"{self.nome} não está falando!")
        else:
            print(f"{self.nome} Parou de falar!")
            self.falando = False
                
    def comer(self, alimento):
        if self.comendo:
            print(f"{self.nome} já está de buxo cheio!")
        elif self.falando:
            print(f"{self.nome} não pode falar comendo!")       
        else:   
            print(f"{self.nome}, Com {self.idade} anos, está comendo {alimento}...")
            self.comendo = True
            
    def parar_comer(self):
        if not self.comendo:
            print(f"{self.nome} está comendo...")
        else:
            print(f"{self.nome} Parou de comer!")
            self.comendo = False

#--------------- PARTICIPANTES DO JANTAR: --------------------------    
p1 = Pessoa("Samuel", 26)
p2 = Pessoa("Daniel", 22)
p3 = Pessoa("João", 32)
p4 = Pessoa("Valcilda", 46)
p5 = Pessoa("Jaqueline", 8)
p6 = Pessoa("Caroline", 7)

#------------------ AÇÕES DOS PARTICIPANTES: ---------------------------
p1.comer("Macarrão com queijo")
p1.falar("POO")
p1.parar_comer()
p1.falar("POO")
p1.parar_falar()
p1.comer("Galinhas")
p2.comer("Batatas")
p3.comer("Mandioca")
p4.falar("Trabalho")
p4.comer("Sopa")
p5.comer("Biscoito")
p5.comer("Biscoito")
p6.comer("Leite em pó")
p6.comer("Banana")