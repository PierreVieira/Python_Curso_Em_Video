"""
Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
"""
nome = input('Nome: ')
while True:
    try:
        media = float(input(f'Média de {nome}: '))
    except ValueError:
        print('Informe apenas números! Digite ponto ao invés de vírgula para separar casas decimais.')
    else:
        break
print('-='*20)
if media <= 3:
    situacao = 'reprovado'
elif media < 6:
    situacao = 'recuperacao'
else:
    situacao = 'aprovado'
dicionario = {'nome': nome, 'media': media, 'situacao': situacao}
print(f'  -nome é igual a {dicionario.get("nome")}')
print(f'  -média é igual a {dicionario.get("media")}')
print(f'  -situação é igual a {dicionario.get("situacao")}')
