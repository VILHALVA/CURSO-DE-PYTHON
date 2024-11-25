def saudacao(dia):
    match dia:
        case 1 | 7:
            return "FIM DE SEMANA. DOMINGO OU SÁBADO"
        case 2:
            return "SEGUNDA-FEIRA"
        case 3:
            return "TERÇA-FEIRA"
        case 4:
            return "QUARTA-FEIRA"
        case 5:
            return "QUINTA-FEIRA"
        case 6:
            return "SEXTA-FEIRA"
        case _:
            return "DIA INVÁLIDO!"

# Exemplo de uso
dia = 1
print(saudacao(dia))  # Saída: FIM DE SEMANA. DOMINGO OU SÁBADO
