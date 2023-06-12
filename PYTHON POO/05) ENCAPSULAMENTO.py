# Vou apresentar um exemplo de projeto simples que utiliza encapsulamento em Python. Neste caso, vamos criar um sistema de gerenciamento de funcionários, onde as informações dos funcionários são encapsuladas em uma classe e só podem ser acessadas por métodos específicos.

class Funcionario:
    def __init__(self, nome, salario):
        self.__nome = nome
        self.__salario = salario

    def get_nome(self):
        return self.__nome

    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    def get_salario(self):
        return self.__salario

    def set_salario(self, novo_salario):
        self.__salario = novo_salario


# Criando objetos de funcionário
funcionario1 = Funcionario("João", 2500)
funcionario2 = Funcionario("Maria", 3000)

# Acessando informações encapsuladas
print(funcionario1.get_nome())  # Saída: João
print(funcionario2.get_salario())  # Saída: 3000

# Modificando informações encapsuladas
funcionario1.set_nome("Pedro")
funcionario2.set_salario(3500)

print(funcionario1.get_nome())  # Saída: Pedro
print(funcionario2.get_salario())  # Saída: 3500

# Nesse exemplo, a classe `Funcionario` encapsula as informações dos funcionários, como o nome e o salário. Os atributos `__nome` e `__salario` são privados, o que significa que eles não podem ser acessados diretamente fora da classe. Em vez disso, métodos getter (`get_nome()` e `get_salario()`) e setter (`set_nome()` e `set_salario()`) são usados para acessar e modificar esses atributos de maneira controlada.

# Ao criar objetos de funcionário, os valores iniciais do nome e salário são definidos. Em seguida, podemos utilizar os métodos getter para obter essas informações encapsuladas. Da mesma forma, os métodos setter permitem modificar esses valores, garantindo que as validações necessárias possam ser aplicadas antes da atualização dos atributos.

# O encapsulamento nesse exemplo protege os dados dos funcionários, evitando que sejam modificados de forma incorreta ou acessados diretamente de fora da classe. Dessa forma, garantimos uma melhor organização e controle sobre as informações do sistema de gerenciamento de funcionários.