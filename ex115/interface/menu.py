from ex115.interface.exibe import multiplas_linhas


def exibe_menu_principal():
    """
    Função que exibe o menu principal
    :return: None
    """
    multiplas_linhas()
    print('MENU PRINCIPAL'.center(50))
    multiplas_linhas()
    print('\033[0;32m1 -\033[m', end=' ')
    print('\033[0;34mVer pessoas cadastradas')
    print('\033[0;32m2 -\033[m', end=' ')
    print('\033[0;34mCadastrar nova pessoa')
    print('\033[0;32m3 -\033[m', end=' ')
    print('\033[0;34mSair do sistema\033[m')
    multiplas_linhas()