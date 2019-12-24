"""
Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
"""
qtde_km = float(input('Informe a quantidade de km percorridos por um carro alugado: '))
qtde_dias = int(input('Informe a quantidade de dias pelos quais ele foi alugado: '))
preco_a_pagar = 60*qtde_dias + 0.15*qtde_km
print(f'O preço total a pagar é de: R$ {preco_a_pagar:.2f}')
