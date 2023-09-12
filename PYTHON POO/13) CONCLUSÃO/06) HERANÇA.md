# Herança 
A **herança** é um dos pilares da Programação Orientada a Objetos (POO) e é usada para criar uma hierarquia de classes, permitindo que uma classe derivada (subclasse) herde os atributos e métodos de uma classe base (superclasse). Em Python, a herança é uma maneira poderosa de reutilizar código e criar relacionamentos entre classes.

## Classe Base (Superclasse)
Uma **classe base** (ou superclasse) é a classe da qual outras classes derivadas herdam atributos e métodos. É a classe pai na hierarquia de classes.

Exemplo de uma classe base em Python:

```python
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        pass
```

## Classe Derivada (Subclasse)
Uma **classe derivada** (ou subclasse) é uma classe que herda atributos e métodos de uma classe base. Ela pode adicionar novos atributos e métodos ou sobrescrever (substituir) os métodos herdados.

Exemplo de uma classe derivada em Python:

```python
class Cachorro(Animal):
    def fazer_som(self):
        return "Au au!"

    def abanar_rabo(self):
        return f"{self.nome} está abanando o rabo."
```

Neste exemplo, a classe `Cachorro` herda da classe `Animal` e sobrescreve o método `fazer_som`. Além disso, adiciona um método novo, `abanar_rabo`.

## Chamando o Construtor da Classe Base
Ao criar uma instância da classe derivada, é importante chamar o construtor da classe base usando `super().__init__(...)` para garantir que os atributos da classe base sejam inicializados corretamente.

Exemplo de chamada ao construtor da classe base em Python:

```python
class Gato(Animal):
    def __init__(self, nome, cor_pelo):
        super().__init__(nome)
        self.cor_pelo = cor_pelo

    def fazer_som(self):
        return "Miau!"
```

## Polimorfismo
A herança também permite o uso de **polimorfismo**, onde objetos de classes diferentes podem ser tratados de maneira semelhante, independentemente de sua classe real. Isso é alcançado por meio da implementação de métodos comuns em diferentes classes.

Exemplo de polimorfismo em Python:

```python
def fazer_som_do_animal(animal):
    return animal.fazer_som()

cachorro = Cachorro("Rex")
gato = Gato("Whiskers", "Branco")

print(fazer_som_do_animal(cachorro))  # Output: "Au au!"
print(fazer_som_do_animal(gato))      # Output: "Miau!"
```

Neste exemplo, o método `fazer_som_do_animal` aceita objetos de classes diferentes e chama o método `fazer_som`, independentemente da classe real do objeto.

## Conclusão
A herança em Python é uma poderosa ferramenta que permite criar hierarquias de classes e reutilizar código de maneira eficiente. Ela também suporta polimorfismo, tornando o código mais flexível e fácil de manter.
