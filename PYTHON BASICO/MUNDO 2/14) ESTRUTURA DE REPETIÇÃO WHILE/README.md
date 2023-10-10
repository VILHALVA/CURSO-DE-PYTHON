# ESTRUTURA DE REPETIÇÃO WHILE
A estrutura de repetição `while` em Python é usada para criar loops que executam um bloco de código repetidamente enquanto uma condição específica for verdadeira. Essa estrutura permite que você crie loops com base em condições, e eles continuam a ser executados até que a condição seja avaliada como falsa. Aqui está a sintaxe básica do `while`:

```python
while condicao:
    # Código a ser executado enquanto a condição for verdadeira
```

- `condicao`: Uma expressão booleana que é avaliada antes de cada iteração. O loop continuará enquanto a condição for verdadeira.

## Exemplo Simples de `while`
Aqui está um exemplo simples que usa `while` para contar de 1 a 5:

```python
contador = 1

while contador <= 5:
    print(contador)
    contador += 1
```

Neste exemplo, o código dentro do loop `while` será executado repetidamente enquanto `contador` for menor ou igual a 5. A cada iteração, o valor de `contador` é incrementado em 1 até que a condição não seja mais verdadeira.

## Comando `break` com `while`
Dentro de um loop `while`, você pode usar o comando `break` para interromper o loop prematuramente, mesmo que a condição seja verdadeira.

Exemplo:

```python
contador = 1

while contador <= 10:
    if contador == 5:
        break
    print(contador)
    contador += 1
```

Neste exemplo, o loop `while` será interrompido quando `contador` for igual a 5, mesmo que a condição `contador <= 10` seja verdadeira.

## Comando `continue` com `while`
Você também pode usar o comando `continue` para pular a iteração atual e continuar com a próxima iteração do loop `while`.

Exemplo:

```python
contador = 1

while contador <= 5:
    if contador == 3:
        contador += 1
        continue
    print(contador)
    contador += 1
```

Neste exemplo, o loop `while` pula a iteração quando `contador` é igual a 3, usando o comando `continue`. Isso resulta na não impressão do número 3.

## `else` com `while`
Você pode usar a cláusula `else` com um loop `while`. O código no bloco `else` é executado quando a condição do loop se torna falsa.

Exemplo:

```python
contador = 1

while contador <= 5:
    print(contador)
    contador += 1
else:
    print("Loop concluído sem interrupções")
```

Neste exemplo, o bloco `else` será executado após o loop `while` quando `contador` não for mais menor ou igual a 5.

A estrutura de repetição `while` é útil quando você precisa executar um bloco de código com base em uma condição que pode mudar ao longo do tempo. Certifique-se de definir uma condição de parada adequada para evitar loops infinitos.