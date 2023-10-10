# TIPOS PRIMITIVOS E SAIDA DE DADOS
Em Python, existem vários tipos primitivos que representam os tipos básicos de dados com os quais você pode trabalhar. Além disso, você pode usar a função `print()` para exibir dados na saída padrão. Neste artigo, exploraremos os tipos primitivos mais comuns e como exibir dados na saída em Python.

## Tipos Primitivos
### 1. Inteiro (`int`)

O tipo `int` é usado para representar números inteiros, como -1, 0, 1, 2, etc.

Exemplo:

```python
numero_inteiro = 42
```

### 2. Ponto Flutuante (`float`)
O tipo `float` é usado para representar números de ponto flutuante (números com casas decimais).

Exemplo:

```python
numero_decimal = 3.14159
```

### 3. String (`str`)
O tipo `str` é usado para representar texto, que deve ser cercado por aspas simples ou duplas.

Exemplo:

```python
texto = "Olá, Python!"
```

### 4. Booleano (`bool`)
O tipo `bool` é usado para representar valores booleanos, `True` (verdadeiro) ou `False` (falso).

Exemplo:

```python
verdadeiro = True
falso = False
```

## Saída de Dados com `print()`
Para exibir informações na saída padrão (normalmente a tela), você pode usar a função `print()`. Você pode passar uma ou mais expressões separadas por vírgulas para o `print()`.

Exemplo:

```python
nome = "Maria"
idade = 25
print("O nome é:", nome)
print("A idade é:", idade)
```

Isso produzirá a seguinte saída:

```
O nome é: Maria
A idade é: 25
```

Você também pode formatar a saída usando a formatação de string f (a partir do Python 3.6) ou usando o método `format()`.

Usando f-strings:

```python
nome = "Maria"
idade = 25
print(f"O nome é: {nome}")
print(f"A idade é: {idade}")
```

Usando o método `format()`:

```python
nome = "Maria"
idade = 25
print("O nome é: {}".format(nome))
print("A idade é: {}".format(idade))
```

Ambos os métodos produzirão a mesma saída.

## Conversão de Tipos
Às vezes, você precisa converter entre tipos primitivos. Por exemplo, converter um número inteiro em uma string ou vice-versa. Isso pode ser feito usando funções como `str()`, `int()`, `float()`, etc.

Exemplo:

```python
numero_inteiro = 42
numero_string = str(numero_inteiro)
```

Isso converte o número inteiro `42` em uma string `"42"`.

Em resumo, em Python, você pode trabalhar com tipos primitivos como inteiros, números de ponto flutuante, strings e booleanos. A função `print()` é usada para exibir dados na saída padrão, e você pode usar formatação de string ou o método `format()` para formatar a saída conforme necessário. A conversão entre tipos pode ser feita usando funções apropriadas.