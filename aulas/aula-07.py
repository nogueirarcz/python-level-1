# Operadores aritméticos

# É possível realizar operações aritméticas e utilizar o Python como uma espécie de calculadora.

print(5 + 3) # Soma

print(5 - 3) # Subtração

print(5 * 3) # Multiplicação

print(5 / 3) # Divisão

print(5 // 3) # Divisão inteira

print(5 % 3) # Resto da divisão

print(5 ** 3) # Potenciação

'''
É importante considerar a ordem de precedência entre os operadores, de modo semelhante ao que se faz na matemática.

Em Python a ordem de precedência é a seguinte:
()              --> parênteses                      (a partir do centro)
**              --> exponenciação                   (da esquerda para a direita)
* e /           --> multiplicação e divisão         (da esquerda para a direita)
+ e -           --> adição e subtração              (da esquerda para a direita)
'''

# Exemplo
print(5**2 + ((3+2) + 1 / 2 * 5))   # primeiro o parênteses no centro (3+2) = 5
                                    # depois dentro do parênteses da direita
                                    # 1/2 = 0.5
                                    # depois a multiplicação 0.5 * 5 = 2,5
                                    # depois o que sobrou no parênteses 5 + 2,5 = 7,5
                                    # depois a operação 5**2 = 25
                                    # por fim a soma de 25 + 7,5 = 32,5
  