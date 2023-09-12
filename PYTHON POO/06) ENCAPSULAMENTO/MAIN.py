from BASE_DE_DADOS import BaseDeDados

bd = BaseDeDados()
bd.inserir_cliente(1, 'OTÁVIO')
bd.inserir_cliente(2, 'MARCELO')
bd.inserir_cliente(3, 'ROSE')
# bd._dados = "INSERIR DADOS QUALQUER"
bd.apaga_cliente(2)
bd.lista_clientes()