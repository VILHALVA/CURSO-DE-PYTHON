# CORES NO TERMINAL
Você pode adicionar cores ao texto que é impresso no terminal em Python usando sequências de escape ANSI. As sequências de escape ANSI são sequências especiais de caracteres que o terminal interpreta para modificar a cor e o estilo do texto. Aqui estão algumas maneiras de adicionar cores ao texto no terminal em Python:

1. **Usando Sequências de Escape ANSI Diretamente:**

   Você pode usar sequências de escape ANSI diretamente em suas strings para definir a cor do texto. Por exemplo, a sequência `'\033[91m'` define a cor vermelha, e a sequência `'\033[0m'` redefine a cor para o padrão. Veja um exemplo:

   ```python
   print('\033[91mTexto vermelho\033[0m')
   ```

   Isso imprimirá o texto "Texto vermelho" em vermelho.

2. **Usando Funções para Definir Cores:**

   Você também pode criar funções personalizadas para facilitar a definição de cores. Aqui está um exemplo de uma função que define a cor vermelha:

   ```python
   def texto_vermelho(texto):
       return f'\033[91m{texto}\033[0m'

   print(texto_vermelho("Texto vermelho"))
   ```

3. **Usando Bibliotecas:**

   Existem bibliotecas Python disponíveis, como `termcolor` e `colorama`, que tornam mais fácil adicionar cores ao texto no terminal de forma mais legível e portátil. Você pode instalá-las usando o `pip`:

   ```bash
   pip install termcolor
   ```

   Exemplo usando a biblioteca `termcolor`:

   ```python
   from termcolor import colored

   print(colored("Texto verde", "green"))
   ```

   Este código imprimirá o texto "Texto verde" em verde.

4. **Estilos de Texto:**

   Além de definir cores, você também pode modificar o estilo do texto, como negrito ou sublinhado, usando as sequências de escape ANSI apropriadas. Por exemplo:

   - Negrito: `'\033[1mTexto em negrito\033[0m'`
   - Sublinhado: `'\033[4mTexto sublinhado\033[0m'`

   Lembre-se de sempre incluir a sequência `'\033[0m'` após o texto formatado para redefinir o estilo para o padrão.

É importante observar que a capacidade de exibir cores no terminal depende do terminal em que você está executando seu código. Nem todos os terminais suportam sequências de escape ANSI, portanto, verifique a compatibilidade com o terminal que você está usando.

As sequências de escape ANSI são uma maneira simples e eficaz de adicionar cores e estilo ao texto no terminal, mas elas podem não ser suportadas em todos os ambientes. Portanto, ao escrever código Python que usa cores no terminal, é importante considerar a compatibilidade com diferentes terminais.

## TABELAS DE CORES:

| Cor                  | Código ANSI    | Exemplo de Uso                  |
|----------------------|----------------|---------------------------------|
| Vermelho             | \033[91m       | `\033[91mTexto Vermelho\033[0m`   |
| Verde                | \033[92m       | `\033[92mTexto Verde\033[0m`      |
| Amarelo              | \033[93m       | `\033[93mTexto Amarelo\033[0m`    |
| Azul                 | \033[94m       | `\033[94mTexto Azul\033[0m`       |
| Magenta (Roxo)       | \033[95m       | `\033[95mTexto Magenta\033[0m`   |
| Ciano                | \033[96m       | `\033[96mTexto Ciano\033[0m`      |
| Branco               | \033[97m       | `\033[97mTexto Branco\033[0m`     |
| Negrito Vermelho     | \033[91m\033[1m | `\033[91m\033[1mTexto Negrito Vermelho\033[0m` |
| Sublinhado Verde     | \033[92m\033[4m | `\033[92m\033[4mTexto Sublinhado Verde\033[0m` |

