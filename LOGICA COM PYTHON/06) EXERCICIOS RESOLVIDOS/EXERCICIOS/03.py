# Programa para converter temperatura de Fahrenheit para Celsius
def conversao_fahrenheit_para_celsius():
    temperatura_fahrenheit = float(input("Informe a temperatura em graus Fahrenheit: "))
    
    temperatura_celsius = (temperatura_fahrenheit - 32) * 5/9
    
    print(f"A temperatura em graus Celsius é de {temperatura_celsius:.2f}°C.")

conversao_fahrenheit_para_celsius()
