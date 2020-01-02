"""
Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""


def abrindo_e_fechando_corretamente(expressao):
    anterior = ''
    for c in expressao:
        if anterior != '' and (anterior == ')' and c == '('):
            return False
        else:
            anterior = c
    return True


def primeiro_parentese_fechando(expressao):
    s = ""
    for c in expressao:
        s += c
        if s.count(")") == 1 and s.count("(") == 0:
            return True
    return False


def ultimo_parentese_abrindo(expressao):
    return expressao[-1] == '('


expressao = input('Digite uma expressão matemática: ')


if expressao.count('(') != expressao.count(')'):
    print('O número de parênteses fechando não é igual ao número de parênteses abrindo!')
elif "()" in expressao:
    print('Não é permitido parênteses vazios!')
elif primeiro_parentese_fechando(expressao):
    print('A expressão está começando com o parêntese fechando.')
elif ultimo_parentese_abrindo(expressao):
    print('A expressão está encerrando com o último parêntese abrindo.')
else:
    if abrindo_e_fechando_corretamente(expressao):
        print('Expressão OK!')
    else:
        print('Abrindo e fechando parênteses incorretamente!')