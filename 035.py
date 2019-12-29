"""
Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não
formar um triângulo.
"""
print('-='*15)
print('ANALISADOR DE TRIÂNGULOS'.center(30))
print('-='*15)
a, b, c = map(float, input('Informe os três segmentos: ').split())
if a > b + c or b > a + c or c > a + b:
    print('Os três segmentos não formam um triângulo')
else:
    print('Os três segmentos formarm um triângulo')
