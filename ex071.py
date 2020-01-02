"""
Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário
qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
"""


def total_de(qtde, nota):
    if qtde == 1:
        print(f'Total de 1 cédula de R$ {nota}')
    else:
        print(f'Total de {qtde} cédulas de R$ {nota}')


qtde_tracos = 40
print("="*qtde_tracos)
print('BANCO CEV'.center(qtde_tracos))
print("="*qtde_tracos)
valor = int(input('Qual valor você quer sacar? R$ '))
for nota in (50, 20, 10, 1):
    if valor >= nota:
        total_de(valor//nota, nota)
        valor %= nota
print("="*qtde_tracos)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
