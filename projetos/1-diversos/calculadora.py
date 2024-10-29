# Calculadora While

# Construção de calculadora simples, com 4 operações básicas.

while True:

    numero_1 = input('Digite o primeiro número: ')
    numero_2 = input('Digite o segundo número: ')
    operador = input('Digite o operador (+ - / *): ')
    numeros_validos = None
    numero_1_float = 0
    numero_2_float = 0

    try:

        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numeros_validos = True

    except:

        numeros_validos = None
    
    if numeros_validos is None:

        print('Você informou valores inválidos.')
        continue
    
    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:

        print('Você informou um operador inválido.')
        continue

    if len(operador > 1):

        print('Você deve informar apenas 1 único operador.')
        continue

    print('Realizando a operação:')

    if operador == '+':

        print(f'{numero_1_float} + {numero_2_float} = {numero_1_float + numero_2_float}')

    if operador == '-':

        print(f'{numero_1_float} - {numero_2_float} = {numero_1_float - numero_2_float}')
        
    if operador == '*':

        print(f'{numero_1_float} * {numero_2_float} = {numero_1_float * numero_2_float}')
        
    if operador == '/':

        print(f'{numero_1_float} / {numero_2_float} = {numero_1_float / numero_2_float}')
        
    sair = input('Aperte [s] para sair do programa: ').lower().startswith('s')
    
    if sair:

        print('Você encerrou o programa')
        break
    