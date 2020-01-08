"""
Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da
digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
"""
def msg_erro(tipo):
    print(f'\033[1;31mERRO! Digite um número {tipo} válido.\033[m')


def leiaInt(*args):
    while True:
        try:
            inteiro = int(input(*args))
        except ValueError:
            msg_erro('inteiro')
        else:
            return inteiro


def leiaFloat(*args):
    while True:
        try:
            real = float(input(*args))
        except ValueError:
            msg_erro('real')
        else:
            return real


inteiro = leiaInt('Digite um número inteiro: ')
print(f'Você acabou de digitar o número {inteiro}')
real = leiaFloat('Digite um número real: ')
print(f'Você acabou de digitar o número {real}')