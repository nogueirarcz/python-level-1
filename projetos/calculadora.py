# Calculadora While

# Construção de calculadora simples, com 4 operações básicas.

while True:

    sair = input('Aperte [s] para sair do programa: ').lower().startswith('s')
    
    if sair:

        print('Você encerrou o programa')
        break
    