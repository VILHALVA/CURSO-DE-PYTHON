# AGREGAÇÃO
Agregação é um conceito em Programação Orientada a Objetos (POO) que descreve uma relação entre um objeto "todo" e um objeto "parte". Em uma relação de agregação, o objeto "todo" contém ou é composto por objetos "partes". A principal característica da agregação é que os objetos "partes" podem existir independentemente do objeto "todo". Vamos explorar a agregação em mais detalhes e como ela é implementada em Python.

**Características da Agregação:**

Aqui estão algumas características importantes da agregação:

1. **Independência:** Os objetos "partes" podem existir independentemente do objeto "todo". Isso significa que os objetos "partes" podem ser criados, modificados e destruídos sem afetar a existência do objeto "todo".

2. **Relação de "tem-um":** A agregação geralmente reflete uma relação de "tem-um", onde o objeto "todo" possui ou é composto por um ou mais objetos "partes". Por exemplo, uma classe `Carro` pode agregar objetos da classe `Motor` e `Rodas`.

3. **Forte Acoplamento Fraco:** Embora o objeto "todo" contenha objetos "partes", a relação é geralmente de acoplamento fraco, o que significa que as classes "todo" e "partes" não dependem estritamente uma da outra. Isso permite maior flexibilidade e facilidade de manutenção.

**Exemplo de Agregação:**

Vamos considerar um exemplo simples de agregação em Python: uma classe `Universidade` que possui várias instâncias da classe `Aluno`.

```python
class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

class Universidade:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

# Criar objetos de ambas as classes
aluno1 = Aluno("Alice", "A123")
aluno2 = Aluno("Bob", "B456")

universidade = Universidade("Universidade ABC")
universidade.adicionar_aluno(aluno1)
universidade.adicionar_aluno(aluno2)

# Acesso aos alunos por agregação
for aluno in universidade.alunos:
    print(f"{aluno.nome} ({aluno.matricula}) estuda na {universidade.nome}")
```

Neste exemplo, a classe `Universidade` agrega objetos da classe `Aluno` usando uma lista. Cada aluno é independente e pode existir fora da universidade, mas eles estão relacionados à universidade por meio da agregação.

**Benefícios da Agregação:**

- **Reutilização de código:** A agregação permite criar classes independentes que podem ser reutilizadas em diferentes contextos.

- **Modelagem de relacionamentos:** A agregação ajuda a modelar relacionamentos complexos entre objetos, refletindo a estrutura do mundo real.

- **Flexibilidade:** Os objetos "partes" podem ser adicionados ou removidos do objeto "todo" sem afetar a estrutura do programa.

A agregação é uma forma importante de estruturar relacionamentos entre objetos em POO e é útil para modelar relacionamentos de "tem-um" em sistemas de software. Ela ajuda a criar código mais organizado e flexível, permitindo a composição de objetos complexos a partir de objetos mais simples.