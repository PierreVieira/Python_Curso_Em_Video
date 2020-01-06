"""
Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função
input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')
"""


def leiaInt(*args):
    while True:
        str = input(*args)
        if not str.isnumeric():
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
        else:
            return str

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
