"""
Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
"""


def posicao_maior(numero):
    """
    Identifica a posição do número menor que seja maior ao maior número passado como parâmetro na lista
    :param numero: número a ser utilizado como parâmetro de pesquisa
    :return: posição do número menor que seja maior ao número passado como parâmetro. Caso não tenha nenhum número maior
    a função retorna o tamanho da lista
    """
    for c in range(len(lista)):
        if lista[c] > numero:
            return c
    return len(lista)


def add_correto(numero):
    """
    Adiciona um número em uma posição da lista de forma que ela fique ordenada crescentemente
    :param numero: número que será retornado
    :return: Nothing
    """
    posicao = posicao_maior(numero)
    if posicao == 0:
        print(f'Adicionando o número {numero} no início.')
    elif posicao == len(lista):
        print(f'Adicionando o número {numero} no fim da lista.')
    else:
        print(f'Adicionando na posição {posicao} o número {numero}')
    lista.insert(posicao, numero)


lista = []
for c in range(5):
    numero = int(input(f'Digite o {c+1}º valor: '))
    add_correto(numero)
print(f'Lista: {lista}')