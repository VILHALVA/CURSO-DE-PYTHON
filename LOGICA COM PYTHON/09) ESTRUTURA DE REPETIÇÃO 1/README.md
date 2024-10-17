# ESTRUTURAS DE REPETIÇÃO - PARTE 1 
As estruturas de repetição "for" e "while" são utilizadas em programação para executar um bloco de código várias vezes com base em uma condição ou um número predefinido de iterações. Elas são fundamentais para automatizar tarefas que precisam ser repetidas, como processar uma lista de itens, realizar cálculos iterativos ou aguardar determinadas condições antes de continuar a execução do programa. Vamos explorar cada uma delas em Python:

## **Estrutura de Repetição "for":**
A estrutura de repetição "for" é utilizada quando você sabe exatamente quantas vezes deseja que um bloco de código seja executado. Ela é especialmente útil quando se trabalha com um intervalo específico de valores, como uma contagem de 1 a 10. A estrutura "for" em Python é composta por três partes principais:

1. **Inicialização:** Você define uma variável de controle e atribui a ela um valor inicial.

2. **Condição de Parada:** Você especifica a condição que determina quando o loop deve parar. O loop continuará a ser executado enquanto a condição for verdadeira.

3. **Incremento ou Decremento:** Você especifica como a variável de controle deve ser modificada a cada iteração, ou seja, como ela deve ser incrementada ou decrementada.

Exemplo de um loop "for" que imprime os números de 1 a 10:
```python
for i in range(1, 11):
    print(i, end=" ")
```

## **Estrutura de Repetição "while":**
A estrutura de repetição "while" é utilizada quando você não sabe antecipadamente quantas vezes um bloco de código deve ser executado, mas você executa o loop enquanto uma condição específica for verdadeira. A estrutura "while" em Python é composta por duas partes principais:

1. **Condição:** Você especifica uma condição que determina se o loop deve continuar a ser executado. O loop continuará enquanto a condição for verdadeira.

2. **Corpo do Loop:** Dentro do corpo do loop, você coloca o código que deve ser repetido enquanto a condição for verdadeira.

Exemplo de um loop "while" que imprime os números de 1 a 10:
```python
i = 1
while i <= 10:
    print(i, end=" ")
    i += 1
```

## **Diferenças e Escolha entre "for" e "while":**
- Use a estrutura "for" quando souber o número exato de iterações que deseja realizar e tiver um intervalo de valores definido.
- Use a estrutura "while" quando não souber quantas vezes o loop deve ser executado antecipadamente ou quando a condição de parada não for baseada em um intervalo definido.

Ambas as estruturas são poderosas e têm suas próprias aplicações. A escolha entre "for" e "while" depende dos requisitos específicos de seu programa e das condições sob as quais você deseja executar o código repetidamente.

## **EXERCÍCIOS RESOLVIDOS:**
Aqui estão as resoluções dos quatro exercícios utilizando as estruturas de repetição "while" e "for" em Python:

### **Exercício 1: Contagem Regressiva de 10 até 0 usando "while" e "for":**
Utilizando "while":
```python
contador = 10
while contador >= 0:
    print(contador, end=" ")
    contador -= 1
```

Utilizando "for":
```python
for contador in range(10, -1, -1):
    print(contador, end=" ")
```

### **Exercício 2: Introduzindo Loop com Castigo usando "while":**
```python
resposta = "nao"
while resposta == "nao":
    resposta = input("Você arrumou o quarto? (sim ou nao): ")
    if resposta == "nao":
        print("Você está de castigo!\n")
print("Você está liberado!")
```

### **Exercício 3: Contagem Personalizada (Crescente) usando "for":**
```python
inicio = int(input("Digite o valor de início: "))
fim = int(input("Digite o valor de fim: "))
for contador in range(inicio, fim + 1):
    print(contador, end=" ")
```

### **Exercício 4: Soma, Maior e Menor Valores usando "for":**
```python
quantidade = int(input("Quantos números deseja inserir? "))
soma = 0
maior = float("-inf")
menor = float("inf")
for i in range(quantidade):
    numero = float(input(f"Digite o {i+1}º número: "))
    soma += numero
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
print("Soma dos números:", soma)
print("Maior número:", maior)
print("Menor número:", menor)
```

Esses programas demonstram o uso das estruturas de repetição "while" e "for" em Python para realizar contagens regressivas, aplicar castigos, contar de forma personalizada e realizar cálculos de soma, maior e menor valores com base nas entradas do usuário. As estruturas de repetição são fundamentais para automatizar tarefas que precisam ser executadas várias vezes em um programa.