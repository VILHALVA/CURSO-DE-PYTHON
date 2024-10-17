# ESTRUTURAS CONDICIONAIS ANINHADAS 
As estruturas condicionais aninhadas em Python referem-se à incorporação de estruturas condicionais dentro de outras estruturas condicionais. Isso permite a criação de lógica complexa com base em múltiplas condições interdependentes, proporcionando uma maior flexibilidade na tomada de decisões em programas.

## **Resolução dos Exercícios Utilizando Condicionais Aninhadas:**
### **Exercício 1: Média do Aluno com Condições de Aprovação:**
```python
nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))

media = (nota1 + nota2) / 2
print("A média do aluno é:", media)

if media >= 7.0:
    print("Aluno aprovado.")
else:
    if media >= 5.0:
        print("Aluno em recuperação.")
    else:
        print("Aluno reprovado.")
```

Este programa calcula a média do aluno com base em suas notas e determina se o aluno está aprovado, em recuperação ou reprovado.

### **Exercício 2: Cálculo do Índice de Massa Corporal (IMC) com Classificação:**
```python
peso = float(input("Digite o peso em quilogramas: "))
altura = float(input("Digite a altura em metros: "))

imc = peso / (altura ** 2)
print("Seu IMC é:", imc)

if imc < 18.5:
    print("Você está abaixo do peso.")
else:
    if imc < 24.9:
        print("Seu peso está normal.")
    else:
        if imc < 29.9:
            print("Você está com sobrepeso.")
        else:
            print("Você está obeso.")
```

Este programa calcula o IMC do usuário e fornece uma classificação com base nos valores de IMC.

### **Exercício 3: Doação para o Criança Esperança com Base na Renda:**
```python
renda_mensal = float(input("Informe a sua renda mensal: "))

if renda_mensal <= 1000:
    valor_doacao = renda_mensal * 0.05
else:
    if renda_mensal <= 2000:
        valor_doacao = renda_mensal * 0.1
    else:
        valor_doacao = renda_mensal * 0.15

print("Sua doação para o Criança Esperança é de R$", valor_doacao)
```

Este programa calcula a quantidade de doação que uma pessoa deve fazer para o Criança Esperança com base em sua renda mensal. A taxa de doação varia dependendo da faixa de renda em que a pessoa se encontra.

Esses exemplos demonstram como as estruturas condicionais aninhadas em Python podem ser usadas para tomar decisões com base em múltiplas condições, criando lógica complexa e proporcionando uma maior flexibilidade na criação de programas.