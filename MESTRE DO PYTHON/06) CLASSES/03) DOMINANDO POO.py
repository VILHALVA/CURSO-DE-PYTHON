#--------------------[A]PROPRIEDADE: ABSTRAÇÃO:-------------------------

class caneca():
    formato = "Cilindro com alça lateral"
    def __init__(self, nome, cor, logo):
        self.nome = nome
        self.cor = cor
        self.logo = logo
        self.status = "Cheia"
    def beber(self):
        self.status = "Vazia"
    def encher(self):
        self.status = "Cheia"

CANECA_1 = caneca("Londrina", "Branca", "Cidade de londres")
CANECA_2 = caneca("Bylarne", "Verde", "Cidade do Rio")
CANECA_3 = caneca("Pothy", "Vermelha", "Cidade do Sul")
CANECA_4 = caneca("Multitype", "Azul", "Cidade do Amazonas")
CANECA_5 = caneca("Rythwe", "Amarelo", "Cidade do Nordeste")

print(f"⛔1 CANECA: ⭐NOME: {CANECA_1.nome}; ⭐COR: {CANECA_1.cor}; ⭐LOGO {CANECA_1.logo}.")
print(f"⛔2 CANECA: ⭐NOME: {CANECA_2.nome}; ⭐COR: {CANECA_2.cor}; ⭐LOGO {CANECA_2.logo}.")
print(f"⛔3 CANECA: ⭐NOME: {CANECA_3.nome}; ⭐COR: {CANECA_3.cor}; ⭐LOGO {CANECA_3.logo}.")
print(f"⛔4 CANECA: ⭐NOME: {CANECA_4.nome}; ⭐COR: {CANECA_4.cor}; ⭐LOGO {CANECA_4.logo}.")
print(f"⛔5 CANECA: ⭐NOME: {CANECA_5.nome}; ⭐COR: {CANECA_5.cor}; ⭐LOGO {CANECA_5.logo}.")

CANECA_1.beber()
CANECA_1.encher()
CANECA_2.beber()

print(f"⛔1 CANECA: ⭐STATUS: {CANECA_1.status}")
print(f"⛔2 CANECA: ⭐STATUS: {CANECA_2.status}")
print(f"⛔3 CANECA: ⭐STATUS: {CANECA_3.status}")
print(f"⛔4 CANECA: ⭐STATUS: {CANECA_4.status}")
print(f"⛔5 CANECA: ⭐STATUS: {CANECA_5.status}")

#--------------------[B]PROPRIEDADE: HERANÇA:---------------------------
class caneca_londrina(caneca):
    def __init__(self):
        super().__init__("caneca londrina", "Verde", "Cidade de Lomdres") 
    def extras(self):
        print("⭐Como bonus voce ganha uma colher!")
    def som(self):
        print("⭐I'm Batman!")

caneca_lomdres = caneca_londrina()
caneca_lomdres.extras()
caneca_lomdres.som()