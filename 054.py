"""
Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
ainda não atingiram a maioridade e quantas já são maiores.
"""
maiores = 0
for c in range(7):
    idade = int(input('Informe a idade: '))
    if idade >= 18:
        maiores += 1
print(f'Maiores de 18 anos: {maiores}\nMenores de 18 anos: {7 - maiores}')
