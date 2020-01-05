"""
Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa
em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
"""
from statistics import mean
lista_pessoas = []
while True:
    nome = input('Nome: ').title()
    while True:
        sexo = input('Sexo: ').upper()
        if sexo != 'M' and sexo != 'F':
            print('ERRO! Por favor, digite apenas M ou F')
        else:
            break
    idade = int(input('Idade: '))
    while True:
        resposta = input('Quer continuar [S/N]? ').upper()
        if resposta == 'S' or resposta == 'N':
            break
        else:
            print('ERRO! Responda apenas S ou N.')
    lista_pessoas.append({'nome': nome, 'sexo': sexo, 'idade': idade})
    if resposta == 'N':
        break
qtde_tracos = 25
print('-='*qtde_tracos)
print(f' A) Ao todo temos {len(lista_pessoas)} pessoas cadastradas.')
tupla_idades = tuple(pessoa['idade'] for pessoa in lista_pessoas)
print(f' B) A média de idade é de {mean(tupla_idades)} anos.')
mulheres_cadastradas = tuple(pessoa['nome'] for pessoa in lista_pessoas if pessoa.get("sexo") == 'F')
print(f' C) As mulheres cadastradas foram {mulheres_cadastradas}')
pessoas_acima_media = [pessoa for pessoa in lista_pessoas if pessoa['idade'] > mean(tupla_idades)]
print('  D) Lista de pessoas que estão acima da média: ')
for pessoa in pessoas_acima_media:
    print(f'   nome = {pessoa.get("nome")}; sexo = {pessoa.get("sexo")}; idade = {pessoa.get("idade")};')
print('<< ENCERRADO >>')
