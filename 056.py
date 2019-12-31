"""
Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a
média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
"""
nome_homem_mais_velho = ''
idade_homem_mais_velho = -1
qtde_mulheres_menos_20 = 0
soma_idade = 0
for c in range(4):
    print('-'*4, end=' ')
    print(f'{c+1}ª PESSOA', end=' ')
    print('-' * 4)
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    soma_idade += idade
    while True:
        sexo = input('Sexo [M/F]: ').upper()
        if sexo == 'M' or sexo == 'F':
            break
    if sexo == 'M' and idade_homem_mais_velho < idade:
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome
    elif sexo == 'F' and idade < 20:
        qtde_mulheres_menos_20 += 1
if idade_homem_mais_velho != -1:
    print(f'O homem mais velho tem {idade_homem_mais_velho} anos e se chama {nome_homem_mais_velho}.')
if qtde_mulheres_menos_20 != 1:
    print(f'Existem {qtde_mulheres_menos_20} mulheres com menos de 20 anos.')
else:
    print('Existe uma mulher com menos de 20 anos.')
print(f'A média das idades informadas é {soma_idade/4:.2f} anos')
