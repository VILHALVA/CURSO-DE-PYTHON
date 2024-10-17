# ATRIBUTOS DE CLASSE
Atributos de classe (ou variáveis de classe) são variáveis que pertencem à classe como um todo, em vez de pertencerem a instâncias individuais da classe. Isso significa que todos os objetos (instâncias) da classe compartilham o mesmo valor para um atributo de classe. Os atributos de classe são definidos dentro da classe, mas fora de qualquer método ou construtor, e são acessados usando a notação de ponto com o nome da classe ou da instância. Vamos explorar como definir e usar atributos de classe em Python.

**Definindo Atributos de Classe:**

Para definir um atributo de classe em Python, você simplesmente o declara dentro da classe, mas fora de qualquer método ou construtor. Eles são definidos na classe em si e não em instâncias individuais. Aqui está um exemplo:

```python
class Pessoa:
    # Atributo de classe
    especie = "Humano"

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Criar instâncias da classe Pessoa
pessoa1 = Pessoa("Alice", 30)
pessoa2 = Pessoa("Bob", 25)

# Acessar o atributo de classe usando a classe ou as instâncias
print(Pessoa.especie)  # Resultado: "Humano"
print(pessoa1.especie)  # Resultado: "Humano"
print(pessoa2.especie)  # Resultado: "Humano"
```

Neste exemplo, `especie` é um atributo de classe da classe `Pessoa`, e todos os objetos (instâncias) da classe compartilham o mesmo valor para esse atributo.

**Modificando Atributos de Classe:**

Os atributos de classe podem ser modificados diretamente na classe ou em instâncias da classe. Quando você modifica o valor de um atributo de classe, a mudança afeta todas as instâncias da classe. Aqui está um exemplo:

```python
# Modificar o valor do atributo de classe na classe
Pessoa.especie = "Ser Humano"

# Modificar o valor do atributo de classe em uma instância
pessoa1.especie = "Ser Voador"

# Acessar o atributo de classe usando a classe ou as instâncias
print(Pessoa.especie)  # Resultado: "Ser Humano"
print(pessoa1.especie)  # Resultado: "Ser Voador"
print(pessoa2.especie)  # Resultado: "Ser Humano"
```

Neste exemplo, o valor do atributo de classe `especie` é modificado tanto na classe `Pessoa` quanto na instância `pessoa1`, mas a instância `pessoa2` mantém o valor original.

**Usos Comuns de Atributos de Classe:**

Atributos de classe são úteis para armazenar informações que se aplicam a todas as instâncias de uma classe. Alguns usos comuns incluem:

1. Constantes compartilhadas: Valores que são constantes para todas as instâncias, como `PI` em uma classe de matemática.

2. Contadores: Variáveis que rastreiam informações sobre todas as instâncias, como o número total de instâncias criadas.

3. Configurações globais: Valores que afetam o comportamento de todas as instâncias, como configurações de aplicativos.

Atributos de classe são uma maneira útil de compartilhar informações e configurações entre todas as instâncias de uma classe em Python. Eles permitem que você evite a duplicação de dados e mantenham a coesão na organização de informações relacionadas a uma classe.