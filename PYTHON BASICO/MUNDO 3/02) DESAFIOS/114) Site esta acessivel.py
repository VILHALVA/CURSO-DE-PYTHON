#==========SITE ESTÁ ACESSÍVEL?:==========================================
import urllib
import urllib.request

try:
    site = urllib.request.urlopen("http://www.pudim.com.br")
except urllib.error.URLError:
    print("⛔ERRO!!! O site não está acessível!!!")
else:
    print("👍CERTO!!! Site acessado com sucesso!!!")
    print(site.read())