from PESSOA import Pessoa

p1 = Pessoa('LUIZ', 32)
p1.get_ano_nascimento()
print(p1.idade)
p1.get_ano_nascimento()
p1.acha_id()
print(p1.acha_id())

p2 = Pessoa('JOÃO', 22)
print(p2.idade)
p2.get_ano_nascimento()
print(p2.acha_id())