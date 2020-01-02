"""
Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma
mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
"""
velocidade_carro = float(input('Informe a velocidade do carro em km/h: '))
if velocidade_carro > 80:
    print('O motorista está multado!')
    print(f'A multa a pagar é de R$ {7*(velocidade_carro - 80):.2f}')
else:
    print('O motorista está dentro do limite!')
