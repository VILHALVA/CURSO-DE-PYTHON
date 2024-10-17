# OPERADORES ARITMETICOS, LOGICOS E RELACIONAIS
## Operadores Aritméticos:
Os operadores aritméticos são usados para realizar operações matemáticas com operandos numéricos.

1. Adição (+): Soma dois operandos.
2. Subtração (-): Subtrai o segundo operando do primeiro.
3. Multiplicação (*): Multiplica dois operandos.
4. Divisão (/): Divide o primeiro operando pelo segundo.
5. Divisão Inteira (//): Divide o primeiro operando pelo segundo e retorna um número inteiro.
6. Módulo (%): Retorna o resto da divisão do primeiro operando pelo segundo.
7. Exponenciação (**): Calcula o primeiro operando elevado à potência do segundo.

Exemplo:
```python
a = 10
b = 3

print("Adição:", a + b)  # 10 + 3 = 13
print("Subtração:", a - b)  # 10 - 3 = 7
print("Multiplicação:", a * b)  # 10 * 3 = 30
print("Divisão:", a / b)  # 10 / 3 = 3.333...
print("Divisão Inteira:", a // b)  # 10 // 3 = 3
print("Módulo:", a % b)  # 10 % 3 = 1
print("Exponenciação:", a ** b)  # 10 ** 3 = 1000
```

## Operadores Lógicos:
Os operadores lógicos são usados para realizar operações lógicas em valores booleanos (True ou False).

1. E (and): Retorna True se ambos os operandos forem True.
2. Ou (or): Retorna True se pelo menos um dos operandos for True.
3. Não (not): Inverte o valor do operando booleano.

Exemplo:
```python
x = True
y = False

print("x and y:", x and y)  # True and False = False
print("x or y:", x or y)    # True or False = True
print("not x:", not x)       # not True = False
```

## Operadores Relacionais:
Os operadores relacionais são usados para comparar valores.

1. Igual a (==): Retorna True se os operandos forem iguais.
2. Diferente de (!=): Retorna True se os operandos forem diferentes.
3. Maior que (>): Retorna True se o primeiro operando for maior que o segundo.
4. Menor que (<): Retorna True se o primeiro operando for menor que o segundo.
5. Maior ou igual a (>=): Retorna True se o primeiro operando for maior ou igual ao segundo.
6. Menor ou igual a (<=): Retorna True se o primeiro operando for menor ou igual ao segundo.

Exemplo:
```python
a = 10
b = 5

print("a == b:", a == b)  # 10 == 5 = False
print("a != b:", a != b)  # 10 != 5 = True
print("a > b:", a > b)    # 10 > 5 = True
print("a < b:", a < b)    # 10 < 5 = False
print("a >= b:", a >= b)  # 10 >= 5 = True
print("a <= b:", a <= b)  # 10 <= 5 = False
```

Esses são os operadores aritméticos, lógicos e relacionais básicos em Python e como usá-los em seus programas.