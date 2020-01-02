"""
Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no
final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
"""
n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
media = (n1 + n2)*0.5
print(f'Média: {media:.2f}')
if media < 5:
    print('REPROVADO')
elif media < 6:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
