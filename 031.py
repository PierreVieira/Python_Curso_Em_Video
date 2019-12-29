"""
Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
"""
distancia_viagem = float(input('Informe a distância da viagem em km: '))
if distancia_viagem <= 200:
    preco = distancia_viagem * 0.5
else:
    preco = distancia_viagem * 0.45
print(f'Distância percorrida: {distancia_viagem} km\nPreço total a se pagar: R$ {preco:.2f}')
