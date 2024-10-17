while True:
    try:
        celsius = float(input("Digite a temperatura em graus Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}")
        break
    except ValueError:
        print("Erro: Insira um valor numérico válido para a temperatura.")
