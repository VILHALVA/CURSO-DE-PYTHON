# Recebe três números do usuário
a = float(input("Digite o valor do lado A: "))
b = float(input("Digite o valor do lado B: "))
c = float(input("Digite o valor do lado C: "))

# Verifica se os lados formam um triângulo válido
if a < b + c and b < a + c and c < a + b:
    print("Os lados formam um triângulo válido.")
else:
    print("Os lados não formam um triângulo válido.")
