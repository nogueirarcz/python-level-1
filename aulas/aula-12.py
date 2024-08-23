# Criando uma lista em Python
lista_de_compras = ['Mouse', 'Teclado', 'Monitor-TV', 'Headset']

# Exibindo o conteúdo da lista
print(lista_de_compras)

# Exibindo por índice
print(lista_de_compras[0])
print(lista_de_compras[1])
print(lista_de_compras[2])

# Podemos usar índices negativos para usar a ordem inversa da lista
print('Ordem inversa:')
print(lista_de_compras[-1])
print(lista_de_compras[-2])
print(lista_de_compras[-3])

# Podemos exibir um intervalo de uma lista
print(lista_de_compras[0:3])

# Observe que existe uma classe específica para o tipo de dados em lista
print(type(lista_de_compras))

# Pode-se utilizar métodos específicos da classe list
lista_de_compras.append('Mousepad') # O método append() insere um novo elemento no fim da lista

lista_de_compras.insert(1, 'Processador') # Inserindo no índice 1 o elemento Processador
print(lista_de_compras)

# Também há métodos para eliminar elementos da lista
del lista_de_compras[0] # Aqui iremos deletar o elemento que ocupa a posição 0
print(lista_de_compras)

# Com o método remove, podemos deletar um elemento com base em seu valor, não em seu índice
lista_de_compras.remove('Teclado')
print(lista_de_compras)

# O método pop remove o último item da lista e o retorna, assim ele pode ser armazenado em uma variável
item_removido = lista_de_compras.pop()
print(lista_de_compras)
print(item_removido)

# Com o método count, posso contar quantas ocorrências de um elemento há na lista
print(lista_de_compras.count('Monitor-TV'))

# Também podemos passar para uma lista, os elementos de outra lista, sem que esta primeira perca seus próprios elementos.
lista_a = [0, 1, 2]
lista_b = [3, 4, 5]

# Para isso usamos o método extends
lista_a.extend(lista_b)
print(lista_a)

# Podemos usar o método clear para eliminar todos os elementos de uma lista
lista_b.clear()
print(lista_b)
