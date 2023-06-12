# Ao falar sobre visibilidade em programação orientada a objetos (POO), estamos nos referindo à forma como os atributos e métodos de uma classe podem ser acessados por outras partes do código. Em Python, existem três níveis de visibilidade: público, protegido e privado. Esses níveis são controlados por convenções, pois a linguagem não impõe restrições estritas de acesso.

# 1. Público: Os atributos e métodos públicos são acessíveis de qualquer lugar do código, tanto dentro da classe como fora dela. Por convenção, os atributos e métodos públicos não possuem nenhuma indicação especial em Python. Eles podem ser acessados diretamente usando a notação de ponto.

class Exemplo:
    def __init__(self):
        self.atributo_publico = 10

    def metodo_publico(self):
        print("Método público")

exemplo = Exemplo()
print(exemplo.atributo_publico)  # Saída: 10
exemplo.metodo_publico()  # Saída: Método público

# 2. Protegido: Os atributos e métodos protegidos são indicados adicionando um único sublinhado (_) como prefixo. Isso sinaliza que esses elementos não devem ser acessados diretamente fora da classe, embora ainda seja possível fazê-lo. A convenção é que os elementos protegidos sejam acessados apenas dentro da classe ou em subclasses derivadas.

class Exemplo:
    def __init__(self):
        self._atributo_protegido = 20

    def _metodo_protegido(self):
        print("Método protegido")

exemplo = Exemplo()
print(exemplo._atributo_protegido)  # Saída: 20
exemplo._metodo_protegido()  # Saída: Método protegido

# 3. Privado: Os atributos e métodos privados são indicados adicionando dois sublinhados (_) como prefixo. Isso indica que esses elementos não devem ser acessados ou sobrescritos diretamente fora da classe. No entanto, em Python, os elementos privados podem ser acessados de forma não convencional, mas é recomendado não fazer isso. A convenção é que os elementos privados sejam tratados como implementações internas da classe.

class Exemplo:
    def __init__(self):
        self.__atributo_privado = 30

    def __metodo_privado(self):
        print("Método privado")

exemplo = Exemplo()
# print(exemplo.__atributo_privado)  # Isso gera um erro
# exemplo.__metodo_privado()  # Isso gera um erro

# Lembrando que, em Python, essas convenções de visibilidade são apenas convenções e não regras rígidas. O programador pode acessar elementos protegidos e privados, mas é recomendado seguir as convenções para manter a integridade do código e evitar possíveis problemas de compatibilidade.

# Essas são as noções básicas de visibilidade em Python. É importante notar que esses níveis de visibilidade são apenas convenções e não restrições impostas pela linguagem.