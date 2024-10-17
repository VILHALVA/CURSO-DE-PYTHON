# ESTRUTURA CONDICIONAL
A estrutura condicional em Python permite que você controle o fluxo de execução do seu programa com base em condições lógicas. Aqui está uma visão geral da estrutura condicional em Python:

## **Condições Simples (if)**
A estrutura `if` permite que você execute um bloco de código se uma condição for verdadeira. Se a condição não for atendida, o bloco de código dentro do `if` não será executado.

```python
idade = 18

if idade >= 18:
    print("Você é maior de idade.")
```

## **Condições Compostas (if-else)**
Com a estrutura `if-else`, você pode executar um bloco de código se a condição for verdadeira e outro bloco se a condição for falsa.

```python
idade = 16

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
```

## **Condições Encadeadas (if-elif-else)**
Com a estrutura `if-elif-else`, você pode testar várias condições em sequência. O bloco associado à primeira condição verdadeira será executado, e os blocos restantes serão ignorados.

```python
nota = 75

if nota >= 90:
    print("A")
elif nota >= 80:
    print("B")
elif nota >= 70:
    print("C")
else:
    print("D")
```

## **Expressões Condicionais (Operador ternário)**
Python também suporta uma forma compacta de estrutura condicional chamada operador ternário.

```python
idade = 20
status = "Maior de idade" if idade >= 18 else "Menor de idade"
print(status)
```

## **Condicionais Aninhadas**
Você pode aninhar estruturas condicionais dentro de outras estruturas condicionais para testar condições mais complexas.

```python
idade = 20
sexo = "F"

if idade >= 18:
    if sexo == "M":
        print("Homem adulto")
    else:
        print("Mulher adulta")
else:
    print("Menor de idade")
```

## **Considerações Importantes:**
- A indentação é crucial em Python. O código dentro de um bloco condicional deve ser indentado corretamente para ser reconhecido como parte desse bloco.
- Você pode usar operadores lógicos como `and`, `or` e `not` para criar condições mais complexas.
- A estrutura `if-elif-else` permite testar várias condições de forma eficiente.

Essa é uma visão geral da estrutura condicional em Python. Ela é uma ferramenta poderosa para controlar o fluxo do seu programa com base em diferentes condições lógicas.