# MATRIZES (VARIAVEIS COMPOSTAS)
## CONCEITOS:
Em Python, assim como em muitas linguagens de programação, as matrizes são estruturas de dados bidimensionais que permitem armazenar uma coleção de elementos em linhas e colunas. Elas são usadas para representar dados tabulares, como tabelas, grades e outros tipos de informações organizadas em formato bidimensional. Aqui estão os conceitos-chave sobre matrizes em Python:

**Declaração de Matrizes:**

Para declarar uma matriz em Python, você pode usar listas aninhadas para representar as linhas e colunas da matriz. Aqui está um exemplo de declaração de matriz:

```python
matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
```

Neste exemplo, `matriz` é o nome da matriz, e suas dimensões são especificadas como 3 linhas e 3 colunas.

**Acesso a Elementos de Matrizes:**

Para acessar os elementos de uma matriz em Python, você usa o nome da matriz seguido de dois índices entre colchetes, um para a linha e outro para a coluna. Os índices indicam a posição do elemento na matriz. Aqui está um exemplo:

```python
matriz[1][2] = 42  # Define o elemento da segunda linha e terceira coluna como 42
x = matriz[0][0]  # Atribui o elemento da primeira linha e primeira coluna à variável x
```

**Tamanho de Matrizes:**

Você pode determinar o número de linhas e colunas de uma matriz usando a função `len()` para contar o número de linhas e o número de elementos em uma linha para obter o número de colunas. Por exemplo:

```python
linhas = len(matriz)  # Retorna o número de linhas da matriz
colunas = len(matriz[0])  # Retorna o número de colunas da matriz
```

**Inicialização de Matrizes:**

Você pode inicializar uma matriz ao declará-la, atribuindo valores diretamente aos elementos. Por exemplo:

```python
matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
```

**Operações com Matrizes:**

Você pode realizar várias operações com matrizes, como adição, subtração, multiplicação, transposição e outras operações matriciais. A manipulação de matrizes geralmente envolve loops e condicionais para percorrer e processar elementos.

**Exemplo de Loop com Matriz:**

Aqui está um exemplo de como usar dois loops "for" aninhados para percorrer e imprimir os elementos de uma matriz:

```python
for linha in matriz:
    for elemento in linha:
        print(elemento, end=' ')
    print()  # Move para a próxima linha após cada linha da matriz
```

Neste exemplo, dois loops "for" aninhados são usados para percorrer cada elemento da matriz e imprimir seu valor.

As matrizes são uma extensão poderosa das listas em Python e são amplamente usadas na programação para lidar com dados bidimensionais. Elas são úteis para representar informações tabulares, como planilhas, imagens, mapas e muito mais. O uso correto de matrizes pode simplificar a manipulação de dados estruturados em programas.

## EXERCICIOS:
* **01) LINHAS E COLUNAS:**
```python
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f"😎Digite o valor [{c+1}/{l+1}]: "))

for l in range(3):
    for c in range(3):
        print(f"[{matriz[l][c]:^5}]", end="")
    print()
```

* **02) PAR E IMPA:**
```python
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f"😎Digite o valor[{c+1}/{l+1}]: "))

for l in range(3):
    for c in range(3):
        if matriz[l][c] % 2 == 0:
            print(f"[{matriz[l][c]:^4}]", end="")
        else:
            print(f"({matriz[l][c]:^4})", end="")
    print()
```

* **03) QUARTA ORDEM:**
```python
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_diagonal_principal = 0

for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f"😎Digite o valor[{c+1}/{l+1}]: "))

    if l == c:
        soma_diagonal_principal += matriz[l][c]

print(f"⭐A soma da diagonal principal é {soma_diagonal_principal}")
```