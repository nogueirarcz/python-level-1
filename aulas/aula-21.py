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

# Acessar o valor por uma chave pode retornar um erro, caso a chave não exista.
# Para evitar esse erro, podemos usar o método get, passando dois parâmetros.
# O primeiro é a chave e o segundo é uma mensagem de erro, caso a chave não exista
print(lista_telefonica.get('Fabi', 'Esta chave não existe'))
print(lista_telefonica.get('Ana', 'Esta chave não existe'))

# Adicionar um novo item também é bem simples. Basta informar um novo par de chave-valor
lista_telefonica['Fabi'] = '44 44444-4444'
print(lista_telefonica)
# Para remover, basta utilizar o método pop e passar a chave

# Podemos imprimir apenas as chaves
print(lista_telefonica.keys())

# Podemos imprimir apenas os valores
print(lista_telefonica.values())
