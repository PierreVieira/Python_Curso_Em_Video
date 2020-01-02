"""
Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que
ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
"""
from random import choice
lista_alunos = input('Informe o nome dos quatro alunos separando por espaço: ').split()
print(f'O aluno sorteado foi {choice(lista_alunos)}.')