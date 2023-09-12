from CLASSE import Cliente

cliente1 = Cliente('LUIZ', 32)
cliente1.insere_endereco('BELO HORIZONTE', 'MG')
print(cliente1.nome)
cliente1.lista_enderecos()
del cliente1
print()

cliente2 = Cliente('MARIA', 55)
cliente2.insere_endereco('SALVADOR', 'BA')
print(cliente2.nome)
cliente2.lista_enderecos()
print()

cliente3 = Cliente('JOÃO', 19)
cliente3.insere_endereco('SÃO PAULO', 'SP')
print(cliente3.nome)
cliente3.lista_enderecos()
print()

print("#"*100)