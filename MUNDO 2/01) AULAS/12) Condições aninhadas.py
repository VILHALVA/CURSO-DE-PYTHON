#=========#CONDIÇÕES ANINHADAS:==============================
nome = str(input("😎Qual é o seu nome?\n>>>")).strip().upper()

if nome == "SAMUEL":
    comentário = "🌚Que nome TOP!"
elif nome == "DANIEL" or nome == "MARIA" or nome == "PAULO":
    comentário = "😡Que nome tosco!!!"
elif nome in "ANA, CAROL, JÉSSICA, VAL, ROBERTA":
    comentário = "🌝Belo nome feminino!"
else:
    comentário = "😤Que nome horrível você tem!!!"

print("😎Seja bem vindo,{}!\n{}".format(nome, comentário))