# ESTRUTURA DE REPETIÇÃO - PARTE 2
## EXERCICIOS:
### Exercício 01: Loop Personalizado
```python
r = 0
c = 0
s = 0
t = 0

while True:
    n = float(input(f"😎Digite {c+1}ª número: "))
    c += 1
    s += n

    if n < 0:
        t += 1

    r = input("😎Você quer continuar?[S/N]:").upper()

    if r == "N":
        break
    elif r == "S":
        continue
    else:
        print("😠Não compreendi...")

print(f"⭐A soma dos {c} valores é: {s}")
print(f"\n⭐Temos {t} negativos!")
```

### Exercício 02: Contador Até
```python
from time import sleep

k = 0

while k < 11:
    print(f"⭐Contagem: {k}")
    k += 1
    sleep(1)
```

### Exercício 03: Tabuada
```python
while True:
    num = int(input("😎Digite um número: "))

    if num == 999:
        break

    opr = input("😎Digite um sinal aritmético[×÷+-]: ")

    for c in range(1, 11):
        if opr == "×":
            print(f"{num} × {c:2} = {num*c}")
        elif opr == "÷":
            print(f"{num} ÷ {c:2} = {num/c}")
        elif opr == "+":
            print(f"{num} + {c:2} = {num+c}")
        elif opr == "-":
            print(f"{num} - {c:2} = {num-c}")
        else:
            print(f"😬Valor {opr} é inválido!")

print("🔔FIM")
```

### Exercício 04: Fatorial
```python
def fatorial(n: int, mostrar: bool = False) -> int:
    f = 1

    for c in range(n, 0, -1):
        if mostrar:
            print(c, end="")
            if c > 1:
                print(" × ", end="")
            else:
                print(" = ", end="")
        f *= c

    return f

print(fatorial(5, mostrar=True))
```

Estes exercícios demonstram várias aplicações das estruturas de repetição "while" e "for" em Python, incluindo contagem personalizada, cálculos iterativos e cálculo de fatorial.

## EXPLICAÇÕES:
Vou explicar cada um dos exercícios da "Estrutura de Repetição - Parte 2" e traduzi-los para Python:

**Exercício 01: Loop Personalizado**

Neste exercício, você cria um loop "while" personalizado que permite ao usuário inserir números até decidir parar. Ele também conta quantos números negativos foram inseridos e calcula a soma dos números inseridos.

- A variável `r` é usada para armazenar a resposta do usuário se deseja continuar ou não.
- A variável `c` é usada para contar quantos números foram inseridos.
- A variável `s` é usada para somar os números inseridos.
- A variável `t` é usada para contar quantos números negativos foram inseridos.

O loop continua até que o usuário decida parar digitando "N". Se o usuário digitar "S", o loop continuará. Se a resposta não for nem "S" nem "N", o programa informa que não compreendeu.

No final, o programa exibe a soma dos números inseridos e quantos deles eram negativos.

**Exercício 02: Contador Até**

Neste exercício, você usa um loop "while" para criar uma contagem de 0 a 10. A função `sleep(1)` é usada para pausar a execução por 1 segundo a cada iteração, criando assim uma contagem visível.

- A variável `k` é usada como contador.

O loop continua enquanto `k` for menor que 11, e a cada iteração, ele escreve o valor de `k` na tela e depois incrementa `k` em 1. A função `sleep(1)` cria um pequeno atraso entre cada contagem.

**Exercício 03: Tabuada**

Neste exercício, você cria um loop "while" que permite ao usuário digitar um número e um operador (+, -, × ou ÷). Em seguida, ele calcula a tabuada desse número usando o operador escolhido e a exibe.

- A variável `num` armazena o número inserido pelo usuário.
- A variável `opr` armazena o operador inserido pelo usuário.
- A variável `c` é usada como contador no loop "for" que calcula a tabuada.

O loop principal continua até que o usuário digite "999". Dentro do loop, outro loop "for" é usado para calcular a tabuada do número inserido com base no operador escolhido. O resultado é exibido na tela. Se o operador não for válido, o programa informa que o valor é inválido.

**Exercício 04: Fatorial**

Neste exercício, você cria uma função chamada `fatorial` que calcula o fatorial de um número inteiro. A função aceita dois parâmetros: o número `n` para o qual o fatorial será calculado e um parâmetro opcional `mostrar` que determina se o cálculo do fatorial será exibido passo a passo.

- A variável `f` é usada para armazenar o resultado do fatorial.
- A variável `c` é usada como contador no loop "for" que calcula o fatorial.

A função `fatorial` calcula o fatorial de `n` e pode exibir cada etapa do cálculo, incluindo os números sendo multiplicados e o resultado final. No final do código, você chama a função `fatorial` com `5` como argumento e `mostrar = True` para exibir o cálculo passo a passo. O resultado é o fatorial de 5, que é exibido na tela.

Esses exercícios demonstram várias aplicações das estruturas de repetição "while" e "for" em Python, incluindo contagem personalizada, cálculos iterativos e cálculo de fatorial.