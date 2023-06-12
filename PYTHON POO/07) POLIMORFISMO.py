# Vou apresentar um exemplo de projeto que utiliza polimorfismo de sobrecarga e sobrescrita em Python. Neste caso, vamos criar uma classe chamada `Calculadora` que possui diferentes métodos para executar operações matemáticas.

# Polimorfismo de sobrecarga ocorre quando múltiplos métodos com o mesmo nome são definidos na mesma classe, mas com diferentes parâmetros. Já o polimorfismo de sobrescrita ocorre quando uma classe filha redefine um método da classe pai com a mesma assinatura.

class Calculadora:
    def soma(self, a, b):
        return a + b

    def soma(self, a, b, c):
        return a + b + c

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        return a / b

# Criando objeto da calculadora
calculadora = Calculadora()

# Sobrecarga de método
resultado1 = calculadora.soma(2, 3)
resultado2 = calculadora.soma(2, 3, 4)

print(resultado1)  # Saída: 5
print(resultado2)  # Saída: 9

# Sobrescrita de método
resultado3 = calculadora.subtracao(5, 3)
print(resultado3)  # Saída: 2

# Neste exemplo, a classe `Calculadora` possui vários métodos para executar operações matemáticas. Observe que há uma sobrecarga do método `soma`, onde ele é definido duas vezes com diferentes números de parâmetros.

# Ao criar um objeto `calculadora` e chamar o método `soma`, o comportamento do método é determinado pelo número de parâmetros fornecidos. Se forem fornecidos dois parâmetros, a soma dos dois números é retornada. Se forem fornecidos três parâmetros, a soma dos três números é retornada.

# Além disso, o método `subtracao` é sobrescrito na classe `Calculadora`. A implementação do método na classe filha substitui a implementação do método na classe pai. Portanto, ao chamar o método `subtracao`, a implementação na classe filha é executada, retornando a subtração dos dois números fornecidos.

# Dessa forma, o polimorfismo de sobrecarga é utilizado para ter métodos com o mesmo nome, mas com diferentes parâmetros, e o polimorfismo de sobrescrita é utilizado para redefinir um método na classe filha com a mesma assinatura da classe pai.