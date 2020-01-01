"""
Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas
extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o
conteúdo das três listas geradas.
"""
def tratar_entrada():
    while True:
        try:
            numero = int(input('Informe um número inteiro: '))
            numeros.append(numero)
            while True:
                resposta = input('Deseja continuar [S/N]? ').upper()
                if resposta == 'S' or resposta == 'N':
                    break
            if resposta == 'N':
                break
        except ValueError:
            print('Digite apenas números inteiros!')
numeros = []
tratar_entrada()
pares = [numero for numero in numeros if numero % 2 == 0] #List comprehension
impares = list(filter(lambda x: x % 2 == 1, numeros)) #Filter
print(f'Todos os números informados: {numeros}')
print(f'Apenas os números pares: {pares}')
print(f'Apenas os números ímpares: {impares}')
