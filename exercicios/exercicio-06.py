# Curso de Engenharia de Software - Algoritmos e Estruturas de Dados
# Professor Guilherme Nogueira

# Exercício 06

'''
Faça um programa que leia o nome do usuário e com um loop while reescreve esse nome em posição vertical".
'''

# .---------------------------.
# |         Resolução         |
# '---------------------------'

nome = input('Digite o seu nome: ')
indice = 0

while indice < len(nome):

    print(nome[indice])
    indice += 1
