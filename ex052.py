def mostrar_divisores():
    for c in diviores:
        print(c, end=' ')
    print()

diviores = []
numero = int(input('Digite um número: '))
for c in range(1, numero+1):
    print(c, end=' ')
    if numero % c == 0:
        diviores.append(c)
qtde_div = len(diviores)
print(f'\nO número {numero} foi divisível {qtde_div} vezes')
mostrar_divisores()
if qtde_div == 2:
    print('E por isso ele É PRIMO')
else:
    print('E por isso ele não É PRIMO')
