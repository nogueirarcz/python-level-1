# Tipos de dados - Strings (str)

# No Python existe uma classe própria para strings, que são um tipo de dados
# Trata-se e uma cadeia de caracteres

minha_variavel = 'Qualquer texto entre aspas será reconhecido como uma string'

print(minha_variavel)

# Utilizamos a função type() para verificar o tipo de dados de uma determinada variável
print(type(minha_variavel))

# A função print é utilizada para imprimir um texto no terminal
print('A função print recebe como argumento uma variável ou uma string')

# Além disso, a string se comporta como um array de caracteres e pode ser manipulada através de seus índices.
# Como em qualquer outra linguagem, em Python os índices começam em 0

# Imprimindo índice específico:
print(minha_variavel[0])

# Imprimindo um intervalo da string:
print(minha_variavel[0: 10])

# Podemos usar a função len() para contar quantos elementos uma determinada string possui:
print(len(minha_variavel))

# Com a função upper() colocamos todos os caracteres em letra maíuscula:
print(minha_variavel.upper())

# Com a função lower() colocamos todos os caracteres em letra minúscula:
print(minha_variavel.lower())

# Com a função captalize() colocamos apenas o primeiro caractere em maíusculo:
print('exemplo'.capitalize())

# A função casefold() também pode ser usada para colocar todos os caracteres em minúsculo:
print('TESTE'.casefold())

# Com a função count() podemos verificar o número de vezes que um determinado caractere aparece na string:
print('Guilherme Nogueira'.count('e'))

# Podemos substituir uma parte do texto por outro texto com a função replace():
print('Guilherme Nogueira'.replace('Guilherme', 'Professor')) # 1 - texto a ser substituído; 2 - novo texto

# Com a função split podemos 'cortar' a string em pedaços de acordo com algum separador (por padrão é o espaço)
print('Guilherme Nogueira'.split())

# Com a função splitlines podemos 'cortar' uma string que possui várias linhas, dividindo-a em novas strings (cada linha)
texto = '''
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
'''

print(texto.splitlines())

# Podemos verificar se uma string começa com um determinado caractere, para isso usamos startwith()
print('Python'.startswith('P')) # Retorna um bool (True ou False)

# Para colocar a primeira letra de cada palavra em maiúsculo, usamos title():
print('engenharia de software'.title())

'''
 Será muito comum em nossos programas, realizar tratamento de strings, como formatação de nomes, números, códigos, entre outros...
 Ainda há muitos outros detalhes que podemos considerar sobre as strings, estudaremos mais sobre isso no futuro.
'''