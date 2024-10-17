while True:
    try:
        idade = int(input("Digite sua idade: "))
        if idade < 0:
            raise ValueError("A idade deve ser um número inteiro positivo!")
        print("Idade inserida com sucesso!")
        break
    except ValueError as ve:
        print(f"Erro: {ve}")
