"""
Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
"""
dist_metros = float(input('Uma distância em metros: '))
print(f'A medida de {dist_metros} m corresponde a\n{dist_metros/1000} km\n{dist_metros/100} hm\n{dist_metros/10} dam')
print(f'{dist_metros*10} dm\n{dist_metros*100} cm\n{dist_metros*1000} mm')
