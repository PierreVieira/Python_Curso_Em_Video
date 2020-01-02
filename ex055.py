lista_pesos = []
for c in range(1, 6):
    lista_pesos.append(float(input(f'Peso da {c}ª pessoa: ')))
print('-='*16)
print(f'O maior peso lido foi de {max(lista_pesos)}Kg')
print(f'O menor peso lido foi de {min(lista_pesos)}Kg')
print('-='*16)
