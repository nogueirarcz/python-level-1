tabuleiro = {'top-l': ' ', 'top-m': ' ', 'top-r': ' ',
    'mid-l': ' ', 'mid-m': ' ', 'mid-r': ' ',
    'low-l': ' ', 'low-m': ' ', 'low-r': ' '             
}

def mostrar_tabuleiro(tabuleiro):

    print(tabuleiro['top-l'] +' | '+ tabuleiro['top-m'] +' | '+ tabuleiro['top-r'])
    print('- + - + -')

    print(tabuleiro['mid-l'] +' | '+ tabuleiro['mid-m'] +' | '+ tabuleiro['mid-r'])
    print('- + - + -')

    print(tabuleiro['low-l'] +' | '+ tabuleiro['low-m'] +' | '+ tabuleiro['low-r'])

jogador = 'x'

for i in range(9):

    mostrar_tabuleiro(tabuleiro)
    print(f'É a vez do jogador [{jogador}]')
    movimento = input('Digite o seu movimento: ')

    tabuleiro[movimento] = jogador

    if jogador == 'x':

        jogador = 'o'
    
    else:

        jogador == 'x'

    mostrar_tabuleiro(tabuleiro)
    