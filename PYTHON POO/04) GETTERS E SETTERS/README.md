# GETTERS E SETTERS
Getters e setters são métodos especiais usados em Programação Orientada a Objetos (POO) para controlar o acesso e a modificação dos atributos de uma classe. Eles permitem que você defina regras específicas para acessar e modificar os valores dos atributos de uma instância da classe. Vamos explorar como criar getters e setters em Python.

**Getters:**

Os getters são métodos usados para obter o valor de um atributo de uma classe. Eles geralmente têm nomes como `get_nome_do_atributo` e são usados para retornar o valor do atributo correspondente. Aqui está um exemplo:

```python
class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    def get_nome(self):
        return self._nome

    def get_idade(self):
        return self._idade

# Criar uma instância da classe Pessoa
pessoa = Pessoa("Alice", 30)

# Obter os valores dos atributos usando os getters
nome = pessoa.get_nome()
idade = pessoa.get_idade()

print(f"Nome: {nome}, Idade: {idade}")
```

Neste exemplo, os métodos `get_nome` e `get_idade` são getters que permitem obter os valores dos atributos `_nome` e `_idade`, respectivamente.

**Setters:**

Os setters são métodos usados para definir (ou modificar) o valor de um atributo de uma classe. Eles geralmente têm nomes como `set_nome_do_atributo` e são usados para atribuir um novo valor ao atributo correspondente. Os setters também podem ser usados para aplicar validações ou regras específicas antes de atribuir um novo valor. Aqui está um exemplo:

```python
class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    def get_nome(self):
        return self._nome

    def set_nome(self, novo_nome):
        if novo_nome != "":
            self._nome = novo_nome

    def get_idade(self):
        return self._idade

    def set_idade(self, nova_idade):
        if nova_idade >= 0:
            self._idade = nova_idade

# Criar uma instância da classe Pessoa
pessoa = Pessoa("Alice", 30)

# Usar os setters para modificar os valores dos atributos
pessoa.set_nome("Bob")
pessoa.set_idade(25)

# Obter os valores dos atributos usando os getters
nome = pessoa.get_nome()
idade = pessoa.get_idade()

print(f"Nome: {nome}, Idade: {idade}")
```

Neste exemplo, os métodos `set_nome` e `set_idade` são setters que permitem modificar os valores dos atributos `_nome` e `_idade`, respectivamente. Eles também aplicam validações simples para garantir que os novos valores atendam a certos critérios.

**Propriedades:**

Em Python, é comum usar a propriedade (property) para definir getters e setters de forma mais elegante. As propriedades permitem que você acesse e modifique atributos como se fossem atributos públicos, mas ainda têm um controle de acesso e validações. Veja um exemplo:

```python
class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        if novo_nome != "":
            self._nome = novo_nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, nova_idade):
        if nova_idade >= 0:
            self._idade = nova_idade

# Criar uma instância da classe Pessoa
pessoa = Pessoa("Alice", 30)

# Usar as propriedades para modificar os valores dos atributos
pessoa.nome = "Bob"
pessoa.idade = 25

# Obter os valores dos atributos usando as propriedades
nome = pessoa.nome
idade = pessoa.idade

print(f"Nome: {nome}, Idade: {idade}")
```

Neste exemplo, as propriedades `nome` e `idade` substituem os métodos getters e setters e permitem um acesso mais natural aos atributos `_nome` e `_idade`.

Em resumo, getters e setters são métodos especiais usados para controlar o acesso e a modificação dos atributos de uma classe em Python. Eles podem ser definidos explicitamente como métodos ou usando propriedades para tornar o código mais elegante e legível. Eles são úteis para aplicar validações e lógica específica ao acesso e à modificação de atributos.