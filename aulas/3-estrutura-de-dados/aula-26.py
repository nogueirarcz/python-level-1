'''
Introdução ao tipo de dados set (conjuntos)

sets são tipos mutáveis, porém aceitam apenas tipos imutáveis em seus elementos
'''

conjunto_a = set()      # Criando um conjunto vazio
print(conjunto_a)
print(type(conjunto_a))

# Sets são parecidos com dicionários, porém não possuem o par de chave-valor. São apenas os valores

conjunto_b = set('Nogueira')
print(conjunto_b)       # Sets não garantem a ordem dos elementos

# Podemos criar sets de outra maneira, desde que não estejam vazios:
conjunto_c = {'a', 'b', 'c', 'd'} # Semelhante ao dicionário, mas sem usar chaves-valor
print(conjunto_c)

'''
Vamos ver como um set se comporta com elementos repetidos
'''
contunto_d = {1, 2, 3, 3, 3, 4, 4, 1}
print(contunto_d)

