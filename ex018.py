"""
Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente
desse ângulo.
"""
from math import sin, cos, tan, radians
angulo = float(input('Digite o ângulo que você deseja em graus: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'O ângulo de {angulo}° tem o seno de {seno:.2f}')
print(f'O ângulo de {angulo}° tem o cosseno de {cosseno:.2f}')
print(f'O ângulo de {angulo}° tem a tangente de {tangente:.2f}')
