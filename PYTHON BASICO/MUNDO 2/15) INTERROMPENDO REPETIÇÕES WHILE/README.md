# INTERROMPENDO REPETIÇÕES WHILE
Em Python, você pode interromper repetições do loop `while` usando a declaração `break`. O `break` é usado para sair imediatamente do loop, independentemente da condição do `while`. Aqui estão algumas situações comuns em que você pode usar `break` para interromper um loop `while`:

1. **Com base em uma Condição Específica:**

   ```python
   contador = 1

   while contador <= 10:
       if contador == 5:
           break
       print(contador)
       contador += 1
   ```

   Neste exemplo, o loop `while` será interrompido quando `contador` for igual a 5.

2. **Com base em uma Entrada do Usuário:**

   ```python
   while True:
       resposta = input("Você deseja sair? (s/n): ")
       if resposta.lower() == 's':
           break
   ```

   Neste exemplo, o loop `while` continua até que o usuário digite 's' para sair.

3. **Com Base em uma Condição Externa:**

   ```python
   executar_loop = True

   while executar_loop:
       resposta = input("Você deseja continuar? (s/n): ")
       if resposta.lower() != 's':
           executar_loop = False
   ```

   Neste exemplo, o loop `while` é controlado por uma variável `executar_loop`. O loop continuará até que `executar_loop` seja definido como `False`.

É importante usar `break` com cuidado, pois ele pode levar à saída abrupta de um loop, e você deve garantir que o loop tenha uma condição de parada adequada. Além disso, considere fornecer mensagens claras ou instruções ao usuário quando estiver usando `break` para que o comportamento do programa seja compreensível.

O `break` é uma ferramenta útil para interromper loops `while` quando uma condição específica for atendida, mas deve ser usado com responsabilidade para evitar loops infinitos e comportamentos inesperados.