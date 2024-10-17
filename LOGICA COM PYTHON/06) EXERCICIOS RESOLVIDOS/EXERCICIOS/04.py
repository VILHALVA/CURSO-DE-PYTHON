# Programa para calcular o imposto de 60% sobre a Muamba
def calculo_imposto_muamba():
    valor_produto = float(input("Informe o valor total dos produtos de Muamba: "))
    
    imposto = valor_produto * 0.60
    
    print(f"O valor do imposto a ser pago é de R${imposto:.2f}.")

calculo_imposto_muamba()
