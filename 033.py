"""
Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""
numeros = list(map(int, input('Informe três números: ').split()))
print(f'Maior: {max(numeros)}\nMenor: {min(numeros)}')
