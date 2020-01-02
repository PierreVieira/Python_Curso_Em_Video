"""
Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar
quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""
from random import sample
from time import sleep
qtde_tracos = 42
print('-'*qtde_tracos)
print('JOGA NA MEGA SENA'.center(qtde_tracos))
print('-'*qtde_tracos)
while True:
    try:
        qtde_jogos = int(input('Quantos jogos você quer que eu sorteie? '))
    except ValueError:
        print('Digite apenas um número inteiro informando a quantidade de jogos!')
    else:
        jogos = []
        print('-='*6, end=f' SORTEANDO {qtde_jogos} JOGOS ')
        print('-='*6)
        sleep(0.5)
        for c in range(qtde_jogos):
            jogo = sample(range(1, 61), 6)
            print(f'Jogo {c+1}: {sorted(jogo)}')
            sleep(0.5)
            jogos.append(sorted(jogo.copy()))
        print('-=' * 6, end=f' < BOA SORTE! > ')
        print('-=' * 6)
        print()
        break
