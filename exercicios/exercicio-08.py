# Curso de Engenharia de Software - Algoritmos e Estruturas de Dados
# Professor Guilherme Nogueira

# Exercício 08

'''
Faça uma lista de compras. Dê ao usuário a opção de vizualizar os itens,
inserir e remover itens
'''
# .---------------------------.
# |         Resolução         |
# '---------------------------'

import os

lista_de_compras = []

while True:

    print('Escolha uma opção: ')
    opcao = input('[i]nserir - [a]pagar - [l]istar - [s]air: ')

    if opcao == 'i':

        os.system('cls')
        novo_item = input('Informe o item a ser inserido: ')
        lista_de_compras.append(novo_item)

    elif opcao == 'a':

        indice_do_item = input('Digite o índice para apagar: ')

        try:

            indice_do_item = int(indice_do_item)
            del lista_de_compras[indice_do_item]

        except TypeError:

            print('Essa operação aceita apenas números inteiros! Tente novamente')

        except ValueError:
            
            print('O índice informado não existe na lista. Tente novamente')

        except Exception:

            print('Operação desconhecida.')

    elif opcao == 'l':

        os.system('cls')
        
        if len(lista_de_compras) == 0:

            print('Não há itens na lista.')

        for indice, item in enumerate(lista_de_compras):

            print(indice, item)

    elif opcao == 's':

        os.system('cls')
        print('Programa encerrado.')
        break

    else:

        os.system('cls')
        print('Opção inválida! Tente novamente')
