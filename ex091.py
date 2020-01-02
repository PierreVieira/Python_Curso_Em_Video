"""
Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses
resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior
número no dado.
"""
from random import randint
from operator import itemgetter
dicionario = {
    "jogador 1": randint(1, 6),
    "jogador 2": randint(1, 6),
    "jogador 3": randint(1, 6),
    "jogador 4": randint(1, 6)
}
for key, value in dicionario.items():
    print(f'{key} tirou {value} no dado.')
qtde_center = 40
print('-='*20)
print('= RANKING DOS JOGADORES ='.center(qtde_center))
c = 1
ordered_dict = dict(sorted(dicionario.items(), key=itemgetter(1), reverse=True))
for key, value in ordered_dict.items():
    print(f'{c}º lugar: {key} com {value}'.center(qtde_center))
    c += 1
