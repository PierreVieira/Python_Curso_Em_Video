"""
Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar
os números como um valor monetário formatado.
"""
from ex108 import moedas
valor = float(input('Digite o preço: R$ '))
print(f'A metade de R$ {moedas.moeda(valor)} é R$ {moedas.moeda(moedas.metade(valor))}')
print(f'O dobro de R$ {moedas.moeda(valor)} é R$ {moedas.moeda(moedas.dobro(valor))}')
print(f'Aumentando 10%, temos R$ {moedas.moeda(moedas.aumento_10_pc(valor))}')
