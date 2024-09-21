# Métodos úteis com set

conjunto_a = set()  # Declarando um conjunto vazio

# Podemos adicionar elementos usando o método add()
conjunto_a.add(1)   # O Método add() aceita apenas 1 único parâmetro
conjunto_a.add(2)
print(conjunto_a)

# Um método interessante é o update(), de modo que inserimos uma strig e ela será dividida em cada elemento
conjunto_a.update('teste')
print(conjunto_a)

# Caso você queira mantar uma string inteira para o set, coloque-a em uma tupla e depois use o update.
conjunto_a.update(('Nogueira',))
print(conjunto_a)

# Podemos eliminar um valor usando o método discard() e passando o valor como parâmetro
conjunto_a.discard('Nogueira')
print(conjunto_a)

# Podemos remover todos os elementos de um set com o método clear()
conjunto_a.clear()
print(conjunto_a)
