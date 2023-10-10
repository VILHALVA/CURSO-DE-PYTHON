# METODOS DE CLASSE
Métodos de classe são funções que estão associadas a uma classe em vez de uma instância específica dessa classe. Eles são declarados usando o decorador `@classmethod` antes da definição do método e têm acesso à própria classe, não às instâncias individuais da classe. Métodos de classe são frequentemente usados para criar utilitários relacionados à classe e para realizar tarefas que não dependem do estado específico da instância. Vamos explorar como criar e usar métodos de classe em Python.

**Definindo um Método de Classe:**

Para definir um método de classe em Python, você precisa usar o decorador `@classmethod` antes da definição do método. Por convenção, o primeiro parâmetro de um método de classe é chamado de `cls`, que se refere à própria classe. Você pode acessar a classe e seus atributos estáticos usando `cls`. Aqui está um exemplo:

```python
class MinhaClasse:
    atributo_estatico = "Sou um atributo estático"

    def __init__(self, valor):
        self.valor = valor

    @classmethod
    def metodo_de_classe(cls):
        print(f"Este é um método de classe. Acessando o atributo estático: {cls.atributo_estatico}")

# Criar uma instância da classe
objeto = MinhaClasse("algum valor")

# Chamar o método de classe
MinhaClasse.metodo_de_classe()
```

Neste exemplo, `metodo_de_classe` é um método de classe que pode acessar o atributo estático `atributo_estatico` e imprimir seu valor.

**Usando Métodos de Classe:**

Os métodos de classe podem ser chamados diretamente na classe, sem a necessidade de criar uma instância da classe. Eles também podem ser chamados em instâncias da classe, mas eles compartilham o mesmo comportamento. Aqui estão exemplos de ambas as formas de uso:

```python
# Chamando o método de classe diretamente na classe
MinhaClasse.metodo_de_classe()

# Criando uma instância e chamando o método de classe nela
objeto = MinhaClasse("algum valor")
objeto.metodo_de_classe()
```

Ambos os casos produzirão a mesma saída, acessando o atributo estático da classe.

**Utilizando Métodos de Classe para Construir Objetos Alternativos:**

Uma aplicação comum de métodos de classe é fornecer construtores alternativos para criar objetos de uma classe com diferentes inicializações. Isso é útil quando você deseja criar objetos de uma classe de maneira flexível. Veja um exemplo:

```python
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def origem(cls):
        return cls(0, 0)

    @classmethod
    def ponto_medio(cls, ponto1, ponto2):
        return cls((ponto1.x + ponto2.x) / 2, (ponto1.y + ponto2.y) / 2)

# Construindo um objeto Ponto com o método de classe origem
ponto_origem = Ponto.origem()

# Construindo um objeto Ponto com o método de classe ponto_medio
ponto_medio = Ponto.ponto_medio(Ponto(1, 2), Ponto(3, 4))

print(f"Ponto Origem: ({ponto_origem.x}, {ponto_origem.y})")
print(f"Ponto Médio: ({ponto_medio.x}, {ponto_medio.y})")
```

Neste exemplo, `origem` e `ponto_medio` são métodos de classe que permitem criar objetos da classe `Ponto` com inicializações diferentes.

Métodos de classe são úteis quando você precisa realizar tarefas que não dependem do estado da instância, quando deseja fornecer construtores alternativos ou quando precisa interagir com atributos estáticos da classe. Eles são uma ferramenta flexível para lidar com tarefas relacionadas à classe em Python.