"""
Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o
nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final,
tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""
nome_jogador = input('Nome do jogador: ').title()
qtde_partidas = int(input(f'Quantas partidas {nome_jogador} jogou? '))
lista_gols = []
for c in range(qtde_partidas):
    lista_gols.append(int(input(f'   Quantos gols na {c+1}ª partida? ')))
qtde_tracos = 25
print('-='*qtde_tracos)
jogador = {'nome': nome_jogador, 'gols': lista_gols, 'total_gols': sum(lista_gols)}
print(jogador)
print('-='*qtde_tracos)
print(f'O campo nome tem o valor {jogador.get("nome")}')
print(f'O campo gols tem o valor {jogador.get("gols")}')
print(f'O campo total_gols tem o valor {jogador.get("total_gols")}')
print('-='*qtde_tracos)
print(f'O jogador {jogador.get("nome")} jogou {jogador.get(len("gols"))} partidas')
cont = 1
for qtde_gols in jogador.get("gols"):
    print(f'    => Na {cont}ª partida, fez {qtde_gols} gols.')
print(f'Foi um total de {sum(jogador.get("gols"))} gols.')
