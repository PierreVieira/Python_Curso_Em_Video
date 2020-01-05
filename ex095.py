"""
Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de
visualização de detalhes do aproveitamento de cada jogador.
"""


def preencher_lista_jogadores():
    lista_jogadores = []
    codigo = -1
    while True:
        nome_jogador = input('Nome do jogador: ').title()
        qtde_partidas = int(input(f'Quantas partidas {nome_jogador} jogou? '))
        lista_gols = []
        for c in range(qtde_partidas):
            lista_gols.append(int(input(f'   Quantos gols na {c + 1}ª partida? ')))
        while True:
            resposta = input('Quer continuar [S/N]? ').upper()
            if resposta == 'S' or resposta == 'N':
                break
        codigo += 1
        lista_jogadores.append({'codigo': codigo, 'nome': nome_jogador, 'gols': lista_gols, 'total_gols': sum(lista_gols)})
        if resposta == 'N':
            return lista_jogadores


def info_jogadores_geral(jogadores):
    c = 0
    print('{} {}{:>15}{:>15}'.format('cod', 'nome', 'gols', 'total'))
    print('--'*qtde_tracos)
    for jogador in jogadores:
        print(f'{c:>2} {jogador.get("nome"):<12}{str(jogador.get("gols")):<20}{sum(jogador.get("gols")):<10}')
    print('--'*qtde_tracos)


def info_jogadores_individual(lista_jogadores):
    while True:
        codigo_jogador = int(input('Mostrar dados de qual jogador (999 para parar)? '))
        if codigo_jogador == 999:
            break
        try:
            jogador = lista_jogadores[codigo_jogador]
        except IndexError:
            print('O jogador de código informado não existe')
        else:
            nome_jogador = jogador.get("nome")
            print(f' -- LEVANTAMENTO DO JOGADOR {nome_jogador}: ')
            for c in range(len(jogador.get("gols"))):
                print(f'     No jogo {c+1} fez {jogador.get("gols")[c]} gols.')
        finally:
            print('--'*qtde_tracos)


qtde_tracos = 25
lista_jogadores = preencher_lista_jogadores()
print('-='*qtde_tracos)
info_jogadores_geral(lista_jogadores)
info_jogadores_individual(lista_jogadores)