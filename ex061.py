"""
Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os
10 primeiros termos dessa progressão.
"""
print('='*33)
print('10 TERMOS DE UMA PA'.center(30))
print('='*33)
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
c = 0
while c < 10:
    print(primeiro_termo, end=' -> ')
    primeiro_termo += razao
    c += 1
print('ACABOU')