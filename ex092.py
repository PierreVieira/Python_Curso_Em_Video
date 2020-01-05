"""
Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade)
em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o
salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""
from datetime import datetime


def info_sem_carteira_trabalho(pessoa):
    print(f'{pessoa["nome"]} tem {pessoa["idade"]} anos e não possui carteira de trabalho.')


def info_carteira_trabalho(pessoa):
    print(f'{pessoa["nome"]} tem {pessoa["idade"]} anos')
    print(f'Ano de contratação: {pessoa["contratacao"]}')
    print(f'Ctps: {pessoa["ctps"]}')
    print(f'Salário: R$ {pessoa["salario"]:.2f}')
    print(f'Ano de aposentadoria: {pessoa["ano_aposentadoria"]}')


ano_atual = datetime.now().year
nome = input('Nome: ').title()
ano_nascimento = int(input('Ano de nascimento: '))
carteira_trabalho = input('Carteira de trabalho (0 não tem): ')
pessoa = {'nome': nome, 'ano_nascimento': ano_nascimento, 'ctps': carteira_trabalho}
pessoa.update({'idade': ano_atual-ano_nascimento})
if carteira_trabalho == '0':
    info_sem_carteira_trabalho(pessoa)
else:
    pessoa_trabalha = pessoa.copy()
    pessoa_trabalha['contratacao'] = int(input('Ano de Contratação: '))
    pessoa_trabalha['salario'] = float(input('Saláro: R$ '))
    pessoa_trabalha['ano_aposentadoria'] = ano_nascimento + 65
    info_carteira_trabalho(pessoa_trabalha)