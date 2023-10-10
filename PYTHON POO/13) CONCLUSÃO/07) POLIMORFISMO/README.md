# Polimorfismo 
O **polimorfismo** é um dos pilares da Programação Orientada a Objetos (POO) e se refere à capacidade de objetos de classes diferentes responderem de maneira diferente a chamadas de métodos com o mesmo nome. Em Python, o polimorfismo é suportado por meio de mecanismos de sobreposição e sobrecarga de métodos.

## Sobreposição de Métodos
A **sobreposição de métodos** ocorre quando uma classe derivada (subclasse) fornece uma implementação específica para um método que já está definido em sua classe base (superclasse). Isso permite que a classe derivada substitua o comportamento do método da classe base.

Exemplo de sobreposição de método em Python:

```python
class Animal:
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "Au au!"
```

Neste exemplo, a classe `Cachorro` sobrepõe o método `fazer_som` da classe `Animal` para fornecer uma implementação específica.

## Sobrecarga de Métodos
A **sobrecarga de métodos** é a capacidade de uma classe ter múltiplas definições do mesmo método, mas com diferentes parâmetros. Em Python, a linguagem não suporta a sobrecarga de métodos como algumas outras linguagens, como Java. Em vez disso, o Python usa valores padrão para permitir flexibilidade nos argumentos dos métodos.

Exemplo de simulação de sobrecarga de método em Python:

```python
class Calculadora:
    def somar(self, a, b=0):
        return a + b

calc = Calculadora()

resultado1 = calc.somar(5)
resultado2 = calc.somar(3, 4)

print(resultado1)  # Output: 5
print(resultado2)  # Output: 7
```

Neste exemplo, o método `somar` da classe `Calculadora` pode aceitar um ou dois argumentos, simulando a sobrecarga de método usando valores padrão.

## Polimorfismo em Ação
O polimorfismo permite que objetos de classes diferentes sejam tratados de maneira semelhante, independentemente de sua classe real. Isso é útil ao chamar métodos comuns em objetos diferentes.

Exemplo de polimorfismo em Python:

```python
def fazer_som_do_animal(animal):
    return animal.fazer_som()

cachorro = Cachorro()
gato = Gato()

print(fazer_som_do_animal(cachorro))  # Output: "Au au!"
print(fazer_som_do_animal(gato))      # Output: "Miau!"
```

Neste exemplo, a função `fazer_som_do_animal` aceita objetos de classes diferentes e chama o método `fazer_som`, independentemente da classe real do objeto.

## Conclusão
O polimorfismo em Python permite que objetos de classes diferentes se comportem de maneira semelhante ao responder a chamadas de métodos com o mesmo nome. Isso torna o código mais flexível e fácil de manter, permitindo que você crie código genérico que funcione com várias classes.
