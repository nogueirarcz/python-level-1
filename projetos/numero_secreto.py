'''
Faça um jogo de advinhação, para que o usuário adivinhe o número entre 0 e 20
'''
import random

numero_secreto = random.randint(0, 20)
numero_informado = None

print('Estou pensando em um número entre 0 e 20.')
print('Você tem 10 tentativas.')

for tentativas in range(10):

    print('Qual número você acha que é?')
    numero_informado = int(input('Digite sua tentativa: '))

    if numero_informado < numero_secreto:

        print('Você errou. Tente um valor mais alto...')

    elif numero_informado > numero_secreto:

        print('Você errou. Tente um valor mais baixo...')

    else:

        print(f'Você acertou! Seu número de tentativas foi {tentativas + 1}')
        break

if numero_informado != numero_secreto:

    print('Seu número de tentativas acabou. Você falhou.')
    