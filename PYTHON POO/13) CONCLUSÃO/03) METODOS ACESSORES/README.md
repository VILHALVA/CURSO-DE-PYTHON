# Métodos Acessores 
Em Python, os métodos acessores, também conhecidos como métodos getters e setters, são usados para controlar o acesso e a modificação de atributos de uma classe, mesmo que a linguagem não tenha modificadores de acesso estritos. Neste guia, exploraremos como criar e usar métodos acessores em Python.

## Métodos Getter
Os métodos getters são usados para obter o valor de um atributo privado de uma classe. Eles geralmente têm o formato `get_nome_do_atributo`. Aqui está um exemplo de um método getter em uma classe:

```python
class Pessoa:
    def __init__(self, nome):
        self._nome = nome

    def get_nome(self):
        return self._nome

# Criando uma instância da classe Pessoa
pessoa = Pessoa("Alice")

# Obtendo o nome usando o método getter
nome = pessoa.get_nome()
print(nome)  # Output: "Alice"
```

O método `get_nome` permite que você acesse o atributo `nome` de forma controlada.

## Métodos Setter
Os métodos setters são usados para definir um novo valor para um atributo privado de uma classe. Eles geralmente têm o formato `set_nome_do_atributo`. Aqui está um exemplo de um método setter em uma classe:

```python
class Pessoa:
    def __init__(self, nome):
        self._nome = nome

    def set_nome(self, novo_nome):
        self._nome = novo_nome

# Criando uma instância da classe Pessoa
pessoa = Pessoa("Alice")

# Definindo um novo nome usando o método setter
pessoa.set_nome("Bob")

# Obtendo o nome atual
nome = pessoa.get_nome()
print(nome)  # Output: "Bob"
```

O método `set_nome` permite que você modifique o atributo `nome` de forma controlada.

## Propriedades (Properties)
Em Python, você pode usar o decorador `@property` para criar propriedades que se comportam como atributos públicos, mas na verdade são métodos getters. Da mesma forma, você pode usar o decorador `@atributo.setter` para criar propriedades que se comportam como métodos setters.

Exemplo de uso de propriedades em Python:

```python
class Pessoa:
    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

# Criando uma instância da classe Pessoa
pessoa = Pessoa("Alice")

# Obtendo e definindo o nome usando propriedades
nome_atual = pessoa.nome
print(nome_atual)  # Output: "Alice"

pessoa.nome = "Bob"
novo_nome = pessoa.nome
print(novo_nome)  # Output: "Bob"
```

As propriedades permitem que você acesse e modifique atributos como se fossem atributos públicos.

## Conclusão
Métodos acessores em Python, como getters e setters, são usados para controlar o acesso e a modificação de atributos de classe de forma controlada. O uso de propriedades oferece uma sintaxe mais limpa para criar métodos getters e setters.