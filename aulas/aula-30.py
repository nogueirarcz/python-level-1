# introdução a list comprehension

# Trata-se de uma forma de criar listas através de iteráveis

# Vamos ver um método de tradicional para criar listas
print(list(range(10)))

# Outro método para ter este mesmo resultado, seria o seguinte
lista = []

for num in range(10):

    lista.append(num)

print(lista)

print()

# Agora vamos utilizar list comprehension para essa mesma proposta
lista = [num for num in range(10)]  # Desse modo, executamos o for no momento de declarar a lista

print(lista)

# Além disso, podemos adicionar qualquer lógica de programação dentro desta declaração. Vamos construir uma lista com o dobro dos valores

lista_dobrada = [
    num * 2
    for num in range(10)
]

print(lista_dobrada)

# Vamos fazer também uma lista de quadrados
lista_quadrados = [
    num ** 2
    for num in range(10)
]

print(lista_quadrados)
