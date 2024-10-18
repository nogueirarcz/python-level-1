# Lista Sequencial Não Ordenada

from random import randint

lista = []

tamanho = randint(1, 10)

while len(lista) != tamanho:

    for num in range(tamanho):

        num_random = randint(1, tamanho)

        if num_random not in lista:

            lista.append(num_random)

print(lista)
