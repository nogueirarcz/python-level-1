# Lista Sequencial Não Ordenada

from random import randint

lista = []

tamanho = randint(1, 200)

while len(lista) != tamanho:

    for num in range(tamanho):

        num_random = randint(1, tamanho)

        if num_random not in lista:

            lista.append(num_random)

print(lista)

# Busca Linear
def busca(lista, elemento):

    for indice in range(len(lista)):

        if lista[indice] == elemento:

            return indice
        
    return None

resultado = busca(lista, 155)

if resultado is None:

    print('O elemento procurado não está na lista')

else:

    print(f'O elemento procurado está no índice {resultado}')
