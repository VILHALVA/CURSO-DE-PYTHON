from datetime import datetime

class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))
    
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
    
    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} NÃO PODE FALAR COMENDO!')
            return
        if self.falando:
            print(f'{self.nome} JÁ ESTÁ FALANDO!')
            return
        print(f"O {self.nome} ESTÁ FALANDO SOBRE {assunto}!")
        self.falando = True
        
    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} NÃO ESTAVA FALANDO!')
            return
        print(f"{self.nome} PAROU DE FALAR!")
        self.falando = False
    
    def comer(self, alimento):
        if self.comendo:
            print(f"{self.nome} JÁ ESTÁ COMENDO!")
            return
        if self.falando:
            print(f'{self.nome} NÃO PODE COMER FALANDO!')
            return
        print(f"O {self.nome} ESTÁ COMENDO {alimento}!")
        self.comendo = True
        
    def parar_comer(self):
        if not self.comendo:
            print(f"{self.nome} NÃO ESTAVA COMENDO!")
            return
        print(f"{self.nome} PAROU DE COMER!")
        self.comendo = False
        
    def get_ano_nascimento(self):
        return self.ano_atual - self.idade
    