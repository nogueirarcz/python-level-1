'''
Excreva um programa que exita a sequência de Collatz
'''

terminou = False
valor_inicial = int(input('Informe um valor para iniciar a sequência de Collatz: '))

print(valor_inicial)

while not terminou:

    if valor_inicial % 2 == 0:

        valor_inicial = (valor_inicial // 2)
        print(valor_inicial)
        
    else:

        valor_inicial = (valor_inicial * 3 + 1)
        print(valor_inicial)

    if valor_inicial == 1:

        terminou = True
