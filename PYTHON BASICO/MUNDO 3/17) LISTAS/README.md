# LISTAS
Uma lista é uma estrutura de dados em Python que permite armazenar uma coleção ordenada de elementos. Ao contrário das tuplas, as listas são mutáveis, o que significa que você pode adicionar, remover ou alterar elementos dentro delas após a criação. As listas são uma das estruturas de dados mais versáteis em Python e são amplamente usadas em programação. Aqui está como criar e usar listas em Python:

## Criando uma Lista
Você pode criar uma lista especificando os elementos entre colchetes `[]`, separados por vírgulas. Por exemplo:

```python
minha_lista = [1, 2, 3, 4, 5]
```

## Acessando Elementos de uma Lista
Para acessar os elementos de uma lista, você pode usar a indexação, começando com 0 para o primeiro elemento. Por exemplo:

```python
minha_lista = [1, 2, 3, 4, 5]
primeiro_elemento = minha_lista[0]  # Resultado: 1
```

Você também pode usar índices negativos para acessar elementos a partir do final da lista:

```python
ultimo_elemento = minha_lista[-1]  # Resultado: 5
```

## Modificando Elementos de uma Lista
Como as listas são mutáveis, você pode modificar os elementos existentes:

```python
minha_lista = [1, 2, 3, 4, 5]
minha_lista[0] = 10
```

Agora, o primeiro elemento da lista é 10 em vez de 1.

## Adicionando Elementos a uma Lista
Você pode adicionar elementos a uma lista usando o método `append()`:

```python
minha_lista = [1, 2, 3]
minha_lista.append(4)
```

Agora, `minha_lista` contém `[1, 2, 3, 4]`.

## Removendo Elementos de uma Lista
Você pode remover elementos de uma lista usando métodos como `remove()`, `pop()`, ou `del`.

- `remove()`: Remove o primeiro elemento com um valor específico.

  ```python
  minha_lista = [1, 2, 3, 4, 5]
  minha_lista.remove(3)  # Remove o elemento 3
  ```

- `pop()`: Remove e retorna um elemento com um índice específico. Se nenhum índice for fornecido, remove o último elemento.

  ```python
  minha_lista = [1, 2, 3, 4, 5]
  elemento = minha_lista.pop(2)  # Remove o elemento no índice 2 (valor 3) e o armazena em 'elemento'
  ```

- `del`: Remove um elemento com um índice específico, mas não o retorna.

  ```python
  minha_lista = [1, 2, 3, 4, 5]
  del minha_lista[1]  # Remove o elemento no índice 1 (valor 2)
  ```

## Comprimento de uma Lista
Você pode obter o comprimento de uma lista usando a função `len()`:

```python
minha_lista = [1, 2, 3, 4, 5]
comprimento = len(minha_lista)  # Resultado: 5
```

## Listas em Laços
Listas podem ser usadas em loops `for` para iterar através de seus elementos:

```python
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta)
```

## Vantagens das Listas
- Mutabilidade: Você pode adicionar, remover e modificar elementos.
- Versatilidade: Listas podem conter elementos de diferentes tipos de dados.
- Flexibilidade: Listas podem ser usadas em muitos contextos, desde armazenar dados simples até representar estruturas de dados complexas.

As listas são uma estrutura de dados fundamental em Python e são amplamente usadas em programação para armazenar e manipular coleções de elementos. Elas são uma escolha versátil e poderosa para muitos tipos de tarefas de programação.