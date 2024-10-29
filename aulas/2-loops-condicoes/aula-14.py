# Estruturas de Repetição - While

# while é equivalente ao enquanto (no portugol - visualg)

'''
Uma estrutura de repetição em Python é um recurso para desenvolver tarefas repetitivas em um loop contínuo. 
O loop funciona até uma condição ser satisfeita.
'''

'''
Vamos criar um programa que conte até 10. Poderiamos usar dez vezes a função print, mas isso seria muito trabalho, imagine contar até 100...
Para reduzir o trabalho, usaremos o loop while. Criaremos uma variável chamada contador e faremos ela aumentar de 1 em 1 até chegar em 10.
'''

contador = 1

while contador <= 10:   # Nosso loop ira se repetir enquanto o contador for menor ou igual a dez

    print(contador)     # Vamos escrever o valor do contador, que na primeira iteração do loop é 1

    contador += 1       # Agora vamos incrementar o valor em 1

print('Nosso loop while encerrou.\n\n') # Aqui deixaremos um print para marcar o momento em que o loop finalizou sua operação.

'''
Vamos construir um novo loop, agora trabalhando com alguma condição booleana.
Pediremos que o usuário informe o seu nome e, se ele não digitar nada, o programa irá repetir o processo.
Mas, se o usuário informar o nome, iremos interromper o loop e finalizar o programa.
'''

nome = ''       # Primeiro definimos uma variável chamada nome e atribuímos a ela uma string vazia, que em bool vale False

while not nome: # Enquanto o valor bool dessa variável for False, o loop se repetirá, por isso usamos o operador not

    nome = input('Informe o seu nome: ') # Capturamos o nome do usuário

    if not nome: # Verificamos se o valor bool da variável é False (será false se o usuário não digitar nada)

        print('Você não informou o seu nome. Tente novamente.') # No caso de não digitar nada, exibe esta mensagem

    else: # Caso o usuário digite algo, a variável assume em bool um valor True

        break # O comando break interrompe o fluxo do loop
    
print(f'Seu nome é {nome}') # Neste momento, já estamos fora do loop. E aí sim, exibimos o nome digitado pelo usuário.

'''
OBSERVE QUE: Se o usuário nunca digitar algo, o loop continuará se repetindo infinitas vezes. Isso é o que chamamos de LOOP INFINITO
Tenha muito cuidado ao programar loops, pois um loop infinito pode comprometer seu programa e iniciar um consumo exagerado de recursos.
'''
