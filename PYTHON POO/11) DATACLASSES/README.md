# SOBRE DATACLASSE:
Uma `dataclasse` é uma classe especial no Python que é projetada para simplificar a criação de classes de dados. Essas classes são principalmente utilizadas para representar dados e não possuem métodos além dos métodos padrão como `__init__()`, `__repr__()`, e `__eq__()`. A funcionalidade de `dataclasse` foi introduzida no Python 3.7 e oferece uma maneira conveniente de criar classes de dados imutáveis.

Para criar uma classe de dados usando `dataclass`, você deve decorar a classe com o decorador `@dataclass` e definir os campos (atributos) que deseja incluir. O Python automaticamente cria métodos especiais, como `__init__()`, `__repr__()`, e `__eq__()`, com base nos campos definidos. Aqui está um exemplo simples:

```python
from dataclasses import dataclass

@dataclass
class Ponto:
    x: int
    y: int

# Criando objetos da classe de dados
p1 = Ponto(1, 2)
p2 = Ponto(1, 2)

# Imprimindo os objetos
print(p1)  # Output: Ponto(x=1, y=2)

# Comparando objetos
print(p1 == p2)  # Output: True
```

Observe que, ao usar `@dataclass`, você não precisa escrever manualmente os métodos `__init__()`, `__repr__()`, e `__eq__()`. O Python os cria automaticamente com base nos campos que você definiu na classe.

As classes de dados criadas com `@dataclass` são imutáveis por padrão, o que significa que, depois de criar um objeto, seus atributos não podem ser alterados. Se você desejar que seus objetos sejam mutáveis, você pode adicionar o decorador `mutable` antes de `@dataclass`.

As `dataclasses` são úteis quando você precisa criar rapidamente classes simples para representar dados, como registros, estruturas ou objetos de transferência de dados (DTOs), economizando o trabalho de escrever os métodos comuns de inicialização, representação e igualdade.

* [SAIBA MAIS](https://docs.python.org/pt-br/3.7/library/dataclasses.html)