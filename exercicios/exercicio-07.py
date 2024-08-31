# Curso de Engenharia de Software - Algoritmos e Estruturas de Dados
# Professor Guilherme Nogueira

# Exercício 07

'''
Faça um algoritmo que esconda uma palavra e permita que o usuário tente descobrir qual é a palavra.
Quando o usuário digitar uma letra, o programa deve verificar se essa letra está na palavra secreta.
Se estiver, deve revelar a letra. Se não estiver, deve mostrar um *.
Certifique-se de mostrar o número de tentativas do usuário.
'''

# .---------------------------.
# |         Resolução         |
# '---------------------------'

import os

palavra_secreta = 'estratégia'
letras_corretas = ''
tentativas = 0

print('Tente descobrir qual é a palavra secreta!\n')

while True:

    letra_informada = input('Digite uma letra: ')
    tentativas += 1

    if len(letra_informada) > 1:

        print('Você informou mais de uma letra. Tente novamente, com apenas uma letra.')
        continue

    if letra_informada in palavra_secreta:

        letras_corretas += letra_informada

    palavra_formada = ''

    for letra_correta in palavra_secreta:

        if letra_correta in letras_corretas:

            palavra_formada += letra_correta
        
        else:

            palavra_formada += '*'
    
    print(palavra_formada)

    if palavra_formada == palavra_secreta:

        os.system('cls')

        print('Você ganhou!')
        print(f'Você realizou {tentativas} tentativas.')
        print('FIM DE JOGO.')
        break
