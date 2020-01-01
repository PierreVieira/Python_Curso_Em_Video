"""
Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na
sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""
qtde_tracos = 40
tupla_materiais = (('Lápis', 1.75), ('Borracha', 2.00), ('Caderno', 15.90), ('Estojo', 25.00), ('Transferidor', 4.20), ('Compasso',
                    9.99), ('Mochila', 120.32), ('Canetas', 22.30), ('Livro', 34.90))
print('-'*qtde_tracos)
print('LISTAGEM DE PREÇOS'.center(qtde_tracos))
print('-'*qtde_tracos)
for material in tupla_materiais:
    nome = material[0]
    preco = material[1]
    print('{:.<30}R${:>7}'.format(nome, preco))
print('-'*qtde_tracos)