# introdução a funções lambda

'''
lambda são funções anônimas, que são declaradas e executadas simultaneamente e, por isso, não precisam ser nomeadas
'''

# Observe esse caso de uma função para calcular 25% de um determinado valor:
def calcular_percentual(valor):

    return valor * 0.25

print(calcular_percentual(100))
print(calcular_percentual(50))

# Nesse caso eu precisei declarar a função de calcular o percentual e depois executá-la.

# Com a função lambda, fazemos tudo ao mesmo tempo. Observe

# Primeiro vamos criar uma lista com os valores que queremos calcular o percentual
valores = [100, 50, 25, 10, 5]

# Agora uma lista para receber os percentuais calculados
# Vamos usar a função map() que serve para executar uma outra função para cada intem de uma lista, nesse caso, nossa função lambda
percentuais = list(map(lambda x : x * 0.25, valores))

print(percentuais)
