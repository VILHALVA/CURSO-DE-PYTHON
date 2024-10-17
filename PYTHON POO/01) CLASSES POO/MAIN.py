from PESSOA import Pessoa

p1 = Pessoa('LUIZ', 32)
p2 = Pessoa('JOÃO', 29)

p1.comer('BATATAS')
p1.comer('BANANAS')
p2.comer('MANDIOCA')
p1.parar_comer()
p1.parar_falar()
p1.falar('FIM DO MUNDO')
p2.falar('ORIENTAÇÃO A OBJETOS')
p2.parar_comer()

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())