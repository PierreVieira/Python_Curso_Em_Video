"""
Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
"""
preco = float(input('Preço das compras: R$ '))
print('FORMAS DE PAGAMENTO')
print('[1] à vista dinheiro/cheque')
print('[2] à vista cartão')
print('[3] 2x no cartão')
print('[4] 3x ou mais no cartão')
opcao = int(input('Opção: '))
if opcao == 1:
    preco *= 0.9
elif opcao == 2:
    preco *= 0.95
elif opcao == 3:
    qtde_parcelas = int(input('Informa a quantidade de parcelas: '))
    print(f'Sua compra será parcelada em {qtde_parcelas}x de R$ {preco / qtde_parcelas:.2f} SEM JUROS.')
elif opcao == 4:
    preco *= 1.2
    qtde_parcelas = int(input('Informa a quantidade de parcelas: '))
    print(f'Sua compra será parcelada em {qtde_parcelas}x de R$ {preco/qtde_parcelas:.2f} COM JUROS.')
print(f'Preço total a pagar: R$ {preco:.2f}')
