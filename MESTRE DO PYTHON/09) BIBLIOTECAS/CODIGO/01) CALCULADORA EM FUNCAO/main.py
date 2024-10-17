# main.py
import operations

def main():
    print("Calculadora Simples")
    print("-------------------")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    print("\nEscolha a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    choice = input("Digite sua escolha (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        if choice == '1':
            print("Resultado:", operations.add(num1, num2))
        elif choice == '2':
            print("Resultado:", operations.subtract(num1, num2))
        elif choice == '3':
            print("Resultado:", operations.multiply(num1, num2))
        elif choice == '4':
            try:
                print("Resultado:", operations.divide(num1, num2))
            except ValueError as e:
                print("Erro:", e)
    else:
        print("Opção inválida!")

if __name__ == "__main__":
    main()
