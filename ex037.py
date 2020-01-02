"""
Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
"""
numero = int(input('Informe um número inteiro: '))
while True:
    print('=============== ESCOLHA A CONVERSÃO ===============')
    print('[1] Binário\n[2] Octal\n[3] Hexadecimal')
    print('===================================================')
    escolha = int(input('Opção: '))
    if 1 <= escolha <= 3:
        break
print(f'{numero} em decimal = ',end='')
if escolha == 1:
    print(f'{bin(numero).replace("0b", "")} em binário')
elif escolha == 2:
    print(f'{oct(numero).replace("0o", "")} em octal')
else:
    print(f'{hex(numero).replace("0x", "")} em hexadecimal')
