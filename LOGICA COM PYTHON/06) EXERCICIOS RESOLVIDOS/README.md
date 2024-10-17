# EXERCICIOS RESOLVIDOS
Aqui estão os exercícios resolvidos em Python:

## **1) Quantas velas no bolo de aniversário?**
```python
# Programa para determinar quantas velas serão colocadas no bolo de aniversário
def quantidade_de_velas():
    idade = int(input("Quantos anos a Cleuza fez no aniversário? "))
    print(f"Cleuza deve botar {idade} velas no bolo de aniversário.")

quantidade_de_velas()
```

## **2) Conversão de Reais para Dólares:**
```python
# Programa para converter Reais em Dólares
def conversao_reais_para_dolares():
    valor_reais = float(input("Informe o valor em reais: "))
    taxa_cambio = float(input("Informe a taxa de câmbio (valor de 1 real em dólares): "))
    
    valor_dolares = valor_reais / taxa_cambio
    
    print(f"Cleuza terá aproximadamente ${valor_dolares:.2f} em dólares.")

conversao_reais_para_dolares()
```

## **3) Conversão de Temperatura Fahrenheit para Celsius:**
```python
# Programa para converter temperatura de Fahrenheit para Celsius
def conversao_fahrenheit_para_celsius():
    temperatura_fahrenheit = float(input("Informe a temperatura em graus Fahrenheit: "))
    
    temperatura_celsius = (temperatura_fahrenheit - 32) * 5/9
    
    print(f"A temperatura em graus Celsius é de {temperatura_celsius:.2f}°C.")

conversao_fahrenheit_para_celsius()
```

## **4) Cálculo de Imposto de 60% sobre a Muamba:**
```python
# Programa para calcular o imposto de 60% sobre a Muamba
def calculo_imposto_muamba():
    valor_produto = float(input("Informe o valor total dos produtos de Muamba: "))
    
    imposto = valor_produto * 0.60
    
    print(f"O valor do imposto a ser pago é de R${imposto:.2f}.")

calculo_imposto_muamba()
```

## **5) Pagamento de Empréstimo com Juros de 20%:**
```python
# Programa para calcular o pagamento de um empréstimo com juros de 20%
def pagamento_emprestimo():
    valor_emprestimo = float(input("Informe o valor do empréstimo: "))
    
    juros = valor_emprestimo * 0.20
    valor_total = valor_emprestimo + juros
    
    print(f"Cleuza deve pagar um total de R${valor_total:.2f} considerando 20% de juros.")

pagamento_emprestimo()
```

Estes programas em Python resolvem cada uma das questões apresentadas, permitindo que Cleuza calcule a quantidade de velas, faça conversões de moeda, temperatura, calcule impostos e pagamentos de empréstimo com juros. Cada programa solicita as informações necessárias ao usuário e fornece o resultado correspondente.