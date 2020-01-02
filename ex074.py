"""
Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""

from random import sample
tupla_aleatoria = tuple(sample(range(11), 5))
print(f'Os valores sorteados foram: {str(tupla_aleatoria)[1:len(str(tupla_aleatoria))-1:]}')
print(f'Maior: {max(tupla_aleatoria)}\nMenor: {min(tupla_aleatoria)}')