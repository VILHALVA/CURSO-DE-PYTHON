# COMANDOS DE ENTRADA E OPERADORES ARITMÉTICOS
Vamos continuar explorando os fundamentos da programação com comandos de entrada e operadores aritméticos:

## **Comandos de Entrada (Input):**
Os comandos de entrada permitem que um programa receba dados fornecidos pelo usuário ou por outra fonte de entrada. Em Python, podemos utilizar a função `input()` para isso. Veja um exemplo simples de como usar o comando `input()` para receber um número inteiro do usuário:

```python
# Recebendo um número inteiro do usuário
numero = int(input("Digite um número inteiro: "))
print("Você digitou:", numero)
```

Neste exemplo:

1. Usamos `input()` para solicitar ao usuário que digite um número inteiro.
2. Utilizamos `int(input())` para converter a entrada em um número inteiro e armazená-lo na variável `numero`.
3. Em seguida, usamos `print()` para mostrar o número de volta ao usuário.

## **Operadores Aritméticos:**
Os operadores aritméticos são usados para realizar operações matemáticas em números. Os operadores aritméticos mais comuns incluem:

1. **Adição (+):** Usado para somar dois valores. Exemplo: `5 + 3` resulta em `8`.

2. **Subtração (-):** Usado para subtrair o valor à direita do valor à esquerda. Exemplo: `7 - 2` resulta em `5`.

3. **Multiplicação (*):** Usado para multiplicar dois valores. Exemplo: `4 * 6` resulta em `24`.

4. **Divisão (/):** Usado para dividir o valor à esquerda pelo valor à direita. Exemplo: `10 / 2` resulta em `5`.

5. **Módulo (%):** Usado para obter o resto da divisão do valor à esquerda pelo valor à direita. Exemplo: `10 % 3` resulta em `1`, pois 10 dividido por 3 tem um resto de 1.

6. **Incremento (++) e Decremento (--):** Em Python, os operadores de incremento e decremento são representados por `+= 1` e `-= 1`, respectivamente.

Aqui está um exemplo de como usar operadores aritméticos em Python:

```python
# Realizando várias operações aritméticas com números fornecidos pelo usuário
a = int(input("Digite o valor de 'a': "))
b = int(input("Digite o valor de 'b': "))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)
print("Resto da divisão:", resto)
```

Neste exemplo, o programa lê dois números inteiros do usuário, realiza várias operações aritméticas com eles e exibe os resultados.

Comandos de entrada e operadores aritméticos são blocos de construção fundamentais para a criação de algoritmos e programas que realizam cálculos e interagem com o usuário. Eles são amplamente utilizados em tarefas de processamento de dados e resolução de problemas.