"""
Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final,
mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""
from statistics import mean
lista = []
while True:
    nome, peso = input('Informe o nome (apenas o primeiro) seguido do peso: ').split()
    lista.append((nome, float(peso)))
    while True:
        resposta = input('Deseja continuar [S/N]? ').upper()
        if resposta == 'S' or resposta == 'N':
            break
    if resposta == 'N':
        break
lista_pesos = [i[-1] for i in lista]
media_pesos = mean(lista_pesos)
print(f'Média dos pesos: {media_pesos:.2f}')
mais_leves = list(filter(lambda pessoa: pessoa[-1] < media_pesos, lista))
mais_pesados = list(filter(lambda pessoa: pessoa[-1] > media_pesos, lista))
peso_medio = list(filter(lambda pessoa: pessoa[-1] == media_pesos, lista))
if len(peso_medio) > 0:
    print(f'Pessoas de peso médio: {peso_medio}')
print(f'Mais leves: {mais_leves}')
print(f'Mais pesados: {mais_pesados}')
