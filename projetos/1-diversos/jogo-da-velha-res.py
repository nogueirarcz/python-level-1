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

def verifica_vitoria(tabuleiro, jogador):
     #verifica linhas
     if (tabuleiro['top-l'] == tabuleiro['top-m'] == tabuleiro['top-r'] == jogador or
         tabuleiro['mid-l'] == tabuleiro['mid-m'] == tabuleiro['mid-r'] == jogador or 
         tabuleiro['low-l'] == tabuleiro['low-m'] == tabuleiro['low-r'] == jogador):
          return True
     #verifica colunas
     if (tabuleiro['top-l'] == tabuleiro['mid-l'] == tabuleiro['low-l'] == jogador or
         tabuleiro['top-m'] == tabuleiro['mid-m'] == tabuleiro['low-m'] == jogador or 
         tabuleiro['top-r'] == tabuleiro['mid-r'] == tabuleiro['low-r'] == jogador):
          return True
     #verifica as diagonais
     if (tabuleiro['top-l'] == tabuleiro['mid-m'] == tabuleiro['low-r'] == jogador or
         tabuleiro['top-r'] == tabuleiro['mid-m'] == tabuleiro['low-l'] == jogador):
          return True 
       
jogador = 'x'

for i in range(9):

    mostrar_tabuleiro(tabuleiro)
    print(f'É a vez do jogador [{jogador}]')
    movimento = input('Digite o seu movimento: ')

    tabuleiro[movimento] = jogador
        
    if verifica_vitoria(tabuleiro, jogador):
        mostrar_tabuleiro(tabuleiro)
        print(f'O jogador [{jogador}] venceu!')
        break
    
    if jogador == 'x':

             jogador = 'o'
    
    else:

            jogador = 'x'       

else:
    mostrar_tabuleiro(tabuleiro)
    print("Empate!")