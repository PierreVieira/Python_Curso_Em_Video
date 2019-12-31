"""
Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os
espaços.
"""
frase = input('Digite uma frase: ').upper()
invertido = frase[::-1]
print(f'O inverso de {frase} é {invertido}')
if frase == invertido:
    print('A frase digitada é um palíndromo')
else:
    print('A frase digitada não é um palíndromo')
