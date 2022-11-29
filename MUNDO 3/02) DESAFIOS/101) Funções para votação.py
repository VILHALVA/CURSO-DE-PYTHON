#==============FUNÇÕES PARA VOTAÇÃO:==============================

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano

    if idade < 16:
        return f"⭐Com {idade} anos;\n👎NÃO É PERMITIDO VOTAR!"
    elif 16 <= idade < 18 or idade > 65:
        return f"⭐Com {idade} anos;\n👏VOTO OPCIONAL!"
    else:
        return f"⭐Com {idade} anos;\n👍VOTO OBRIGATÓRIO!"
  
nasc = int(input("😎Digite o ano que você nasceu:\n>>>"))      
print("_" *35, " 🎂RESULTADO:\n", voto(nasc), "\n", "_" *35)