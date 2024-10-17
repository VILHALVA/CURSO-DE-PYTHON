# OPERADORES LÓGICOS E RELACIONAIS 
Operadores lógicos e relacionais são fundamentais para a construção de algoritmos e programas de computador que envolvem tomada de decisões, controle de fluxo e avaliação de condições. Vamos explorar esses dois tipos de operadores em detalhes:

## **Operadores Relacionais (ou Comparação):**
Operadores relacionais são usados para comparar dois valores e determinar a relação entre eles. Eles retornam um valor booleano (verdadeiro ou falso) como resultado da comparação. Aqui estão os operadores relacionais mais comuns:

1. **Igual a (==):** Verifica se dois valores são iguais. Exemplo: `a == b` verifica se `a` é igual a `b`.

2. **Diferente de (!=):** Verifica se dois valores são diferentes. Exemplo: `a != b` verifica se `a` é diferente de `b`.

3. **Maior que (>):** Verifica se o valor à esquerda é maior que o valor à direita. Exemplo: `a > b` verifica se `a` é maior que `b`.

4. **Menor que (<):** Verifica se o valor à esquerda é menor que o valor à direita. Exemplo: `a < b` verifica se `a` é menor que `b`.

5. **Maior ou igual a (>=):** Verifica se o valor à esquerda é maior ou igual ao valor à direita. Exemplo: `a >= b` verifica se `a` é maior ou igual a `b`.

6. **Menor ou igual a (<=):** Verifica se o valor à esquerda é menor ou igual ao valor à direita. Exemplo: `a <= b` verifica se `a` é menor ou igual a `b`.

Esses operadores são frequentemente usados em instruções condicionais para tomar decisões com base em comparações. Por exemplo, você pode usar uma instrução "if" para executar um bloco de código apenas se uma condição específica for verdadeira.

## **Operadores Lógicos:**
Operadores lógicos são usados para combinar expressões lógicas e avaliar se uma condição composta é verdadeira ou falsa. Os operadores lógicos mais comuns são:

1. **E Lógico (and):** Retorna verdadeiro se ambas as expressões forem verdadeiras. Exemplo: `(a > 5) and (b < 10)` é verdadeiro se `a` for maior que 5 e `b` for menor que 10.

2. **OU Lógico (or):** Retorna verdadeiro se pelo menos uma das expressões for verdadeira. Exemplo: `(x < 0) or (y > 20)` é verdadeiro se `x` for menor que 0 ou `y` for maior que 20.

3. **NÃO Lógico (not):** Inverte o valor de uma expressão. Exemplo: `not(a == b)` é verdadeiro se `a` não for igual a `b`.

Os operadores lógicos são frequentemente usados para criar condições mais complexas em instruções condicionais. Por exemplo, você pode usar "E lógico" para verificar duas ou mais condições simultaneamente.

## **Exemplo de Uso:**
Aqui está um exemplo de uso de operadores relacionais e lógicos em um algoritmo simples:

```python
# Solicitando informações ao usuário
idade = float(input("Informe a idade: "))
renda = float(input("Informe a renda mensal: "))

# Verificando a elegibilidade para um empréstimo
if idade >= 18 and renda > 1000:
    print("Você é elegível para um empréstimo.")
else:
    print("Você não é elegível para um empréstimo.")
```

Neste exemplo, o programa pede ao usuário sua idade e renda mensal, depois usa operadores relacionais e lógicos para determinar se o usuário é elegível para um empréstimo. Se a idade for maior ou igual a 18 e a renda for maior que 1000, o programa exibirá a mensagem apropriada. Caso contrário, exibirá uma mensagem diferente.

Operadores relacionais e lógicos são ferramentas poderosas para criar lógica de programação e controlar o fluxo do seu programa com base em condições específicas. Eles são amplamente utilizados na criação de algoritmos e programas em todas as linguagens de programação.