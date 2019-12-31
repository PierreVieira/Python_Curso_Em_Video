"""
Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.
"""
print('='*33)
print('GERADOR DE PA'.center(30))
print('='*33)
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
qtde_mostrados = 10
mostrar = 10
while True:
    for c in range(mostrar):
        print(primeiro_termo, end=' -> ')
        primeiro_termo += razao
    print('PAUSA')
    mostrar = int(input('Quantos termos você quer mostrar a mais? '))
    if mostrar == 0:
        break
    qtde_mostrados += mostrar
print(f'Progressão finalizada com {qtde_mostrados} termos mostrados.')

