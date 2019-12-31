"""
Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for.
"""
numero = int(input('Digite um número par ver sua tabuada: '))
print('-'*15)
for c in range(10):
    print(f'{numero:2} X {c+1:2} = {numero*(c+1):2}')
print('-'*15)