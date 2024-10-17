# ASSOCIAÇÃO
A associação é um dos princípios fundamentais da Programação Orientada a Objetos (POO) e descreve como objetos de diferentes classes interagem entre si. Na POO, os objetos se comunicam e colaboram uns com os outros por meio de associações. Vamos explorar o conceito de associação e como ela é implementada em Python.

**Associação entre Objetos:**

A associação ocorre quando um objeto de uma classe está relacionado a um objeto de outra classe. Isso pode ser feito de várias maneiras, incluindo:

1. **Atributos de referência:** Um objeto pode conter um atributo que faz referência a outro objeto de outra classe. Por exemplo, uma classe `Carro` pode ter um atributo que faz referência a um objeto da classe `Motor`.

2. **Parâmetros de métodos:** Um método de uma classe pode receber um objeto de outra classe como parâmetro. Por exemplo, uma classe `Loja` pode ter um método que recebe um objeto da classe `Cliente`.

3. **Métodos de acesso:** Um objeto pode acessar ou chamar métodos de outro objeto de outra classe. Por exemplo, uma classe `ContaBancaria` pode chamar métodos de uma classe `Cliente` para verificar informações sobre o titular da conta.

**Exemplo de Associação:**

Vamos considerar um exemplo simples de associação entre duas classes em Python: `Pessoa` e `Endereco`. Uma pessoa pode ter um endereço, e isso é uma relação de associação.

```python
class Endereco:
    def __init__(self, rua, numero, cidade):
        self.rua = rua
        self.numero = numero
        self.cidade = cidade

class Pessoa:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

# Criar objetos de ambas as classes
endereco = Endereco("Rua A", 123, "Cidade X")
pessoa = Pessoa("Alice", endereco)

# Acesso aos atributos por associação
print(f"{pessoa.nome} mora em {pessoa.endereco.rua}, {pessoa.endereco.numero}, {pessoa.endereco.cidade}")
```

Neste exemplo, uma instância da classe `Pessoa` está associada a uma instância da classe `Endereco` por meio do atributo `endereco`. Isso permite que você acesse informações de endereço de uma pessoa diretamente por associação.

**Benefícios da Associação:**

- **Reutilização de código:** A associação permite criar classes independentes que podem ser reutilizadas em diferentes contextos.

- **Abstração e modelagem realista:** A associação ajuda a modelar objetos no mundo real e a refletir relacionamentos entre eles em seu código.

- **Manutenção e extensibilidade:** As classes podem ser modificadas ou estendidas independentemente, facilitando a manutenção e a adição de novos recursos.

A associação é uma parte fundamental da POO e é usada para criar sistemas de software mais organizados, flexíveis e fáceis de manter. Ela permite que objetos de diferentes classes colaborem para realizar tarefas mais complexas e modelar relacionamentos do mundo real de forma eficaz.