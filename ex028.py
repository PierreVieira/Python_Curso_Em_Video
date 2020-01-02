"""
Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o
usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o
usuário venceu ou perdeu.
"""
from random import randint
numero_computador = randint(0, 5)
while True:
    numero_jogador = int(input('Informe o número inteiro escolhido pelo computador de 0 a 5: '))
    if 0 <= numero_jogador <= 5:
        break
print(f'O número sorteado foi {numero_computador}\nVocê escolheu o número {numero_jogador}')
if numero_computador == numero_jogador:
    print('Você venceu!')
else:
    print('Você perdeu!')
