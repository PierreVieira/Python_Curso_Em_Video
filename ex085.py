"""
Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista
única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
"""
lista = [[], []]
for c in range(7):
    valor = int(input(f'Informe o {c+1}º valor: '))
    if valor%2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print(f'Pares: {sorted(lista[0])}\nÍmpares: {sorted(lista[1])}')
