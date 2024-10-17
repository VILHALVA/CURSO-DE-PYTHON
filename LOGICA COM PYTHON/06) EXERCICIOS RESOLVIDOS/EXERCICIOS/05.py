# Programa para calcular o pagamento de um empréstimo com juros de 20%
def pagamento_emprestimo():
    valor_emprestimo = float(input("Informe o valor do empréstimo: "))
    
    juros = valor_emprestimo * 0.20
    valor_total = valor_emprestimo + juros
    
    print(f"Cleuza deve pagar um total de R${valor_total:.2f} considerando 20% de juros.")

pagamento_emprestimo()
