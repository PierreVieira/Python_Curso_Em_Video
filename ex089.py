"""
Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno
individualmente.
"""
from statistics import mean

def pegar_nome():
    while True: #Garantindo que o nome está certo
        nome = input('Nome: ').title()
        if not(nome.isalpha()):
            print('Digite apenas caracteres!')
        else:
            return nome


def pegar_nota(n):
    while True:
        try:
            nota = float(input(f'Nota {n}: '))
        except ValueError:
            print('Informe apenas números! Utilize ponto em vez de vírgula para separar casas decimais.')
        else:
            return nota


def pegar_resposta():
    while True:
        resposta = input('Deseja continuar [S/N]? ').upper()
        if resposta == 'S' or resposta == 'N':
            return resposta

def info_geral():
    for aluno in lista_alunos:
        print('{:<3}{:<9}{:>8.1f}'.format(aluno[0], aluno[1], aluno[3]))

def tratar_entrada_n_aluno():
    number = -1
    while not (0 <= number <= len(lista_alunos) - 1) and number != 999:
        try:
            number = int(input('Mostrar notas de qual aluno?  (999 interrompe): '))
        except ValueError:
            print('Informe apenas valores inteiros!')
        else:
            return number



number_aluno = 1
lista_alunos = []
while True:
    nome = pegar_nome()
    nota1 = pegar_nota(1)
    nota2 = pegar_nota(2)
    lista_aluno = [number_aluno, nome, [nota1, nota2], mean([nota1, nota2])]
    lista_alunos.append(lista_aluno)
    resposta = pegar_resposta()
    if resposta == 'N':
        break
qtde_tracos = 10
print('-='*qtde_tracos)
print('No. NOME{:>11}'.format("MÉDIA"))
print('-'*qtde_tracos*2)
info_geral()
while True:
    print('--'*25)
    n_aluno = tratar_entrada_n_aluno()
    if n_aluno == 999:
        break
    else:
        print(f'Notas de {lista_alunos[n_aluno][1]} são {lista_alunos[n_aluno][2]}')
