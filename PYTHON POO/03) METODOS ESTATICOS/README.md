# METODOS ESTATICOS
Métodos estáticos (ou métodos de classe estáticos) são funções que pertencem a uma classe, mas não têm acesso aos atributos da instância nem à própria classe. Eles são definidos usando o decorador `@staticmethod` e não recebem automaticamente o primeiro parâmetro `self` ou `cls`. Em vez disso, eles são métodos independentes que não dependem do estado da instância ou da classe. Vamos explorar como criar e usar métodos estáticos em Python.

**Definindo um Método Estático:**

Para definir um método estático em Python, você usa o decorador `@staticmethod` antes da definição do método. Ao contrário dos métodos de instância (que recebem `self`) e dos métodos de classe (que recebem `cls`), os métodos estáticos não recebem automaticamente nenhum parâmetro relacionado à instância ou à classe. Eles podem ser chamados diretamente na classe ou em instâncias da classe, mas não têm acesso direto aos atributos da instância ou da classe. Aqui está um exemplo:

```python
class Matematica:
    @staticmethod
    def somar(a, b):
        return a + b

# Chamando o método estático diretamente na classe
resultado1 = Matematica.somar(5, 3)

# Criando uma instância e chamando o método estático nela
objeto = Matematica()
resultado2 = objeto.somar(10, 20)

print(resultado1)  # Resultado: 8
print(resultado2)  # Resultado: 30
```

**Usando Métodos Estáticos:**

Os métodos estáticos podem ser chamados diretamente na classe ou em instâncias da classe, como mostrado no exemplo acima. Eles são úteis quando você precisa de uma função relacionada à classe que não depende do estado da instância ou da classe em si.

**Quando Usar Métodos Estáticos:**

Aqui estão algumas situações em que os métodos estáticos são úteis:

1. Funções utilitárias relacionadas à classe: Métodos que não dependem de atributos da instância ou da classe e não precisam de acesso a esses atributos.

2. Funções independentes do contexto: Métodos que realizam cálculos ou operações independentes do contexto da classe.

3. Criação de funções de fábrica: Você pode usar métodos estáticos para criar objetos de uma classe de maneira flexível, fornecendo construtores alternativos.

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @staticmethod
    def criar_pessoa_com_idade_aleatoria():
        import random
        nome = "Pessoa Sem Nome"
        idade = random.randint(1, 100)
        return Pessoa(nome, idade)

# Criar uma pessoa com idade aleatória usando o método estático
pessoa_aleatoria = Pessoa.criar_pessoa_com_idade_aleatoria()
```

Em resumo, métodos estáticos em Python são funções associadas a uma classe que não dependem do estado da instância ou da classe e não recebem automaticamente parâmetros relacionados à instância ou à classe. Eles são úteis para funções utilitárias, operações independentes de contexto e construtores alternativos.