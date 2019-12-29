"""
Exercício Python 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as
informações possíveis sobre ele.
"""
algo = input('Digite algo: ')
print('O tipo primitivo desse valor é {}'.format(type(algo)))
print(f'Só tem espaços? {algo.isspace()}\nÉ um número? {algo.isnumeric()}\nÉ alfabético? {algo.isalpha()}\n'
      f'É alfanumérico? {algo.isalnum()}\nEstá em maiúsculas? {algo.isupper()}\nEstá em minúsculas? '
      f'{algo.islower()}\nEstá capitalizada? {algo.istitle()}')
