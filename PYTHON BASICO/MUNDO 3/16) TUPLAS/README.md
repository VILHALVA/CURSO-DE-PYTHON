# TUPLAS
Uma tupla é uma estrutura de dados em Python que permite armazenar um conjunto ordenado de elementos. A principal característica das tuplas é que elas são imutáveis, o que significa que, uma vez criadas, não é possível adicionar, remover ou alterar elementos dentro delas. As tuplas são frequentemente usadas quando você deseja armazenar um conjunto de valores que não devem ser modificados durante a execução do programa. Aqui está como criar e usar tuplas em Python:

## Criando uma Tupla
Você pode criar uma tupla especificando os elementos entre parênteses `()`, separados por vírgulas. Por exemplo:

```python
minha_tupla = (1, 2, 3, 4, 5)
```

Também é possível criar uma tupla sem parênteses, apenas separando os elementos por vírgulas:

```python
outra_tupla = 10, 20, 30
```

## Acessando Elementos de uma Tupla
Para acessar os elementos de uma tupla, você pode usar a indexação, começando com 0 para o primeiro elemento. Por exemplo:

```python
minha_tupla = (1, 2, 3, 4, 5)
primeiro_elemento = minha_tupla[0]  # Resultado: 1
```

Você também pode usar índices negativos para acessar elementos a partir do final da tupla:

```python
ultimo_elemento = minha_tupla[-1]  # Resultado: 5
```

## Tuplas São Imutáveis
Como mencionado anteriormente, tuplas são imutáveis. Isso significa que você não pode modificar, adicionar ou remover elementos de uma tupla após a criação. Tentar fazer isso resultará em um erro:

```python
minha_tupla = (1, 2, 3)
minha_tupla[0] = 10  # Isso resultará em um erro
```

Se você precisar modificar uma tupla, a única opção é criar uma nova tupla com os valores desejados.

## Desempacotando Tuplas
Você pode desempacotar os elementos de uma tupla em variáveis individuais:

```python
coordenadas = (10, 20, 30)
x, y, z = coordenadas
print(x)  # Resultado: 10
print(y)  # Resultado: 20
print(z)  # Resultado: 30
```

## Comprimento de uma Tupla
Você pode obter o comprimento de uma tupla usando a função `len()`:

```python
minha_tupla = (1, 2, 3, 4, 5)
comprimento = len(minha_tupla)  # Resultado: 5
```

## Usando Tuplas em Laços
Tuplas podem ser usadas em loops `for` para iterar através de seus elementos:

```python
frutas = ("maçã", "banana", "laranja")
for fruta in frutas:
    print(fruta)
```

## Vantagens das Tuplas
- Imutabilidade: É útil quando você quer ter certeza de que os dados não serão alterados acidentalmente.
- Desempacotamento: Permite que você atribua múltiplas variáveis de uma vez.
- Eficiência: Tuplas são mais eficientes em termos de espaço e tempo de execução do que listas quando se trata de armazenar elementos imutáveis.

As tuplas são uma estrutura de dados versátil em Python e são frequentemente usadas para representar coleções ordenadas de valores imutáveis. Elas são adequadas para situações em que a imutabilidade é importante e podem ser usadas de várias maneiras em seus programas.