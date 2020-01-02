"""
Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa
Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- IMC entre 18,6 e 24,9: Peso ideal (parabéns)
- IMC entre 25 e 29,9: Levemente acima do peso
- IMC entre 30 e 34,9: Obesidade grau I
- IMC entre 35 e 39,9: Obesidade grau II (severa)
- IMC acima de 40: Obesidade grau III (mórbida)
"""
peso = float(input('Qual é o seu peso em quilos? '))
altura = float(input('Qual é a sua altura em metros? '))
imc = peso/(altura**2)
print(f'IMC: {imc:.2f}')
if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal. Parabéns!')
elif imc < 30:
    print('Levemente acima do peso')
elif imc < 35:
    print('Obesidade grau I')
elif imc < 40:
    print('Obesidade grau II (severa)')
else:
    print('Obesidade grau III (mórbida)')