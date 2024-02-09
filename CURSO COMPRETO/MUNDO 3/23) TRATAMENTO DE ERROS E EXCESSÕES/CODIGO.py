#============TRATAMENTO DE ERROS E EXCEÇÕES:=====================================
#-------TRATAMENDO DE ERROS:-------------------------
try: #<Significa "tente fazer!"
    a = int(input("😎Numerador:\n>>>"))
    b = int(input("😎Denominador:\n>>>"))
    r = a / b
except Exception as erro: #<Significa "senão tente esse" 
    print("😬Tivemos um erro!")
    print(f"🔺O erro foi {erro.__cause__}")
else:
    print(f"⭐O resultado é {r:.1f}")
finally: #<É opcional. Se refere a finalização.
    print("😠Tudo certo! Até nunca mais!!!")

#----------TRATAMENTO PERSONALIZADO:------------------------------------------
try: #<Significa "tente fazer!"
    a = int(input("😎Numerador:\n>>>"))
    b = int(input("😎Denominador:\n>>>"))
    r = a / b
except (ValueError, TypeError):
    print("😬Tivemos um erro!")
    print("🔺O erro foi de valor ou tipo de dado!")
except ZeroDivisionError:
    print("🔺Houve erro ao dividir valor por 0!")
except KeyboardInterrupt:
    print("🔺Houve erro! Usuário não digitou valor!")
else:
    print(f"⭐O resultado é {r:.1f}")
finally: #<É opcional. Se refere a finalização.
    print("😠Até nunca mais!")