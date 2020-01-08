def mensagem_erro():
    print('\033[0;31mERRO! Entrada inválida! Informe apenas o valor do produto\033[m')


def deu_erro(entrada):
    if len(entrada) == 0:
        mensagem_erro()
        return True
    aceitos = '0123456789,.'
    for caractere in entrada:
        if not caractere in aceitos:
            mensagem_erro()
            return True
    return False


def leia_dinheiro(texto):
    while True:
        entrada = input(texto)
        if not deu_erro(entrada):
            entrada = entrada.replace(',', '.')
            return float(entrada)
