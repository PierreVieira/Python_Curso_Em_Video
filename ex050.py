"""
Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem
pares. Se o valor digitado for ímpar, desconsidere-o.
"""
soma_par = 0
for c in range(6):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        soma_par += numero
print(f'A soma dos números pares é: {soma_par}')
