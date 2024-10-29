# Estruturas de repetição
# Loop for

'''
O loop for é uma excelente estratégia para iterar listas, fazer contagens e muito mais.
Vamos iterar uma lista para que você entenda melhor.
'''

lista_de_carros = ['Gol', 'Siena', 'Uno', 'Jetta', 'Amarok', 'Corolla'] # Criando nossa lista de carros

for elemento in lista_de_carros: # Para cada elemento que está na lista de carros

    print(elemento) # O programa deve escrever o conteúdo do elemento

print('O primeiro loop for acabou\n\n') # Após escrever todos os elementos, nosso loop se encerra

'''
Veja a mesma lógica aplicada a contagem numérica:
'''

for numero in range(10): # para cada número até 10 (lembrando que a contagem começa em 0)

    print(numero) # Escreva o número - Desse modo a incrementação é automática, pois ustilizamos a função range()

print('O segundo loop acabou\n\n')

'''
Como strings em Python são listas de caracteres, também podemos iterá-las com for:
'''

for letra in 'Nogueira':        # Para cada letra em Nogueira, o programa irá escrever a letra

    print(letra)

print('\nO terceiro loop for acabou')
