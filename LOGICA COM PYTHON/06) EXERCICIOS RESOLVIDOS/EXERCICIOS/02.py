# Programa para converter Reais em Dólares
def conversao_reais_para_dolares():
    valor_reais = float(input("Informe o valor em reais: "))
    taxa_cambio = float(input("Informe a taxa de câmbio (valor de 1 real em dólares): "))
    
    valor_dolares = valor_reais / taxa_cambio
    
    print(f"Cleuza terá aproximadamente ${valor_dolares:.2f} em dólares.")

conversao_reais_para_dolares()
