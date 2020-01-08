from ex115.interface import exibe
from ex115.arquivos import ver_pessoas_cadastradas, fechar_arquivo, cadastrar_pessoa

def tratar_opcao_menu_principal(opcao):
    if opcao == 3:
        print('Saindo do sistema... Até logo!'.center(50))
        exibe.multiplas_linhas()
        fechar_arquivo()
        exit(0)
    elif opcao == 1:
        ver_pessoas_cadastradas()
    else: #opcao == 2
        cadastrar_pessoa()


