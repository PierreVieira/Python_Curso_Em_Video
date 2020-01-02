"""
Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a
média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele
quer ou não continuar a digitar valores.
"""
lista_numeros = []
while True:
    lista_numeros.append(int(input('Digite um número: ')))
    if input('Quer continuar [S/N]? ').upper() == 'N':
        break
print(f'Você digitou {len(lista_numeros)} números e a média foi {sum(lista_numeros)/len(lista_numeros):.2f}')
print(f'O maior valor foi {max(lista_numeros)} e o menor foi {min(lista_numeros)}')
