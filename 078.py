"""
Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""
def encontra_todas_ocorrencias_do_numero(numero):
    lista2 = []
    for c in range(len(lista)):
        if lista[c] == numero:
            lista2.append(c)
    return lista2

lista = list(map(int, input('Informe 5 valores: ').split()))
maior = max(lista)
menor = min(lista)
aparicoes_maior = encontra_todas_ocorrencias_do_numero(maior)
aparicoes_menor = encontra_todas_ocorrencias_do_numero(menor)
print(f'O maior número encontrado foi {maior} e ele está nas posições {str(aparicoes_maior).replace("[","").replace("]", "")}')
print(f'O menor número encontrado foi {menor} e ele está nas posições {str(aparicoes_menor).replace("[","").replace("]", "")}')