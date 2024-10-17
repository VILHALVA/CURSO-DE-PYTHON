# ESTRUTURAS CONDICIONAIS
As estruturas condicionais em Python são fundamentais para a tomada de decisões em programas. Elas permitem que você execute blocos de código com base em condições específicas, proporcionando flexibilidade e controle sobre o fluxo de execução. Neste README, vamos explorar as principais estruturas condicionais em Python e fornecer exemplos de como utilizá-las.

## **Principais Estruturas Condicionais em Python:**
### 1. **If (se... então...):**
O `if` permite que um bloco de código seja executado apenas se uma condição especificada for verdadeira.

Exemplo:
```python
idade = 20

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
```

### 2. **Else (senão...):**
O `else` é usado em conjunto com o `if` para executar um bloco de código alternativo se a condição não for verdadeira.

### 3. **Elif (senão se...):**
O `elif` permite adicionar mais condições para serem verificadas caso a condição anterior seja falsa.

### 4. **While (enquanto... faça...):**
O `while` executa um bloco de código repetidamente enquanto uma condição específica for verdadeira.

### 5. **For (para... em...):**
O `for` é usado para iterar sobre uma sequência (como uma lista ou intervalo) e executa um bloco de código um número específico de vezes.

## **Exercícios Resolvidos:**
Agora, vamos resolver os três exercícios propostos utilizando as estruturas condicionais em Python:

### **Exercício 1: Verificar Idade com base no Ano de Nascimento:**
```python
ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = 2024
idade = ano_atual - ano_nascimento

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
```

### **Exercício 2: Verificar se um Número é Par ou Ímpar:**
```python
numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
```

### **Exercício 3: Cálculo do Índice de Massa Corporal (IMC):**
```python
peso = float(input("Digite o peso em quilogramas: "))
altura = float(input("Digite a altura em metros: "))
imc = peso / (altura ** 2)

print("Seu IMC é:", imc)

if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc < 24.9:
    print("Seu peso está normal.")
elif imc < 29.9:
    print("Você está com sobrepeso.")
else:
    print("Você está obeso.")
```

Esses exemplos demonstram como as estruturas condicionais são utilizadas em Python para tomar decisões com base em condições específicas, proporcionando uma maior flexibilidade na criação de lógica em programas.