# Classes e Objetos 
Python é uma linguagem de programação orientada a objetos (POO), o que significa que você pode criar classes para modelar objetos do mundo real e criar instâncias dessas classes para interagir com esses objetos. Neste guia, exploraremos os conceitos fundamentais de classes e objetos em Python.

## Definindo uma Classe
Em Python, uma classe é uma estrutura que define um conjunto de atributos e métodos que descrevem um tipo específico de objeto. Você pode definir uma classe da seguinte maneira:

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
```

Neste exemplo, definimos uma classe `Pessoa` com dois atributos: `nome` e `idade`. O método `__init__` é o construtor da classe, usado para inicializar os atributos.

## Criando um Objeto
Uma vez que uma classe está definida, você pode criar instâncias (objetos) dessa classe. Veja como criar um objeto da classe `Pessoa`:

```python
pessoa1 = Pessoa("Alice", 25)
pessoa2 = Pessoa("Bob", 30)
```

Aqui, criamos duas instâncias da classe `Pessoa`, cada uma com valores diferentes para os atributos `nome` e `idade`.

## Acessando Atributos e Métodos
Você pode acessar os atributos e métodos de um objeto usando a notação de ponto. Por exemplo, para acessar o atributo `nome` de `pessoa1`:

```python
print(pessoa1.nome)  # Output: "Alice"
```

Você também pode chamar métodos em um objeto da seguinte maneira:

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."

pessoa1 = Pessoa("Alice", 25)
mensagem = pessoa1.saudacao()
print(mensagem)  # Output: "Olá, meu nome é Alice e eu tenho 25 anos."
```

## Encapsulamento e Atributos Privados
Em Python, não existem atributos privados estritos, mas a convenção é usar um sublinhado simples (por exemplo, `_nome`) para indicar que um atributo deve ser tratado como protegido ou privado.

## Conclusão
Classes e objetos são fundamentais na programação orientada a objetos em Python. Eles permitem que você modele e interaja com objetos do mundo real em seu código, tornando-o mais organizado e legível.


