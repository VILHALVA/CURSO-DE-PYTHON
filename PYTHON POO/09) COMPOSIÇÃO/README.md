# COMPOSIÇÃO
A composição é um conceito importante na Programação Orientada a Objetos (POO) que descreve uma relação entre um objeto "todo" e objetos "partes" que são essenciais para o objeto "todo". Na composição, os objetos "partes" não podem existir independentemente do objeto "todo" e são criados, mantidos e destruídos junto com o objeto "todo". A composição é uma forma de criar objetos complexos por meio da combinação de objetos mais simples. Vamos explorar a composição em mais detalhes e como ela é implementada em Python.

**Características da Composição:**

Aqui estão algumas características importantes da composição:

1. **Dependência forte:** Na composição, os objetos "partes" dependem diretamente do objeto "todo" para sua existência e funcionamento. Eles não podem existir ou funcionar sem o objeto "todo".

2. **Relação de "tem-um":** A composição geralmente reflete uma relação de "tem-um", onde o objeto "todo" é composto por um ou mais objetos "partes". Por exemplo, uma classe `Carro` pode ser composta por objetos da classe `Motor`, `Rodas` e `Transmissao`.

3. **Acoplamento forte:** A composição envolve um acoplamento forte entre o objeto "todo" e os objetos "partes", o que significa que eles estão intimamente interligados. Alterações no objeto "todo" podem afetar diretamente os objetos "partes" e vice-versa.

**Exemplo de Composição:**

Vamos considerar um exemplo simples de composição em Python: uma classe `Carro` que é composta por objetos das classes `Motor`, `Rodas` e `Transmissao`.

```python
class Motor:
    def __init__(self, cilindrada):
        self.cilindrada = cilindrada

class Rodas:
    def __init__(self, quantidade):
        self.quantidade = quantidade

class Transmissao:
    def __init__(self, tipo):
        self.tipo = tipo

class Carro:
    def __init__(self, motor, rodas, transmissao):
        self.motor = motor
        self.rodas = rodas
        self.transmissao = transmissao

# Criar objetos de todas as classes
motor_do_carro = Motor(2000)
rodas_do_carro = Rodas(4)
transmissao_do_carro = Transmissao("Automática")

carro = Carro(motor_do_carro, rodas_do_carro, transmissao_do_carro)

# Acessar os componentes do carro por composição
print(f"Motor: {carro.motor.cilindrada} cc")
print(f"Rodas: {carro.rodas.quantidade}")
print(f"Transmissão: {carro.transmissao.tipo}")
```

Neste exemplo, a classe `Carro` é composta por objetos das classes `Motor`, `Rodas` e `Transmissao`. Esses objetos são criados junto com o objeto `Carro` e são essenciais para seu funcionamento.

**Benefícios da Composição:**

- **Encapsulamento:** A composição ajuda a encapsular a complexidade, permitindo que objetos sejam compostos a partir de objetos mais simples.

- **Reusabilidade:** A composição permite criar objetos complexos reutilizando objetos mais simples em diferentes contextos.

- **Modelagem precisa:** A composição ajuda a modelar objetos complexos refletindo a estrutura do mundo real, onde os objetos "partes" são essenciais para o objeto "todo".

A composição é uma forma importante de estruturar relacionamentos entre objetos em POO e é útil para modelar relacionamentos de "tem-um" onde os objetos "partes" são essenciais para o objeto "todo". Ela ajuda a criar objetos complexos de maneira organizada e encapsulada, facilitando a manutenção e a extensão do código.