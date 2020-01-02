"""
Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor
da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou
então o empréstimo será negado.
"""
valor_casa = float(input('Informe o valor da casa: R$ '))
salario = float(input('Informe o salário do comprador: R$ '))
qtde_anos = int(input('Informe em quantos anos você irá pagar a casa: '))
prestacao_mensal = valor_casa/(12*qtde_anos)
if prestacao_mensal > salario*0.3:
    print('EMPRÉSTIMO NEGADO!\nA prestação mensal excede 30% do valor do salário')
else:
    print('EMPRÉSTIMO CONCEDIDO!')
print(f'Prestação mensal: R$ {prestacao_mensal:.2f}')
