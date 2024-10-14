from random import randint
# Busca linear em lista não ordenada com alocação sequencial

# Considere que não temos nenhuma informação a respeito da lista, como a quantidade de elementos, por exemplo.
# Sabemos apenas qual é o elmento que queremos encontrar, mas não temos ideia de onde ele está

lista = []

tamanho = randint(1, 200)
for num in range(tamanho):

    lista.append(randint(1, tamanho))

    if num == lista[-1]:

        num = randint(1, tamanho)

def busca(lista, elemento): # Uma função de busca, que deve receber a lista e o elemento a ser encontrado

    for indice in range(len(lista)): # Para cada elemento da lista, iremos comparar com nosso elemento a ser encontrado

        if lista[indice] == elemento: # Caso o elemento seja igual, retornaremos o seu índice

            return indice
        
    return None # Caso o elemento não seja encontrado na lista, retornaremos None

# Vamos testar
print(busca(lista, 10))
