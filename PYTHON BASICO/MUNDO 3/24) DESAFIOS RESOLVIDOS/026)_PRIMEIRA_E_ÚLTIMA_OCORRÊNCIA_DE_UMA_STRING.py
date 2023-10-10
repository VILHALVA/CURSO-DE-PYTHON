#=======PRIMEIRA E ÚLTIMA OCORRÊNCIA DE UMA STRING:=================
frase = str(input("😎Digite uma frase:\n>>>")).strip().upper()
print("⭐A letra A aparece {} vezes na frase!".format(frase.count("A")))
print("⭐A primeira letra A aparece na posição {}!".format(frase.find("A")+1))
print("⭐A última letra A apareceu na posição {}!".format(frase.rfind("A")+1))
