# ESTRUTURA DE REPETIÇÃO FOR
A estrutura de repetição `for` é usada em Python para iterar (percorrer) uma sequência de elementos, como uma lista, tupla, string ou até mesmo um intervalo numérico. O `for` é uma estrutura de controle de fluxo que permite executar um bloco de código repetidamente para cada item na sequência. Vamos explorar como usar a estrutura de repetição `for` em Python.

## Sintaxe Básica do `for`
A sintaxe básica do `for` em Python é a seguinte:

```python
for elemento in sequencia:
    # Código a ser executado para cada elemento
```

- `elemento`: Uma variável que assume o valor de cada item na sequência a cada iteração.
- `sequencia`: A sequência de elementos a ser percorrida, como uma lista, tupla, string ou objeto iterável.

## Exemplo de Uso do `for` com uma Lista
Aqui está um exemplo simples de como usar o `for` para iterar através dos elementos de uma lista:

```python
frutas = ["maçã", "banana", "laranja", "uva"]

for fruta in frutas:
    print(fruta)
```

Neste exemplo, o `for` itera através da lista `frutas`, e a variável `fruta` assume o valor de cada elemento em cada iteração. O código dentro do loop `for` imprime cada fruta na lista.

## Exemplo de Uso do `for` com um Intervalo Numérico
Você também pode usar o `for` para iterar através de um intervalo numérico. O `range()` é uma função que gera uma sequência de números inteiros. Aqui está um exemplo:

```python
for i in range(5):
    print(i)
```

Este código imprimirá os números de 0 a 4.

## Comando `break` e `continue` com o `for`
Dentro de um loop `for`, você pode usar os comandos `break` e `continue` para controlar o fluxo de execução.

- `break`: Encerra o loop prematuramente se uma condição for atendida.

  Exemplo:

  ```python
  numeros = [1, 2, 3, 4, 5, 6]
  for numero in numeros:
      if numero == 4:
          break
      print(numero)
  ```

  Neste exemplo, o loop `for` será interrompido quando `numero` for igual a 4.

- `continue`: Pula a iteração atual e passa para a próxima.

  Exemplo:

  ```python
  numeros = [1, 2, 3, 4, 5, 6]
  for numero in numeros:
      if numero % 2 == 0:
          continue
      print(numero)
  ```

  Neste exemplo, o `continue` pula os números pares e imprime apenas os números ímpares.

## `else` com o `for`
Você também pode usar a cláusula `else` com um loop `for` em Python. O código no bloco `else` é executado quando o loop termina normalmente, ou seja, sem ser interrompido pelo comando `break`.

Exemplo:

```python
for i in range(5):
    print(i)
else:
    print("Loop concluído sem interrupções")
```

Neste exemplo, o bloco `else` será executado após o loop `for` imprimir os números de 0 a 4.

A estrutura de repetição `for` é uma ferramenta poderosa para iterar através de sequências de elementos em Python. Ela permite que você execute um bloco de código para cada item em uma sequência, facilitando o processamento de dados e a realização de tarefas repetitivas.