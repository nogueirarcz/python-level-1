# Curso de Engenharia de Software - Algoritmos e Estruturas de Dados
# Professor Guilherme Nogueira

# Exercício 10

"""
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
Faça um programa capaz de gerar a série até o n−ésimo termo.
"""

# .---------------------------.
# |         Resolução         |
# '---------------------------'
termos = int(input("Digite o numero de termos da série de Fibonacci: "))

numero = 1
numero_anterior = 0

for termo in range(termos):

    print(numero)

    aux = numero
    numero += numero_anterior
    numero_anterior = aux
    