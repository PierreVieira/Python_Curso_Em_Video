"""
Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
"""
import urllib
from urllib.request import urlopen
try:
    url = urlopen('http://www.pronhub.com')
except urllib.error.URLError:
    print('Deu erro!')
else:
    print('Tudo ok!')
    print(url.read())