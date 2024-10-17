# CLASSES POO
Na programação orientada a objetos (POO), existem quatro pilares principais que guiam o design e a implementação das classes e objetos. Esses pilares são os princípios fundamentais que definem como as classes devem ser estruturadas e como os objetos interagem entre si. Aqui está uma explicação detalhada de cada um dos quatro pilares da POO:

1. **Abstração:**
   - Abstração é o conceito de representar características essenciais sem incluir os detalhes de implementação. Em POO, você define uma classe com atributos e métodos que encapsulam o comportamento desejado sem expor a complexidade interna.
   - Por exemplo, em um sistema de gerenciamento de biblioteca, você pode ter uma classe `Livro` que encapsula atributos como título, autor e ano de publicação, juntamente com métodos para emprestar, devolver e verificar disponibilidade.

    - Exemplo de código em Python:

    ```python
    class Veiculo:
        def __init__(self, marca, modelo):
            self.marca = marca
            self.modelo = modelo

        def dirigir(self):
            print(f"Dirigindo um {self.marca} {self.modelo}")

    # Criando uma instância da classe Veiculo
    carro = Veiculo("Toyota", "Corolla")
    carro.dirigir()  # Saída: Dirigindo um Toyota Corolla
    ```

    - Neste exemplo, a classe `Veiculo` representa um veículo genérico, com atributos como marca e modelo, e um método `dirigir()` para simular a ação de dirigir.

2. **Encapsulamento:**
   - Encapsulamento é o princípio de ocultar os detalhes internos de um objeto e fornecer uma interface clara para interagir com ele. Em Python, você pode controlar o acesso aos atributos e métodos de uma classe usando modificadores de acesso como `public`, `private` e `protected`.
   - Por exemplo, em uma classe `ContaBancaria`, você pode encapsular o saldo e as transações privadas, permitindo que os clientes acessem apenas métodos públicos para depositar, sacar e verificar o saldo.

    - Exemplo de código em Python:

    ```python
    class ContaBancaria:
        def __init__(self, saldo):
            self.__saldo = saldo

        def depositar(self, valor):
            self.__saldo += valor

        def sacar(self, valor):
            if valor <= self.__saldo:
                self.__saldo -= valor
                print(f"Saque de R${valor} realizado com sucesso.")
            else:
                print("Saldo insuficiente.")

        def get_saldo(self):
            return self.__saldo

    # Criando uma instância da classe ContaBancaria
    conta = ContaBancaria(1000)
    conta.depositar(500)
    conta.sacar(200)
    print("Saldo:", conta.get_saldo())  # Saída: Saldo: 1300
    ```

    - Neste exemplo, o saldo da conta bancária (`__saldo`) é encapsulado como um atributo privado, e o acesso a ele é feito por meio de métodos públicos como `depositar()` e `sacar()`.

3. **Herança:**
   - Herança é o princípio que permite que uma classe herde atributos e métodos de outra classe. Isso promove a reutilização de código e facilita a criação de classes mais especializadas a partir de classes mais genéricas.
   - Por exemplo, em um sistema de gerenciamento de funcionários, você pode ter uma classe `Funcionario` com atributos e métodos básicos, e então criar classes mais específicas como `Gerente` e `Programador` que herdam da classe `Funcionario` e adicionam funcionalidades adicionais.

   - Exemplo de código em Python:

    ```python
    class Animal:
        def __init__(self, nome):
            self.nome = nome

        def som(self):
            pass

    class Cachorro(Animal):
        def som(self):
            return "Au Au!"

    class Gato(Animal):
        def som(self):
            return "Miau!"

    # Criando instâncias das classes Cachorro e Gato
    cachorro = Cachorro("Rex")
    gato = Gato("Whiskers")

    print(cachorro.nome, "faz", cachorro.som())  # Saída: Rex faz Au Au!
    print(gato.nome, "faz", gato.som())          # Saída: Whiskers faz Miau!
    ```

    - Neste exemplo, as classes `Cachorro` e `Gato` herdam da classe `Animal`, que define o atributo `nome`. Cada subclasse implementa seu próprio método `som()` para retornar o som característico do animal.

4. **Polimorfismo:**
   - Polimorfismo é o princípio que permite que objetos de diferentes classes sejam tratados de maneira uniforme. Isso significa que você pode usar uma interface comum para operar em objetos de diferentes tipos.
   - Por exemplo, em uma aplicação de desenho, você pode ter classes como `Circulo` e `Retangulo`, cada uma com um método `desenhar()`. O polimorfismo permite que você chame o método `desenhar()` em um objeto sem se preocupar com o tipo específico, pois cada objeto sabe como se desenhar.

    - Exemplo de código em Python:

    ```python
    class Animal:
        def som(self):
            pass

    class Cachorro(Animal):
        def som(self):
            return "Au Au!"

    class Gato(Animal):
        def som(self):
            return "Miau!"

    def fazer_barulho(animal):
        print(animal.som())

    # Criando instâncias das classes Cachorro e Gato
    cachorro = Cachorro()
    gato = Gato()

    fazer_barulho(cachorro)  # Saída: Au Au!
    fazer_barulho(gato)      # Saída: Miau!
    ```

    - Neste exemplo, a função `fazer_barulho()` aceita qualquer objeto que seja uma instância da classe `Animal`, permitindo que você chame o método `som()` de forma polimórfica, independentemente do tipo de animal passado como argumento.

Esses quatro pilares da programação orientada a objetos são fundamentais para criar sistemas robustos, modulares e escaláveis. Ao aplicar esses princípios em seu código, você pode escrever software mais flexível, fácil de entender e fácil de manter.