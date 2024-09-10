# Dicionários - São uma estrutura de dados fundamental em Python, usada para armazenar pares de chave-valor.
# Diferente das listas e das tuplas que têm seus valores organizados por índices, os dicionários
# possuem chaves para organizar seus valores. Cada valor possui uma chave correspondente.

# Veja um exemplo de dicionário utilizado como lista telefônica, em que temos o modelo
# contato: número

lista_telefonica = {
    'Ana': '99 99999-9999',
    'Bia': '88 88888-8888',
    'Carla': '77 77777-7777',
    'Duda': '66 66666-6666'
}

# Veja como a função print se comporta ao escrever um dicionário:
print(lista_telefonica)
print()

# Assim como as outras estruturas de dados estudadas até aqui, os dicionários possuem seus métodos
print(lista_telefonica.items()) # Esse método traz os items do dicionário organizados em uma lista

# O método pop remove e retorna um elemento associado a uma chave
lista_telefonica.pop('Carla')
print(lista_telefonica)

# Para atualizar o valor de alguma chave, basta determinar um novo valor a ela
lista_telefonica['Duda'] = '55 55555-5555'
print(lista_telefonica)