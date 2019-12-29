"""
Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""
preco_produto = float(input('Informe o preço do produto: R$ '))
print(f'O novo preço do produto é R$ {preco_produto*0.95:.2f}')
