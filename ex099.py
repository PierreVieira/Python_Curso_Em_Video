"""
Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores
inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""


def analisar_valores(*args):
    print(f'Analisando os valores passados...')
    if len(args) == 1:
        print(str(args).replace("(", "").replace(")", "").replace(",", ""))
        print(f'Foi informado 1 valor ao todo.')
        print(f'O maior valor informado foi {args[0]}.')
    elif len(args) == 0:
        print(f'Foram informados 0 valores ao todo.')
    else:
        print(str(args).replace("(", "").replace(")", "").replace(",", ""))
        print(f'Foram inforamados {len(args)} valores ao todo.')
        print(f'O mair valor inforamdo foi {max(args)}')


qtde_tracos = 20
analisar_valores(2, 9, 5, 7, 1)
print('-='*qtde_tracos)
analisar_valores(4, 7, 0)
print('-='*qtde_tracos)
analisar_valores(1, 2)
print('-='*qtde_tracos)
analisar_valores(6)
print('-='*qtde_tracos)
analisar_valores()
