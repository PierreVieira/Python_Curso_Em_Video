"""
Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. Mostrando na tela uma mensagem:
"""
a, b = map(float, input('Informe dois valores: ').split())
if a > b:
    print('O primeiro valor é maior!')
elif b > a:
    print('O segundo valor é maior!')
else:
    print('Os valores são iguais!')
