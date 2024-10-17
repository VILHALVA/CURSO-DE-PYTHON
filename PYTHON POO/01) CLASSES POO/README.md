# CLASSES POO
Programação Orientada a Objetos (POO) é um paradigma de programação que se baseia no conceito de "objetos" para organizar e estruturar o código. Em Python, como em muitas outras linguagens, você pode usar a POO para criar classes, que são modelos para a criação de objetos. Vamos explorar os conceitos fundamentais de classes e objetos em Python.

**Definindo uma Classe:**

Em Python, você define uma classe usando a palavra-chave `class`, seguida pelo nome da classe e um bloco de código indentado que contém atributos (variáveis) e métodos (funções) relacionados à classe. Aqui está um exemplo simples:

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."
```

Neste exemplo, criamos uma classe chamada `Pessoa` com um construtor `__init__` que inicializa os atributos `nome` e `idade`. Também definimos um método `saudacao` que retorna uma saudação personalizada com os atributos da pessoa.

**Criando Objetos:**

Uma vez que você tenha definido uma classe, pode criar objetos dessa classe. Objetos são instâncias da classe. Por exemplo:

```python
pessoa1 = Pessoa("Alice", 30)
pessoa2 = Pessoa("Bob", 25)
```

Aqui, criamos duas instâncias da classe `Pessoa`, `pessoa1` e `pessoa2`, com diferentes valores para `nome` e `idade`.

**Acessando Atributos e Métodos:**

Você pode acessar atributos e métodos de um objeto usando a notação de ponto:

```python
print(pessoa1.nome)  # Acessa o atributo 'nome' de pessoa1
print(pessoa2.idade)  # Acessa o atributo 'idade' de pessoa2
print(pessoa1.saudacao())  # Chama o método 'saudacao' de pessoa1
```

**Herança:**

A herança é um conceito importante na POO que permite criar classes derivadas (ou subclasses) com base em uma classe base (ou superclasse). As subclasses herdam atributos e métodos da superclasse e podem adicionar ou substituir comportamento. Aqui está um exemplo de herança em Python:

```python
class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def saudacao(self):
        return f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e minha matrícula é {self.matricula}."

aluno1 = Aluno("Carol", 20, "12345")
print(aluno1.saudacao())
```

Neste exemplo, criamos uma classe `Aluno` que herda de `Pessoa`. A classe `Aluno` adiciona um novo atributo `matricula` e substitui o método `saudacao` para incluir a matrícula.

**Encapsulamento:**

O encapsulamento é um princípio da POO que diz que os detalhes internos de uma classe devem ser ocultos para o mundo exterior. Em Python, você pode usar o conceito de "encapsulamento fraco" usando um sublinhado simples `_` antes de um atributo para indicar que ele não deve ser acessado diretamente de fora da classe. No entanto, o acesso ainda é possível, mas é uma convenção de que o atributo é "privado".

```python
class Livro:
    def __init__(self, titulo, autor):
        self._titulo = titulo
        self._autor = autor

    def obter_titulo(self):
        return self._titulo

    def obter_autor(self):
        return self._autor

livro = Livro("Python 101", "John Smith")
print(livro.obter_titulo())  # Acesso por método
print(livro._titulo)  # Acesso direto (não recomendado)
```

**Polimorfismo:**

O polimorfismo é outro conceito importante da POO, que permite que objetos de diferentes classes sejam tratados de maneira uniforme. Isso é alcançado por meio de métodos comuns ou interfaces. Python suporta polimorfismo naturalmente devido à sua tipagem dinâmica.

```python
def cumprimentar_pessoa(pessoa):
    print(pessoa.saudacao())

pessoa = Pessoa("Alice", 30)
aluno = Aluno("Bob", 25, "12345")

cumprimentar_pessoa(pessoa)
cumprimentar_pessoa(aluno)
```

Neste exemplo, a função `cumprimentar_pessoa` pode receber objetos de diferentes classes (uma pessoa ou um aluno) e chama o método `saudacao` de cada objeto de maneira uniforme.

A Programação Orientada a Objetos é uma abordagem poderosa para organizar e estruturar seu código, tornando-o mais reutilizável e manutenível. Python suporta totalmente a POO e oferece muitas facilidades para a criação e manipulação de objetos e classes.