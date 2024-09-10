# Estruturas de dados
# Tuplas - listas imutáveis

'''
As tuplas são semelhantes às listas, porém são imutáveis, ou seja, não poderão
ser alteradas depois de criadas.
'''

'''
Podemos declarar uma tupla de diferentes formas, por exemplo:
'''

tupla_um = 'Azul', 'Amarelo', 'Vermelho'        # repare que não usamos colchetes, nem chaves ou parênteses
print(type(tupla_um))
print(tupla_um)

# Outra forma de declarar uma tupla é usar os parênteses
tupla_dois = ('Quadrado', 'Triângulo', 'Retângulo')
print(type(tupla_dois))
print(tupla_dois)

# É possível fazer type casting de listas para tuplas e de tuplas para listas
lista_um = list(tupla_um)
print(type(lista_um))
print(lista_um)

tupla_um = tuple(lista_um)
print(type(tupla_um))
print(lista_um)

# Podemos acessar um item específico de uma tupla usando o índice
print(tupla_um[1])
print(tupla_um[2])

'''
Como não podemos alterar a tupla, métodos como append e remove não estão disponíveis.
'''

# Mas podemos usar o método index para encontrar o índice de um elemento
print(tupla_um.index('Vermelho'))

# Ou o método count para verificar quantas vezes um elemento aparece na tupla
print(tupla_um.count('Vermelho'))
