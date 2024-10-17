from CLASSE import Carrinho, Produto

carrinho = Carrinho()

p1 = Produto('CAMISETA', 72)
p2 = Produto('COPO', 56)
p3 = Produto('LIVRO', 343)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)

carrinho.lista_produtos()
print(carrinho.soma_total())

        