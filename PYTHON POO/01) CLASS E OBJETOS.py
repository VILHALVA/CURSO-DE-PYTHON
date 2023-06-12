# Em Python, você pode criar classes usando a palavra-chave `class`. Por exemplo, vamos criar uma classe simples chamada `Pessoa`:

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")

# Nesse exemplo, a classe `Pessoa` possui dois atributos: `nome` e `idade`. O método `__init__` é um método especial chamado de construtor, que é executado automaticamente quando um objeto é criado a partir da classe. Ele recebe os parâmetros `nome` e `idade` e atribui esses valores aos atributos correspondentes do objeto.

# Além disso, a classe possui o método `saudacao`, que imprime uma mensagem de saudação com o nome e idade da pessoa.

# Para criar um objeto da classe `Pessoa` e acessar seus atributos e métodos, fazemos o seguinte:

pessoa1 = Pessoa("João", 25)
print(pessoa1.nome)  # Saída: João
print(pessoa1.idade)  # Saída: 25
pessoa1.saudacao()  # Saída: Olá, meu nome é João e eu tenho 25 anos.

# Aqui, criamos um objeto chamado `pessoa1` da classe `Pessoa`, passando os valores "João" e 25 para os parâmetros `nome` e `idade`. Em seguida, imprimimos os valores dos atributos `nome` e `idade` e chamamos o método `saudacao`.

# A POO em Python oferece recursos adicionais, como herança, encapsulamento e polimorfismo, que permitem criar hierarquias de classes, proteger dados e fornecer comportamento flexível e reutilizável.
