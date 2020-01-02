"""
Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
"""


def preenche_matriz():
    for c in range(3):
        line = []
        for d in range(3):
            line.append(int(input(f'Informe um valor para [{c}, {d}]: ')))
        matriz3x3.append(line)
    print('-=' * 20)
    for c in matriz3x3:
        for d in c:
            print(f'[{d:^3}]', end='')
        print()


matriz3x3 = []
preenche_matriz()
