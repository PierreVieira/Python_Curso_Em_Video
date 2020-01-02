"""
Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que
agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
"""
from random import randint
numero_computador = randint(0, 10)
tentativas = 1
palpite_anterior = -1
ja_disse_mais = False
ja_disse_menos = False
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
while True:
    palpite = int(input('Qual é sue palpite? '))
    if not(0 <= palpite <= 10):
        print('Eu disse que o intervalo é de 0 a 10. IMBECIL!')
    else:
        if palpite > numero_computador:
            ja_disse_menos = True
            if ja_disse_menos and palpite >= palpite_anterior and palpite_anterior != -1 and not ja_disse_mais:
                print('EU JÁ DISSE QUE FOI MENOS! VOCÊ É IDIOTA?')
            else:
                print('Menos... Tente mais uma vez.')
            ja_disse_mais = False
        elif palpite < numero_computador:
            ja_disse_menos = False
            ja_disse_mais = True
            if ja_disse_mais and palpite <= palpite_anterior and palpite_anterior != -1 and not ja_disse_menos:
                print('EU JÁ DISSE QUE FOI MAIS! VOCÊ É IDIOTA?')
            else:
                print('Mais... Tente mais uma vez.')
            ja_disse_menos = False
        else: #palpite == numero_computador
            if tentativas == 1:
                print('Acertou com uma tentativa! PARABÉNS!')
            else:
                print(f'Acertou com {tentativas} tentativas.')
            break
        tentativas += 1
        palpite_anterior = palpite
