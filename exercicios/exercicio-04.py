# Curso de Engenharia de Software - Algoritmos e Estruturas de Dados
# Professor Guilherme Nogueira

# Exercício 04

'''
Faça um programa que pergunte a hora ao usuário e, com base no horário descrito, exiba uma saudação.
Bom dia, boa tarde ou boa noite.
'''

# .---------------------------.
# |         Resolução         |
# '---------------------------'

horario = input('Digite a hora em números inteiros (24h): ')

try:

    horario = int(horario)

    if (horario >= 00 and horario <= 11):

        print('Bom dia!')

    elif (horario >= 12 and horario <= 18):

        print('Boa tarde')

    else:

        print('Boa noite')

except:

    print('O valor que você digitou é inválido. Tente novamente.')
    