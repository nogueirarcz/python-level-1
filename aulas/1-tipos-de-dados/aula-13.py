# Formatação de strings com f-strings

nome = input('Digite seu nome: ')
saudacao = 'Bem-vindo!'

'''
A formatação de strings com f-strings nos permite formatar e personalizar a saída de strings de diversas
maneiras e cria um grande número de possibilidades para se trabalhar strings.
'''

'''
Podemos inserir e manipular variáveis dentro de strings, de modo que ao invés de exibir a string
com o nome da variável, iremos exibir o valor dessa variável.
'''

# Veja um exemplo:
print('\n\n' + f'{saudacao: ^60}')      # Essa técnica se chama padding
print('.' + '-'*60 + '.')               # Uma ideia semelhante ao padding de CSS
print('|' + f'{nome: ^60}' + '|')       # Mas nesse caso, aplicada à saídas no terminal
print('\'' + '-'*60 + '\'')             # Útil para personalizar saídas e fazer desenhos no terminal

''' 
Uma outra situação muito comum, é a formatação de casas decimais.
Normalmente queremos mostrar apenas 2 casas decimais, porém operações matemáticas
podem gerar números com muitas casas...
'''
numero_decimal = 12.309859303848
print(f'{numero_decimal:.2f}')      # desse modo podemos determinar com 2f para duas casas decimais
print(f'{numero_decimal:.5f}')      # desse modo podemos determinar com 5f para cinco casas decimais

'''
É possível realizar muitos outros tipos de formatações com f-strings, sugiro que pesquise mais sobre isso.
'''
