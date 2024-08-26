# Curso de Engenharia de Software - Algoritmos e Estruturas de Dados
# Professor Guilherme Nogueira

# Exercício 02

'''
Peça ao usuário para digitar seu nome.
Peça ao usuário para digitar sua idade.

Se nome e idade forem digitados, faça exibir:

    Seu nome é {str}
    Sua idade é {int}
    Seu nome invertido é {str}
    Seu nome contém ou não espaços {bool}
    seu nome tem {int} letras
    A primeira letra do seu nome é {str}
    A última letra do seu nome é {str}

Se nada for digitado, faça exibir:

    "Para executar corretamente o programa, você deve digitar as informações. Tente novamente."
'''

# .---------------------------.
# |         Resolução         |
# '---------------------------'

nome = input('Digite o seu nome: ')
idade = int(input('Digite sua idade: '))

if nome and idade:

    print(f'Seu nome é : {nome}')
    print(f'Sua idade é {idade}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        espacos = True
    
    else:
        espacos = False

    print(f'Seu nome contem espaços: {espacos}')
    print(f'Seu nome tem {len(nome)} letras.')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
