# A função input()

'''
Para coletar dados inseridos pelo usuário do programa através do teclado, utilizamos a função input().
Basta atribuir a uma variável o valor obtido através dessa função. Observe:
'''

minha_variavel = input('Digite alguma coisa: ')

# É importante observar que a informação obtida através da função input será sempre uma string (str)
print(type(minha_variavel))

# Caso você queria capturar números inteiros ou decimais, terá que realizar uma conversão de tipo de dados:
minha_variavel = int(input('Digite um número inteiro: '))
print(type(minha_variavel))

minha_variavel = float(input('Digite um número decimal: '))
print(type(minha_variavel))

'''
Caso você queira capturar uma senha, será importante ocultar a senha enquanto digita. 
Para isso importaremos a biblioteca getpass
'''

from getpass import getpass

senha_do_usuario = getpass('Digite sua senha: ')

# A função input() é amplamente utilizada em programas executados no terminal.
