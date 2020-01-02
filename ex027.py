"""
Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
e o último nome separadamente.
"""
nome = input('Informe seu nome completo: ').strip().split()
print(f'Seja bem vindo {nome[0]} {nome[-1]}')