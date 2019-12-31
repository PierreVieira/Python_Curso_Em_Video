"""
Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""


def exibe_menu():
    print('[1] SOMAR')
    print('[2] MULTIPLICAR')
    print('[3] MAIOR')
    print('[4] NOVOS NÚMEROS')
    print('[5] SAIR DO PROGRAMA')


while True:
    a, b = map(float, input('Informe dois valores: ').split())
    while True:
        exibe_menu()
        print('--' * 4)
        opcao = int(input('Opção: '))
        print('--' * 4)
        if 1 <= opcao <= 5:
            break
    if opcao == 1:
        print(f'{a} + {b} =  {a + b}')
    elif opcao == 2:
        print(f'{a} * {b} = {a * b}')
    elif opcao == 3:
        print(f'O maior número entre {a} e {b} é {max([a, b])}')
    elif opcao == 5:
        print('Volte sempre :)')
        break
