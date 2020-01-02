"""
Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""
from ex086 import *
pares = [numero for line in matriz3x3 for numero in line if numero % 2 == 0]
terceira_coluna = [matriz3x3[0][2], matriz3x3[1][2], matriz3x3[2][2]]
segunda_linha = matriz3x3[1]
print('-='*20)
print(f'Os valores pares foram {pares}')
print(f'Soma de todos os valores pares digitados: {sum(pares)}')
print('--'*20)
print(f'Os valores da terceira coluna foram {terceira_coluna}')
print(f'Soma de todos os valores da terceira coluna: {sum(terceira_coluna)}')
print('--'*20)
print(f'Segunda linha: {segunda_linha}')
print(f'O maior valor da segunda linha: {max(segunda_linha)}')
print('--'*20)
