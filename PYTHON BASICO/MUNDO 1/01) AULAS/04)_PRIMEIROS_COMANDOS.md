# PRIMEIROS COMANDOS
Ótimo! Vamos começar com alguns dos primeiros comandos e conceitos básicos do Python. Python é uma linguagem de programação conhecida por sua simplicidade e legibilidade. Vamos dar uma olhada em algumas operações simples para começar:

## 1. Imprimindo no Console:
O comando `print()` é usado para exibir mensagens ou valores no console. Isso é muito útil para depurar seu código e ver o que está acontecendo.

```python
print("Olá, mundo!")
```

## 2. Variáveis e Tipos de Dados:
Em Python, você não precisa declarar explicitamente o tipo de uma variável. O interpretador Python deduz o tipo com base no valor atribuído.

```python
# Declarando variáveis
nome = "João"
idade = 30
altura = 1.75

# Exibindo variáveis
print(nome)
print(idade)
print(altura)
```

## 3. Operações Matemáticas:
Você pode realizar operações matemáticas simples em Python, como adição, subtração, multiplicação e divisão.

```python
a = 10
b = 5

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b

print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)
```

## 4. Estruturas de Controle:
Python suporta estruturas de controle como condicionais (if-else) e loops (for, while). Aqui está um exemplo simples:

```python
idade = 18

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
```

## 5. Listas:
Listas são uma coleção ordenada de elementos que podem conter diferentes tipos de dados.

```python
frutas = ["maçã", "banana", "laranja"]
print(frutas[0])  # Acessando o primeiro elemento
print(frutas[1])  # Acessando o segundo elemento

# Adicionando um novo elemento à lista
frutas.append("morango")

# Iterando sobre os elementos da lista
for fruta in frutas:
    print(fruta)
```

## 6. Funções:
Você pode criar funções em Python para organizar e reutilizar seu código.

```python
def saudacao(nome):
    print("Olá, " + nome + "!")

saudacao("Maria")
```

Esses são apenas alguns dos conceitos e comandos básicos em Python. À medida que você se familiariza com esses fundamentos, poderá explorar tópicos mais avançados, como classes, objetos, tratamento de exceções e muito mais. A prática constante é a chave para se tornar proficiente em Python. Experimente e construa pequenos programas para consolidar seus conhecimentos.