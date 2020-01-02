"""
Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.
"""
qtde_pessoas_maiores_18 = 0
homens_cadastrados = 0
qtde_mulher_menor_20 = 0
qtde_tracos = 30
while True:
    print('-'*qtde_tracos)
    print('CADASTRE UMA PESSSOA'.center(qtde_tracos))
    print('-'*qtde_tracos)
    idade = int(input('Idade: '))
    while True:
        sexo = input('Sexo [M/F]: ').upper()
        print('-' * qtde_tracos)
        if sexo == 'M' or sexo == 'F':
            break
    while True:
        resposta = input('Quer continuar [S/N]? ').upper()
        if resposta == 'S' or resposta == 'N':
            break
    if idade > 18:
        qtde_pessoas_maiores_18 += 1
    if sexo == 'M':
        homens_cadastrados += 1
    elif sexo == 'F' and idade < 20:
        qtde_mulher_menor_20 += 1
    if resposta == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {qtde_pessoas_maiores_18}')
print(f'Total de homens cadastrados: {homens_cadastrados}')
print(f'Mulheres com menos de 20 anos: {qtde_mulher_menor_20}')
