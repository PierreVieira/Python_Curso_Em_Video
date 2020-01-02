"""
Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela
pode comprar.
"""
real = float(input('Quanto de dinheiro você tem na carteira? R$ '))
dolar = real/4.1 #cotação de 21/12/2019
print(F'Com R$ {real:.2f} você pode comprar U$ {dolar:.2f}')
