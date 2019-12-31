"""
Exercício Python 048: Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se
encontram no intervalo de 1 até 500.
"""
s = 0
for c in range(3, 501, 6): # O passo é 6 pois (3 devido aos multiplos de 3 e *2 para pegar apeans os ímpares
    s += c
print(f'A soma dos {500//6} valores solicitados é {s}')
