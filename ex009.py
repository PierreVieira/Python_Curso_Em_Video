"""
Exercício Python 009: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
"""
numero = int(input('Digite um número par ver sua tabuada: '))
print('-'*15)
for c in range(10):
    print(f'{numero:2} X {c+1:2} = {numero*(c+1):2}')
print('-'*15)
