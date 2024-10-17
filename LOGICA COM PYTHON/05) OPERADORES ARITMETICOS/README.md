# OPERADORES ARITMÉTICOS 
Neste exemplo, vamos continuar explorando os operadores aritméticos e criar um programa em Python para determinar se três valores digitados pelo usuário formam um triângulo e, em caso afirmativo, qual é o tipo de triângulo (equilátero, isósceles ou escaleno).

## **Operadores Aritméticos:**
Os operadores aritméticos são usados para realizar cálculos matemáticos. Aqui estão os principais operadores em Python:

- **Adição (+):** Soma dois valores.
- **Subtração (-):** Subtrai o valor à direita do valor à esquerda.
- **Multiplicação (*):** Multiplica dois valores.
- **Divisão (/):** Divide o valor à esquerda pelo valor à direita.
- **Módulo (%):** Retorna o resto da divisão do valor à esquerda pelo valor à direita.

## **Exemplo: Verificando o Tipo de Triângulo:**
```python
# Programa para verificar o tipo de triângulo

# Solicita ao usuário os comprimentos dos lados do triângulo
lado_a = float(input("Digite o comprimento do lado A: "))
lado_b = float(input("Digite o comprimento do lado B: "))
lado_c = float(input("Digite o comprimento do lado C: "))

# Verifica se os valores fornecidos formam um triângulo válido
if lado_a + lado_b > lado_c and lado_a + lado_c > lado_b and lado_b + lado_c > lado_a:
    # Verifica o tipo de triângulo
    if lado_a == lado_b == lado_c:
        print("É um triângulo equilátero.")
    elif lado_a == lado_b or lado_b == lado_c or lado_a == lado_c:
        print("É um triângulo isósceles.")
    else:
        print("É um triângulo escaleno.")
else:
    print("Não é um triângulo válido.")
```

Neste exemplo em Python, o programa solicita ao usuário os comprimentos dos três lados de um triângulo. Em seguida, ele verifica se os valores fornecidos formam um triângulo válido usando a desigualdade triangular.

Se os valores formarem um triângulo válido, o programa verifica o tipo de triângulo:

- Se todos os lados forem iguais, é um triângulo equilátero.
- Se pelo menos dois lados forem iguais, é um triângulo isósceles.
- Caso contrário, é um triângulo escaleno.

Esta implementação em Python fornece uma maneira prática e eficiente de determinar o tipo de triângulo com base nos comprimentos dos lados fornecidos pelo usuário.
