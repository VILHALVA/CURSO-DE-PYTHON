from PRODUTO import Produto

p1 = Produto('CAMISETA', 50)
p1.desconto(10)
print(p1.nome, p1.preco)

p2 = Produto('CANECA', "R$15")
p2.desconto(20)
print(p2.nome, p2.preco)
