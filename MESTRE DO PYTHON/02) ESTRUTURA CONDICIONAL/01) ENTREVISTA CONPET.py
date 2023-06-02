nome = input("😎Qual é o seu nome?\n>>>").strip().upper()
if "SAMUEL" in nome or "DANIEL" in nome or "LUCAS" in nome or "MARIA" in nome or "ANA" in nome:
    print("😍Que nome lindo você tem!")
else: 
    print("😒Seu nome é tão comum!")

escola = input("😎Você tem o ensino médio completo?\n>>>").strip().upper()
if "SIM" in escola or "TENHO" in escola or "FIZ" in escola or "FACULDADE" in escola or "UNIVERSIDADE" in escola:
    print("👏PARABÉNS!!!")
elif "NÃO" in escola or "FUNDAMENTAL" in escola:
    print("😔Assim fica complicado️!") 
else:
    print("👏️Continue,que você consegue!!!️")