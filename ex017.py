"""
Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
retângulo. Calcule e mostre o comprimento da hipotenusa.
"""
oposto = float(input('Informe o cateto oposto: '))
adjacente = float(input('Informe o cateto adjacente: '))
hipotenusa = (oposto**2 + adjacente**2)**0.5
print(f'A hipotenusa mede: {hipotenusa:.2f}')
