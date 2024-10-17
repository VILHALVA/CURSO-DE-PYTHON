class BaseDeDados:
    def __init__(self):
        self._dados = {}
        
    def inserir_cliente(self, id, nome):
        if 'clientes' not in self._dados:
            self._dados['clientes'] = {id:nome}
        else:
            self._dados['clientes'].update({id:nome})
    
    def lista_clientes(self):
        for id, nome in self._dados['clientes'].items():
            print(id, nome)
    
    def apaga_cliente(self, id):
        del self._dados['clientes'][id]