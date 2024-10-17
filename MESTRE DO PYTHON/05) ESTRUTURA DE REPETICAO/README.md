# ESTRUTURA DE REPETIÇÃO
A estrutura de repetição em Python permite executar um bloco de código várias vezes. Existem duas formas principais de estrutura de repetição em Python: o loop "for" e o loop "while".

## Exemplo de Loop "for":
```python
# Loop for para imprimir os números de 1 a 5
for i in range(1, 6):
    print(i)
```
Neste exemplo, o loop "for" imprime os números de 1 a 5.

## Exemplo de Loop "while":
```python
# Loop while para imprimir os números de 1 a 5
i = 1
while i <= 5:
    print(i)
    i += 1
```
Neste exemplo, o loop "while" imprime os números de 1 a 5 enquanto a condição `i <= 5` for verdadeira.

## Exemplo de Loop com Listas:
```python
# Loop for para iterar sobre os elementos de uma lista
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta)
```
Neste exemplo, o loop "for" itera sobre os elementos da lista `frutas` e imprime cada fruta.

## Exemplo de Loop com Dicionários:
```python
# Loop for para iterar sobre os itens de um dicionário
notas = {"João": 8, "Maria": 7, "Carlos": 9}
for nome, nota in notas.items():
    print(f"{nome}: {nota}")
```
Neste exemplo, o loop "for" itera sobre os itens do dicionário `notas` e imprime cada nome e nota.

## Exemplo de Loop com "break" e "continue":
```python
# Loop while com break e continue
i = 0
while i < 10:
    i += 1
    if i == 3:
        continue  # Pula a iteração quando i é igual a 3
    if i == 8:
        break  # Sai do loop quando i é igual a 8
    print(i)
```
Neste exemplo, o loop "while" é interrompido quando `i` é igual a 8 devido ao uso do `break`, e a iteração é pulada quando `i` é igual a 3 devido ao uso do `continue`.

A estrutura de repetição é uma ferramenta poderosa para executar operações repetitivas em Python, facilitando a automação de tarefas e a manipulação de dados.