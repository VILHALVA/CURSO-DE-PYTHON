# COMO DATACLASSES SÃO CRIADAS:
Vou criar alguns exemplos simples de classes em Python para ajudá-lo a entender como elas são criadas. Vamos começar com uma classe simples que representa uma pessoa:

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."

# Criando uma instância da classe Pessoa
pessoa1 = Pessoa("João", 30)

# Chamando um método da classe
mensagem = pessoa1.saudacao()
print(mensagem)
```

Neste exemplo, criamos a classe `Pessoa` com um construtor `__init__` que inicializa os atributos `nome` e `idade`. Também definimos um método `saudacao` que retorna uma saudação personalizada com base nos atributos da pessoa.

Aqui está outro exemplo que ilustra herança, onde criamos uma classe `Estudante` que herda da classe `Pessoa`:

```python
class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso

    def saudacao(self):
        return f"Olá, meu nome é {self.nome}, eu tenho {self.idade} anos e estou cursando {self.curso}."

# Criando uma instância da classe Estudante
estudante1 = Estudante("Maria", 22, "Ciência da Computação")

# Chamando o método saudacao da classe Estudante
mensagem = estudante1.saudacao()
print(mensagem)
```

Neste caso, a classe `Estudante` herda os atributos e métodos da classe `Pessoa` e também define um método `saudacao` próprio, que substitui o método da classe base.

Por fim, aqui está um exemplo que utiliza uma classe de dados (`dataclass`) para representar um livro:

```python
from dataclasses import dataclass

@dataclass
class Livro:
    titulo: str
    autor: str
    ano_publicacao: int

# Criando uma instância da classe de dados Livro
livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)

# Acessando os atributos da classe de dados
print(f"Título: {livro1.titulo}")
print(f"Autor: {livro1.autor}")
print(f"Ano de Publicação: {livro1.ano_publicacao}")
```

Neste exemplo, usamos a `dataclass` para criar uma classe de dados `Livro`, que tem três atributos. A `dataclass` automaticamente cria o método `__init__`, `__repr__` e outros métodos especiais para nós.

Esses exemplos devem ajudá-lo a entender como as classes são criadas em Python e como você pode definir atributos e métodos para representar objetos e suas funcionalidades.

* [SAIBA MAIS](https://youtu.be/0ERF7PFtcRo?si=6NkEerIuAgt6CQ7Z)