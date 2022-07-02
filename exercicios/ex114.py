import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError():
    print(f'O site Pudim não está acessível no momento.')
else:
    print(f"O site Pudim está acessível no momento.")
    #print(site.read()) Copiar código do site(HTML)