"""
Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de
Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.
"""
# Dados do Campeonato Brasileiro de 2019
times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Atlético-PR', 'São Paulo', 'Internacional', 'Corinthians',
         'Fortaleza', 'Goiás', 'Bahia', 'Vasco da Gama', 'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará SC',
         'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
qtde_tracos = 138
print('-=' * qtde_tracos)
print(f'Os 5 primeiros times: {times[:5:]}')
# print(f'Os últimos 4 colocados: {times[16::]}')
print(f'Os últimos 4 colocados: {times[-4::]}')
print(f'Times em ordem alfabética: {sorted(times)}')
print(f'O chapecoense está em {times.index("Chapecoense") + 1}º lugar.')
print('-=' * qtde_tracos)
