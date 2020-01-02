"""
Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
"""
from datetime import datetime
ano_atual = datetime.now().year
ano = int(input('Informe um ano para analisar (0 caso deseje o ano atual): '))
if ano == 0:
    ano = ano_atual
if (ano % 4 == 0 or ano % 400 == 0) and ano % 100 != 0:
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto!')
