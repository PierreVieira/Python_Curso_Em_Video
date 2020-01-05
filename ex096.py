"""
Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
retangular (largura e comprimento) e mostre a área do terreno.
"""


def area(largura, comprimento):
    print(f'A área de um terreno de {largura}x{comprimento} é de {largura * comprimento:.2f} m²')


print(' Controle de Terrenos')
print('-'*15)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)
