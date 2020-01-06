def metade(valor, format=False):
    if format:
        return moeda(valor/2)


def dobro(valor, format=False):
    if format:
        return moeda(valor*2)
    return valor*2


def aumento_10_pc(valor, format=False):
    if format:
        return moeda(valor*1.1)
    return valor*1.1


def moeda(valor):
    string_valor = str(round(valor, 2)).replace('.', ',')
    cont = -1
    for caractere in range(string_valor.find(','), len(string_valor)):
        cont += 1
    if cont == 1:
        string_valor += '0'
    return string_valor
