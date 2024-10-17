# ESTRUTURA DE REPETIÇÃO - PARTE 3
## Exercício 01: Contagem Crescente
```python
import time

for c in range(12):
    print("🔔Contagem", c)
    time.sleep(1)
```

**Explicação:**
- Importamos o módulo `time` para usar a função `sleep`.
- Usamos um loop `for` que percorre os números de 0 a 11 (inclusive).
- A cada iteração do loop, imprimimos a mensagem "🔔Contagem" seguida do valor atual de `c`.
- Usamos `time.sleep(1)` para pausar a execução por 1 segundo entre cada iteração.

## Exercício 02: Contagem Decrescente
```python
import time

for c in range(10, 0, -1):
    print("🔔Contagem", c)
    time.sleep(1)
```

**Explicação:**
- Importamos o módulo `time` para usar a função `sleep`.
- Usamos um loop `for` que percorre os números de 10 até 1 (exclusive), com passo -1 para fazer a contagem decrescente.
- A cada iteração do loop, imprimimos a mensagem "🔔Contagem" seguida do valor atual de `c`.
- Usamos `time.sleep(1)` para pausar a execução por 1 segundo entre cada iteração.

## Exercício 03: Soma PID
```python
num = [[], []]
cont = s = p = i = d = 0

for c in range(1, 6):
    valor = int(input(f"😎Digite o {c}ª número: "))
    cont += 1
    s += valor
    if valor >= 0 and valor >= 10:
        d += cont
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

print(f"⭐A soma entre os {cont} valores é {s}")
print(f"⭐Os pares são {num[0]}")
print(f"⭐Os ímpares são: {num[1]}")
print(f"⭐Primeira dezena é {d}")
```

**Explicação:**
- Criamos uma lista `num` com duas sublistas para armazenar os números pares e ímpares.
- Inicializamos as variáveis `cont`, `s`, `p`, `i` e `d` com zero.
- Usamos um loop `for` para pedir ao usuário que insira 5 números.
- Em cada iteração, adicionamos o número à lista apropriada (`num[0]` para números pares e `num[1]` para números ímpares), somamos o número à soma total `s`, e verificamos se o número é maior ou igual a 10 para calcular a primeira dezena.
- No final do loop, exibimos a soma total, os números pares e ímpares, e a posição da primeira dezena.