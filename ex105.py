"""
Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai
retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
"""
from statistics import mean


def notas(*notas, situacao=False):
    """
    A função notas serve para analisar várias notas passadas como parâmetro
    :param notas: As notas a serem analisadas
    :param situacao: Parâmetro opcional, caso seja verdadeiro irá retornar, junto ao retorno  do dicionário padrão,
    a situação do discente. Por padrão esse parâmetro é falso.
    :return: Dicionário contendo, por padrão, a quantidade de notas informadas, a maior nota, a menor nota e a média das
    notas.
    """
    qtde_notas = len(notas)
    maior_nota = max(notas)
    menor_nota = min(notas)
    media_notas = mean(notas)
    if situacao:
        if media_notas < 4:
            s = 'REPROVADO'
        elif media_notas < 6:
            s = 'RECUPERAÇÃO'
        else:
            s = 'APROVADO'
        return {'qtde_notas': qtde_notas, 'maior_nota': maior_nota, 'menor_nota': menor_nota, 'media_notas': media_notas
                , 'situacao': s}
    return {'qtde_notas': qtde_notas, 'maior_nota': maior_nota, 'menor_nota': menor_nota, 'media_notas': media_notas}


print(notas(2, 3, 4.5, 1.2, situacao=True))
print(notas(6, 4.5, 7, 5, situacao=True))
print(notas(10, 5, 8, 9.2, situacao=True))
help(notas)