"""
Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
"""
nome_completo = input('Informe seu nome completo: ').strip()
print(f'Tudo maiúsculo: {nome_completo.upper()}\nTudo minúsculo: {nome_completo.lower()}')
sem_espacos = ''.join(nome_completo.split())
print(f'Total de letras sem considerar espaços: {len(sem_espacos)}')
