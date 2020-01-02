"""
Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados,
em ordem crescente.
"""
lista = []
while True:
    try:
        numero = int(input('Digite um número: '))
        if not (numero in lista):
            lista.append(numero)
        while True:
            resposta = input('Quer continuar [S/N]? ').upper()
            if resposta == 'S' or resposta == 'N':
                break
        if resposta == 'N':
            break
    except ValueError:
        print('Digite apenas números!')
print(f'Você digitou os valores {sorted(lista)}')
