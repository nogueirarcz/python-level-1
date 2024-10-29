# Operadores lógicos

'''
Estes operadores são utilizados para transpor um raciocínio lógico para o código.
Se comportam como uma operação comparativa e possuem como resposta um valor bool
'''

print(3 == 3) # Verifica se um valor é igual a outro

print(2 != 2) # Verifica se um valor é diferente do outro

print(2 > 3) # Verifica se um valor é maior que outro

print(2 >= 3) # Verifica se um valor é maior ou igual a outro

print(2 < 3) # Verifica se um valor é menor que outro

print(2 <= 3) # Verifica se um valor é menor ou igual a outro

# também podemos utilizar estes operadores entre variáveis e strings
print('Python' == 'python') # Retorna False pois Python é case sensitive

valor_um = 10
valor_dois = 15

print(valor_um <= valor_dois) # Retorna False pois foi atribuído à variável valor_um o número 10, que é menor que 15 (valor_dois)
