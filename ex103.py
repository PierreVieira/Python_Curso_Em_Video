"""
Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que
algum dado não tenha sido informado corretamente.
"""


def resposta(nome_jogador = '<desconhecido>', qtde_gols='0'):
    return f'O jogador {nome_jogador} fez {qtde_gols} gols no campeonato.'


nome_jogador = input('Nome do jogador: ').title()
qtde_gols = input('Número de gols: ')
if not nome_jogador.isalpha() and not qtde_gols.isnumeric():
    print(resposta())
elif not nome_jogador.isalpha():
    print(resposta(qtde_gols=qtde_gols))
elif not qtde_gols.isnumeric():
    print(resposta(nome_jogador=nome_jogador))
else:
    print(resposta(nome_jogador, qtde_gols))