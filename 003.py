#Exercício Python 003: Crie um programa que leia dois números e mostre a soma entre eles.
a, b = map(float, input('Informe dois números: ').split())
print(f'{a} + {b} = {a+b:.2f}')
