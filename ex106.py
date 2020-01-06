"""
Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e
o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.
"""


def print_colorido(texto, style, text_color, backgroud_color):
    print(f'\033[{style};{text_color};{backgroud_color}m{texto}\033[m')


def apresentacao():
    palavra = 'SISTEMA DE AJUDA PyHELP'
    qtde_tracos = len(palavra) + 4
    print_colorido('~' * qtde_tracos, 1, 30, 42)
    print_colorido(palavra.center(qtde_tracos), 1, 30, 42)
    print_colorido('~' * qtde_tracos, 1, 30, 42)


def ate_logo():
    palavra = 'ATÉ LOGO!'
    qtde_tracos = len(palavra) + 4
    print_colorido('~' * qtde_tracos, 1, 30, 41)
    print_colorido(palavra.center(qtde_tracos), 1, 30, 41)
    print_colorido('~' * qtde_tracos, 1, 30, 41)


def msg_acessa_comando(comando):
    palavra = f"Acessando o manual do comando '{comando}'"
    qtde_tracos = len(palavra) + 4
    print_colorido('~' * qtde_tracos, 1, 30, 44)
    print_colorido(palavra.center(qtde_tracos), 1, 30, 44)
    print_colorido('~' * qtde_tracos, 1, 30, 44)


def acessa_comando(comando):
    #Não dá para usar a função print colorido aqui pois help não retorna nada
    print('\033[1;37;40m')
    help(comando)


while True:
    apresentacao()
    resposta = input('Função ou Biblioteca: ')
    if resposta.upper() == 'FIM':
        ate_logo()
        break
    msg_acessa_comando(resposta)
    acessa_comando(resposta)
