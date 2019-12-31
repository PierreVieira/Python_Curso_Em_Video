"""
Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o
usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
"""
qtde_tracos = 30
print('-'*qtde_tracos)
print('LOJA SUPER BARATÃO'.center(qtde_tracos))
print('-'*qtde_tracos)
total_compra = 0
qtde_produtos_maior_que_1000 = 0
mais_barato = ''
produto_mais_barato = ''
while True:
    nome_produto = input('Nome do produto: ')
    preco = float(input('Preço: R$ '))
    total_compra += preco
    if preco > 1000:
        qtde_produtos_maior_que_1000 += 1
    if mais_barato == '':
        mais_barato = preco
        produto_mais_barato = nome_produto
    elif preco < mais_barato:
        mais_barato = preco
        produto_mais_barato = nome_produto
    while True:
        continuar = input('Quer continuar [S/N]? ').upper()
        if continuar == 'S' or continuar == 'N':
            break
    if continuar == 'N':
        break
print('-'*(qtde_tracos//2), end=' ')
print('FIM DO PROGRAMA', end=' ')
print('-'*(qtde_tracos//2))
print(f'O total da compra foi R$ {total_compra:.2f}')
print(f'Quantidade de progutos custando mais de R$ 1000.00: {qtde_produtos_maior_que_1000}')
print(f'O produto mais barato foi {produto_mais_barato} que custa R$ {mais_barato:.2f}')
