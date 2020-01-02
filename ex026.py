"""
Exercício Python 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
"""
#Forma very easy
frase = input('Digite uma frase: ').strip().upper()
print(f'A letra A aparece {frase.count("A")} vezes\nA primeira letra A apreceu na posição {frase.find("A") + 1}')
print(f'A última letra A apareceu na posição {frase.rfind("A") + 1}')

#Forma +/- raiz
"""
def ultima_aparicao(palavra, frase):
    soma_index = 0
    posicao = 0
    while True:
        try:
            posicao = frase.index(palavra, soma_index)
            soma_index += posicao
            if soma_index == 0:
                soma_index += 1
        except ValueError:
            soma_index -= posicao
            break
    return soma_index


frase = input('Digite uma frase: ').strip().upper()
print(f'A letra A aparece {frase.count("A")} vezes\nA primeira letra A apreceu na posição {frase.index("A") + 1}')
print(f'A última letra A apareceu na posição {ultima_aparicao("A", frase)}')
"""