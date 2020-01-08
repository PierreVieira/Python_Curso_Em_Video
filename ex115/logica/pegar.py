def pegar_opcao_menu_principal():
    """
    Essa função vai pegar a opção do menu principal via teclado e retorná-la
    :return: opção escolhia pelo usuário
    """
    while True:
        try:
            opcao = int(input('\033[0;32mSua opção: \033[m'))
        except ValueError:
            print('\033[0;31mInforme apenas valores inteiros!\033[m')
        else:
            if not (1 <= opcao <= 3):
                print('\033[0;31mInforme apenas uma opção entre 1 e 3!\033[m')
            else:
                break
    return opcao


def pegar_pessoa_nova():
    nome = input('Nome: ')
    while True:
        try:
            idade = int(input('Idade: '))
        except ValueError:
            print('\033[0;31mInforme apenas números inteiros para a idade!\033[m')
        else:
            break
    pessoa = nome + ';' + str(idade)
    return pessoa