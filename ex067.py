"""
Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
pelo usuário. O programa será interrompido quando o número solicitado for negativo.
"""
while True:
    numero = int(input('Digite um número par ver sua tabuada: '))
    if numero < 0:
        break
    print('-'*15)
    for c in range(10):
        print(f'{numero:2} X {c+1:2} = {numero*(c+1):2}')
    print('-'*15)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
