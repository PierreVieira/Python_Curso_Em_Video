"""
Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre
todos os valores pares sorteados pela função anterior.
"""
from random import sample


def sorteia():
    lista = sample(range(1, 10), 5)
    print(f'Sorteando 5 valores da lista: {lista}')
    return lista


def sum_only_pares(lista):
    print(f'Somando os valores pares de {lista}, temos {sum(list(filter(lambda x: x % 2 == 0, lista)))}')


lista = sorteia()
sum_only_pares(lista)
