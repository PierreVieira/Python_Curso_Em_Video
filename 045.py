"""
Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.
"""

from random import randint
from time import sleep


def jogador_vence(opcao_jogador, opcao_pc):
    """
    :param opcao_jogador: opção escolhida pelo jogador
    :param opcao_pc: opção sorteada para o computador
    :return: Retorna True se o jogador tiver vencido e false se não tiver vencido
    """
    if opcao_jogador == 0 and opcao_pc == 2: #Jogador jogou pedra e computador jogou tesoura
        return True
    elif opcao_jogador == 1 and opcao_pc == 0: #Jogador jogou papel e computador jogou pedra
        return True
    elif opcao_jogador == 2 and opcao_pc == 1: #Jogador jogou tesoura e computador jogou papel
        return True
    return False #Jogador não venceu


print('Suas opções: ')
print('[0] PEDRA\n[1] PAPEL\n[2] TESOURA')
lista_possibilidades = ['pedra', 'papel', 'tesoura']
opcao_pc = randint(0, 2)
opcao_jogador = int(input('Qual é a sua jogada? '))
if not(0 <= opcao_jogador <= 2):
    print('Opão inválida!')
else:
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO!!!')
    sleep(0.5)
    print('-='*13)
    print(f'Computador jogou {lista_possibilidades[opcao_pc]}')
    print(f'Jogador jogou {lista_possibilidades[opcao_jogador]}')
    print('-='*13)
    if opcao_pc == opcao_jogador:
        resultado = 'VELHA'
    elif jogador_vence(opcao_jogador, opcao_pc):
        resultado = 'JOGADOR VENCE'
    else:
        resultado = 'COMPUTADOR VENCE'
    print(resultado)
