from ex115.logica import tratar, pegar
from ex115.interface import exibe, menu

while True:
    menu.exibe_menu_principal()
    opcao = pegar.pegar_opcao_menu_principal()
    exibe.ver_opcao(opcao)
    tratar.tratar_opcao_menu_principal(opcao)
