from ex115.logica.pegar import pegar_pessoa_nova


def inicializar_leitura(caminho_arquivo):
    """
    Verifica se o arquivo existe, caso não exista, um novo arquivo é criado.
    :return: refernêcia para o arquivo informado.
    """
    while True:
        try:
            return open(caminho_arquivo, 'rt', encoding="utf-8")  # coloca-se o "utf-8" para ele pegar os acentos
        except FileNotFoundError:
            open(caminho_arquivo, 'a')


def ver_pessoas_cadastradas():
    """
    Exibe todas as pessoas cadastradas no arquivo.
    :return: None
    """
    referencia_arquivo.seek(0)  # Posiciona o ponteiro no início do arquivo
    pessoas_cadastradas = referencia_arquivo.readlines()
    pessoas_cadastradas = tuple(pessoa.strip('\n').split(';') for pessoa in pessoas_cadastradas)

    for pessoa in pessoas_cadastradas:
        print(f'{pessoa[0]:<42}{pessoa[1]:} anos')


def fechar_arquivo():
    referencia_arquivo.close()


def cadastrar_pessoa():
    """
    Cadastra uma nova pessoa no arquivo.
    :return: None
    """
    referencia_arquivo = open('pessoas_cadastradas.txt', 'a')
    pessoa = pegar_pessoa_nova()
    referencia_arquivo.write(pessoa + '\n')


referencia_arquivo = inicializar_leitura('pessoas_cadastradas.txt')
