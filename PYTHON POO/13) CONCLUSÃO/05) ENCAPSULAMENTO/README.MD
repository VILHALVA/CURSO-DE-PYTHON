# Encapsulamento 
O **encapsulamento** é um dos pilares da Programação Orientada a Objetos (POO) e envolve o conceito de ocultar os detalhes internos de uma classe e expor uma interface pública controlada para interagir com objetos dessa classe. Em Python, o encapsulamento é implementado principalmente por meio de convenções de nomeação e não por restrições rígidas de acesso.

## Visibilidade Pública, Protegida e Privada
Em Python, todos os atributos e métodos de uma classe são públicos por padrão, o que significa que eles podem ser acessados de qualquer lugar do código. No entanto, Python utiliza convenções de nomeação para indicar o nível de visibilidade pretendido:

- **Atributos e métodos públicos:** Não têm prefixos especiais e são acessíveis a partir de qualquer lugar do código.

- **Atributos e métodos protegidos:** Geralmente começam com um sublinhado simples (`_`). Isso indica que eles são considerados protegidos, embora ainda possam ser acessados de fora da classe.

- **Atributos e métodos privados:** Geralmente começam com dois sublinhados (`__`). Isso indica que eles são considerados privados, embora ainda possam ser acessados por meio de técnicas específicas.

Exemplo de atributos com diferentes níveis de visibilidade:

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome               # Atributo público
        self._idade = idade            # Atributo protegido
        self.__endereco = "Desconhecido"  # Atributo privado

    def saudacao(self):
        return f"Olá, meu nome é {self.nome}."

    def _exibir_idade(self):
        return f"Idade: {self._idade}"

    def __exibir_endereco(self):
        return f"Endereço: {self.__endereco}"
```

Embora a visibilidade seja uma convenção em Python, é importante seguir as práticas recomendadas para manter o código organizado e seguro.

## Métodos Acessores
Os **métodos acessores**, como **getters** e **setters**, são usados para controlar o acesso e a modificação de atributos, permitindo uma abordagem mais controlada para acessar atributos protegidos ou privados. Eles geralmente têm a seguinte forma:

- **Getter:** Retorna o valor do atributo.
- **Setter:** Define um novo valor para o atributo.

Exemplo de métodos acessores em Python:

```python
class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome  # Atributo protegido
        self._idade = idade  # Atributo protegido

    def get_nome(self):
        return self._nome

    def set_nome(self, novo_nome):
        self._nome = novo_nome

    def get_idade(self):
        return self._idade

    def set_idade(self, nova_idade):
        if nova_idade >= 0:
            self._idade = nova_idade
```

O uso de métodos acessores permite que você controle o acesso e a modificação de atributos de maneira mais segura.

## Conclusão
O encapsulamento em Python é baseado em convenções de nomeação e métodos acessores para controlar o acesso a atributos e métodos de uma classe. Seguir as melhores práticas de encapsulamento torna o código mais organizado e seguro.
