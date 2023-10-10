#===========NÚMERO POR EXTENSO:=============================
cont = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez",
	       "onze", "doze", "treze", "quartoze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
	   
while True:    
    num = int(input("😎Digite um número entre 0 e 20:\n>>>"))
    if 0 <= num <= 20:
        break
    print("😬Tente novamente...")
print(f"⭐Você digitou o número {cont[num]}!")