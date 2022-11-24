#========VERIFICANDO AS PRIMEIRAS LETRAS DO TEXTO:=========================
cidade = str(input("😎Em que cidade você nasceu?\n>>>")).strip() #>Elimina os espaços que o usuário digitou.
print(cidade[:5].upper() == "SANTO") #>Funciona tanto em maiúsculo quanto minosculo.