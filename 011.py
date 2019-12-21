"""
Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
"""
largura_parede = float(input('Largura da parede em metros: '))
altura_parede = float(input('Altura da parede em metros: '))
area_parede = largura_parede*altura_parede
qtde_tinta = area_parede/2
print(f'Sua parede tem a dimensão de {largura_parede}x{altura_parede} e sua área é de {area_parede}m².')
print(f'Para pintar essa parede, você precisará de {qtde_tinta:.2f} litros de tinta.')
