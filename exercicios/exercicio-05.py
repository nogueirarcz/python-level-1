# Curso de Engenharia de Software - Algoritmos e Estruturas de Dados
# Professor Guilherme Nogueira

# Exercício 05

'''
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos, escreva
"Seu nome é curto"; se tiver 5 e 6 letras, escreva: "Seu nome é normal"; maior que 6 escreva
"Seu nome é grande".
'''

# .---------------------------.
# |         Resolução         |
# '---------------------------'

nome = input('Digite o seu nome: ')

if len(nome) <= 4:

    print('Seu nome é curto.')

elif (len(nome) == 5 or len(nome) == 6):

    print('Seu nome é normal')

else:

    print('Seu nome é grande')
