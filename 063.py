"""
Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros
elementos de uma Sequência de Fibonacci.
"""
print('-'*40)
print('Sequência de Fibonacci'.center(40))
print('-'*40)
mostrar = int(input('Quantos termos você quer mostrar? '))
primeiro = 0
segundo = 1
if mostrar <= 0:
    print('Bye')
elif mostrar == 1:
    print('0 -> FIM')
elif mostrar == 2:
    print('0 -> 1 -> FIM')
else:
    print('0 -> 1 -> ',end='')
    mostrar -= 2
    while mostrar > 0:
        proximo = primeiro + segundo
        primeiro = segundo
        segundo = proximo
        print(proximo, end=' -> ')
        mostrar -= 1
    print('FIM')
