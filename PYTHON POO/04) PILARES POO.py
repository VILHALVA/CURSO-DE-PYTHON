# 1. Encapsulamento:
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # Atributo privado

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente!")

    def get_saldo(self):  # Getter
        return self.__saldo

    def set_saldo(self, novo_saldo):  # Setter
        if novo_saldo >= 0:
            self.__saldo = novo_saldo
        else:
            print("Saldo inválido!")

conta = ContaBancaria("João", 1000)
print(conta.get_saldo())  # Saída: 1000
conta.set_saldo(1500)  # Alterando o saldo
print(conta.get_saldo())  # Saída: 1500
conta.set_saldo(-500)  # Tentativa de alterar o saldo com valor inválido

# Neste exemplo, a classe `ContaBancaria` possui um atributo privado `__saldo` que é encapsulado, ou seja, não pode ser acessado diretamente fora da classe. Os métodos `get_saldo()` e `set_saldo()` são utilizados para acessar e modificar o saldo de forma controlada.

# 2. Herança:
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        print("Au au!")

class Gato(Animal):
    def emitir_som(self):
        print("Miau!")

cachorro = Cachorro("Rex")
gato = Gato("Mimi")

cachorro.emitir_som()  # Saída: Au au!
gato.emitir_som()  # Saída: Miau!

# Neste exemplo, a classe `Animal` é a classe pai (superclasse) e as classes `Cachorro` e `Gato` são as classes filhas (subclasses). As subclasses herdam o atributo `nome` da classe pai e sobrescrevem o método `emitir_som()` para cada tipo de animal.

# 3. Polimorfismo:
class Animal:
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        print("Au au!")

class Gato(Animal):
    def emitir_som(self):
        print("Miau!")

def fazer_barulho(animal):
    animal.emitir_som()

cachorro = Cachorro()
gato = Gato()

fazer_barulho(cachorro)  # Saída: Au au!
fazer_barulho(gato)  # Saída: Miau!

# Neste exemplo, a função `fazer_barulho()` recebe um objeto animal como argumento e chama o método `emitir_som()`. O polimorfismo permite que diferentes objetos (cachorro ou gato) se comportem de maneira diferente, mesmo quando usados com a mesma interface.

# Esses são exemplos simples para ilustrar os pilares da POO em Python. Através do encapsulamento, herança e polimorfismo, é possível criar estruturas de código mais flexíveis, reutilizáveis e organizadas.