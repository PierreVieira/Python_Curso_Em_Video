"""
Exercício Python 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
"""
numero = int(input('Informe um número: '))
print(f'Unidade: {numero%10}')
print(f'Dezena: {(numero%100)//10}')
print(f'Centena: {(numero%1000)//100}')
print(f'Milhar: {(numero%10000)//1000}')
