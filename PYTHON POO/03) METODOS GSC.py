# Em programação orientada a objetos, os métodos getters, setters e construtores são comumente usados para manipular os atributos de uma classe. Eles fornecem uma maneira de acessar e modificar os valores dos atributos de forma controlada. Vamos entender melhor cada um desses métodos em Python:

# 1. Construtor (Constructor):
# O construtor é um método especial usado para inicializar os atributos de um objeto quando ele é criado a partir de uma classe. Em Python, o construtor é definido pelo método `__init__`. Ele é executado automaticamente assim que um objeto é criado e permite que você passe argumentos para definir os valores iniciais dos atributos.

class Exemplo:
    def __init__(self, valor):
        self.atributo = valor

exemplo = Exemplo(10)
print(exemplo.atributo)  # Saída: 10

# No exemplo acima, a classe `Exemplo` possui um atributo chamado `atributo`. O construtor recebe um argumento `valor` e atribui esse valor ao atributo `atributo` do objeto sendo criado.

# 2. Getter (Método de Acesso):
# Um getter é um método usado para obter o valor de um atributo de uma classe. Em Python, os getters são criados usando o decorador `@property`. Isso permite que você acesse o valor do atributo como se fosse um atributo de instância, sem a necessidade de chamar explicitamente um método.

class Exemplo:
    def __init__(self, valor):
        self._atributo = valor

    @property
    def atributo(self):
        return self._atributo

exemplo = Exemplo(20)
print(exemplo.atributo)  # Saída: 20

# No exemplo acima, a classe `Exemplo` possui um atributo protegido `_atributo`. O getter `atributo` retorna o valor desse atributo. Ao acessar `exemplo.atributo`, o valor é retornado diretamente.

# 3. Setter (Método de Modificação):
# Um setter é um método usado para modificar o valor de um atributo de uma classe. Em Python, os setters são criados usando o decorador `@nome_atributo.setter`. Isso permite que você defina o valor do atributo como se estivesse atribuindo diretamente a ele.

class Exemplo:
    def __init__(self, valor):
        self._atributo = valor

    @property
    def atributo(self):
        return self._atributo

    @atributo.setter
    def atributo(self, novo_valor):
        self._atributo = novo_valor

exemplo = Exemplo(30)
exemplo.atributo = 40
print(exemplo.atributo)  # Saída: 40

# No exemplo acima, além do getter `atributo`, também definimos um setter para o atributo `_atributo`. O setter `atributo` permite modificar o valor do atributo diretamente, atribuindo um novo valor a `exemplo.atributo`.

# Os getters e setters fornecem uma camada de encapsulamento, permitindo que você controle o acesso aos atributos de uma classe. Ao usar esses métodos, você pode adicionar lógica personalizada ao processo de obtenção e definição de valores, como validação ou cálculos adicionais.

# Lembrando que, em Python, as convenções para getters e setters são mais flexíveis, e o acesso direto aos atributos é permitido. No entanto, é uma boa prática utilizar getters e setters para manter a coesão e a integridade do código.

# Essas são as noções básicas sobre construtores, getters e setters em Python. Eles são recursos poderosos na programação orientada a objetos para manipular os atributos de uma classe de forma controlada.