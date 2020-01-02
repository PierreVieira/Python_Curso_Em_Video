while True:
    sexo = input('Informe seu sexo [M/F]: ').upper()
    if sexo == 'M' or sexo == 'F':
        break
    print('Dados inválidos!')
print(f'Sexo {sexo} registrado com sucesso.')
