# Curso de Engenharia de Software - Algoritmos e Estruturas de Dados
# Professor Guilherme Nogueira

# Exercício 03

'''
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par
ou ímpar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
'''

# .---------------------------.
# |         Resolução         |
# '---------------------------'

numero = input('Digite um número inteiro: ')

if numero.isdigit():

    numero = int(numero)

    if (numero % 2 == 0):

        print(f'O número {numero} é par.')
    
    else:

        print(f'O número {numero} é ímpar.')

else:

    print('Você não informou um número inteiro. Tente novamente!')
