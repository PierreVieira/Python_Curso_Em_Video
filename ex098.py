"""
Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim
e passo. Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
"""
from time import sleep


def contar(inicio, fim, passo):
    passo = abs(passo)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio <= fim:
        fim += 1
    else:
        fim -= 1
        passo = -passo
    for c in range(inicio, fim, passo):
        print(c, end=' ')
        sleep(0.5)
    print('FIM!')


qtde_tracos = 20
print('-='*qtde_tracos)
contar(1, 10, 1)
print('-='*qtde_tracos)
contar(10, 0, 2)
print('-='*qtde_tracos)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
print('-='*qtde_tracos)
contar(inicio, fim, passo)
