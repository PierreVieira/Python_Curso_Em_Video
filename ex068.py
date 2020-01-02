"""
Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""
from random import randint
print('-='*12)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*12)
qtde_vitorias = 0
while True:
    valor = int(input('Diga um valor: '))
    valor_pc = randint(0, 10)
    total = valor + valor_pc
    while True:
        par_impar = input('Par ou ímpar [P/I]? ').upper()
        if par_impar == 'P' or par_impar == 'I':
            break
    print('--'*10)
    print(f'Você jogou {valor}\nComputador jogou {valor_pc}')
    print(f'Total deu {total}')
    print('--' * 10)
    if total % 2 == 0 and par_impar == 'P':
        qtde_vitorias += 1
    elif total % 2 == 1 and par_impar == 'I':
        qtde_vitorias += 1
    else:
        break
print('VOCÊ PERDEU!')
print('-='*12)
if qtde_vitorias == 1:
    print('Você ganhou 1 vez')
else:
    print(f'Você ganhou {qtde_vitorias} vezes')

