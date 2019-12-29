"""
Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta para o alistamento caso esse já não deva se alistar.
"""
from datetime import datetime
ano_atual = datetime.now().year
ano_nascimento = int(input('Informe o ano de nascimento: '))
ano_alistamento = ano_nascimento + 18
print(f'Idade: {ano_atual - ano_nascimento} anos')
if ano_atual == ano_alistamento:
    print('O alistamento deverá ser realizado esse ano esse ano!')
elif ano_atual > ano_alistamento:
    print('O alistamento foi a {} anos atras.'.format(ano_atual - ano_alistamento))
else:
    print('O alistamento será daqui {} anos.'.format(ano_alistamento - ano_atual))
