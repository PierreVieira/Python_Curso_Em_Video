"""
Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
"""
cidade = input('Informe uma cidade: ')
if cidade.split()[0].lower() == 'santo':
    print('Cidade começa com Santo')
else:
    print('Cidade não começa com Santo')