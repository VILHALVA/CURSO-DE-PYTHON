# Configurando Visibilidade
Em Python, a visibilidade de atributos e métodos é controlada principalmente por meio de convenções de nomeação, uma vez que a linguagem não possui modificadores de acesso estritos como algumas outras linguagens de programação. Neste guia, exploraremos como configurar a visibilidade de atributos e métodos em Python.

## Visibilidade Pública
Em Python, todos os atributos e métodos são públicos por padrão, o que significa que podem ser acessados diretamente de qualquer lugar do código. Não há restrições rígidas de acesso. Aqui está um exemplo de um atributo e método públicos:

```python
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def saudacao(self):
        return f"Olá, meu nome é {self.nome}."
```

Você pode acessar o atributo `nome` e o método `saudacao` diretamente, mesmo fora da classe.

## Visibilidade Privada (Convenção de Nomeação)
Embora Python não tenha atributos privados estritos, a convenção é usar um sublinhado simples (`_`) como prefixo para indicar que um atributo ou método deve ser tratado como protegido ou privado. Isso é uma dica para outros programadores de que eles devem tratá-lo com cuidado.

Exemplo de atributo privado com convenção de nomeação:

```python
class Pessoa:
    def __init__(self, nome):
        self._nome = nome  # Atributo protegido
```

Apesar de ser uma convenção, o atributo `_nome` ainda pode ser acessado diretamente. A visibilidade privada é uma convenção e não uma restrição.

## Encapsulamento
O encapsulamento em Python é baseado na responsabilidade do programador em seguir as convenções de nomeação e não impõe restrições rígidas de acesso. O Python segue o princípio da "Programação orientada a objetos é um jeito de juntar variáveis e funções que operam em objetos e de esconder os detalhes."

Lembre-se de que, embora Python não force a visibilidade privada, seguir as convenções de nomeação é considerado uma boa prática para manter o código organizado e legível.

## Conclusão
Em Python, a visibilidade de atributos e métodos é principalmente controlada por meio de convenções de nomeação. Enquanto a linguagem não impõe restrições rígidas de acesso, seguir as convenções é importante para manter o código organizado e compreensível.
