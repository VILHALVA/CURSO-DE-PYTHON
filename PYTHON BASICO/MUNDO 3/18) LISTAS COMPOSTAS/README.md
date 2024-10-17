# LISTAS COMPOSTAS
Listas compostas, também conhecidas como listas aninhadas, são listas que contêm outras listas ou sequências como seus elementos. Isso permite que você crie estruturas de dados mais complexas e organizadas em Python. Listas compostas são especialmente úteis quando você precisa armazenar dados relacionados ou tabelados. Vamos explorar como criar e usar listas compostas em Python.

## Criando Listas Compostas
Para criar uma lista composta, você pode colocar outras listas ou sequências dentro de uma lista principal. Aqui está um exemplo de uma lista composta:

```python
lista_composta = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

Neste exemplo, `lista_composta` é uma lista que contém três listas internas, cada uma representando uma linha de dados.

## Acessando Elementos de Listas Compostas
Você pode acessar elementos em listas compostas usando indexação múltipla. A primeira indexação obtém a lista interna e a segunda indexação obtém o elemento dentro dessa lista. Por exemplo:

```python
lista_composta = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
elemento = lista_composta[1][2]  # Obtém o elemento na segunda linha e terceira coluna (valor 6)
```

Você pode usar loops `for` aninhados para percorrer listas compostas:

```python
lista_composta = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for linha in lista_composta:
    for elemento in linha:
        print(elemento)
```

Este código imprimirá todos os elementos da lista composta.

## Modificando Listas Compostas
Você pode modificar elementos em listas compostas da mesma forma que em listas simples:

```python
lista_composta = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lista_composta[1][2] = 42  # Modifica o elemento na segunda linha e terceira coluna
```

## Adicionando Elementos em Listas Compostas
Você pode adicionar elementos a uma lista composta usando a função `append()`:

```python
lista_composta = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
nova_linha = [10, 11, 12]
lista_composta.append(nova_linha)  # Adiciona uma nova linha à lista composta
```

## Comprimento de Listas Compostas
Para obter o comprimento de uma lista composta (ou seja, o número de linhas), você pode usar a função `len()`:

```python
lista_composta = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
comprimento = len(lista_composta)  # Resultado: 3 (três linhas)
```

## Vantagens das Listas Compostas
- Organização: Listas compostas permitem organizar dados relacionados em uma estrutura de dados tabular.
- Flexibilidade: Elas podem conter elementos de diferentes tipos de dados.
- Aninhamento: Você pode criar estruturas de dados complexas aninhando várias listas.

As listas compostas são uma ferramenta poderosa em Python para lidar com dados tabulados, matrizes e estruturas de dados mais complexas. Elas são amplamente usadas para representar informações organizadas e relacionadas em muitos tipos diferentes de aplicativos.