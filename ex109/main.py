"""
Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
"""
from ex109 import moedas
valor = float(input('Digite o preço: R$ '))
print(f'A metade de R$ {moedas.moeda(valor)} é R$ {moedas.metade(valor, format=True)}')
print(f'O dobro de R$ {moedas.moeda(valor)} é R$ {moedas.dobro(valor)}')
print(f'Aumentando 10%, temos R$ {moedas.aumento_10_pc(valor)}')
