"""
Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""
from random import shuffle
nomes = input('Informe o nome dos quatro alunos separando por espaço: ').split()
shuffle(nomes)
print('A ordem de apresentação será: {}'.format(nomes))
