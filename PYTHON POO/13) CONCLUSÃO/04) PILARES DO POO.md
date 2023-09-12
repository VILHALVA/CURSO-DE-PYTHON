# Pilares da Programação Orientada a Objetos (POO) 
A Programação Orientada a Objetos (POO) é um paradigma de programação que se baseia em quatro pilares fundamentais: encapsulamento, abstração, herança e polimorfismo. Esses pilares são a base para a criação de classes e objetos em Python e outras linguagens de programação orientadas a objetos. Neste guia, exploraremos cada um desses pilares em Python.

## 1. Encapsulamento
**Encapsulamento** é o conceito de ocultar os detalhes de implementação internos de um objeto e expor apenas uma interface pública para interagir com o objeto. Em Python, o encapsulamento é baseado em convenções de nomeação e não em restrições rígidas de acesso.

- Atributos ou métodos que começam com um sublinhado simples (por exemplo, `_atributo`) são considerados protegidos e devem ser tratados com cuidado.
- O uso de propriedades (getters e setters) pode ser usado para controlar o acesso e a modificação de atributos.

Exemplo de encapsulamento em Python:

```python
class Pessoa:
    def __init__(self, nome):
        self._nome = nome  # Atributo protegido

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome
```

## 2. Abstração
**Abstração** envolve a criação de classes que representam objetos do mundo real e a definição de suas características e comportamentos essenciais, enquanto oculta os detalhes de implementação menos relevantes.

- Classes abstratas e interfaces em Python são usadas para definir modelos de objetos que outras classes podem herdar ou implementar.

Exemplo de abstração em Python:

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "Au au!"

class Gato(Animal):
    def fazer_som(self):
        return "Miau!"
```

## 3. Herança
**Herança** é o mecanismo pelo qual uma classe pode herdar atributos e métodos de outra classe. Em Python, a herança é uma maneira de reutilizar código e criar uma hierarquia de classes.

- A classe derivada herda os atributos e métodos da classe base.
- Você pode substituir ou estender métodos da classe base na classe derivada.

Exemplo de herança em Python:

```python
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano):
        super().__init__(marca, modelo)
        self.ano = ano
```

## 4. Polimorfismo
**Polimorfismo** permite que objetos de classes diferentes sejam tratados de maneira semelhante, independentemente de sua classe real. Isso é alcançado por meio da implementação de métodos comuns em diferentes classes.

- O polimorfismo permite que você chame métodos em objetos sem se preocupar com a classe específica do objeto.

Exemplo de polimorfismo em Python:

```python
class Animal:
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "Au au!"

class Gato(Animal):
    def fazer_som(self):
        return "Miau!"

# Função polimórfica
def som_do_animal(animal):
    return animal.fazer_som()
```

## Conclusão
Os pilares da Programação Orientada a Objetos (POO) - encapsulamento, abstração, herança e polimorfismo - são fundamentais para a criação de classes e objetos em Python. Eles permitem criar código mais organizado, reutilizável e fácil de manter, seguindo as melhores práticas de POO.