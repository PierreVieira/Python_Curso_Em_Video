"""
Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de
nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO
nas eleições.
"""


from datetime import datetime


def condicao(idade):
    if idade < 16:
        return 'NÃO VOTA'
    elif idade < 18:
        return 'VOTO OPCIONAL'
    elif idade < 65:
        return 'VOTO OBRIGATÓRIO'
    return 'VOTO OPCIONAL'


print('--'*20)
ano_atual = datetime.now().year
ano_nascimento = int(input('Em que ano você nasceu? '))
idade = ano_atual - ano_nascimento
print(f'Com {idade} anos: {condicao(idade)}')