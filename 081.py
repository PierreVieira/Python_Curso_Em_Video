"""
Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""
numeros = []
while True:
    try:
        numero = int(input('Informe um número inteiro: '))
        numeros.append(numero)
        while True:
            resposta = input('Deseja continuar [S/N]? ').upper()
            if resposta == 'S' or resposta == 'N':
                break
        if resposta == 'N':
            break
    except ValueError:
        print('Digite apenas números inteiros!')
print(f'\nAo todo foram digitados {len(numeros)} números')
print(f'Em ordem decrescente temos {sorted(numeros, reverse=True)}')
if 5 in numeros:
    print('O número 5 está na lista.')
else:
    print('O número 5 não está na lista.')
