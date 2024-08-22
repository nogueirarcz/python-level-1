# Tipos de dados (bool)

# Dados booleanos podem assumir dois valores: verdadeiro ou falso
# São representados em Python pelos valores True e False, respectivamente

# Normalmente os dados booleanos são possíveis respostas ou retorno de expressões comparativas e
# ou lógicas

valor_um = True
valor_dois = False

print(type(valor_um)) # Verificamos que os booleanos fazem parte da classe bool
print(valor_um)

print(type(valor_dois))
print(valor_dois)

# Expressões lógicas ou comparativas podem retornar valores bool
print(5 > 2) # 5 é maior que dois, portanto retorna True
print(3 == 3) # 3 é igual a 3 e por isso retorna True
print(12 < 8) # 12 não é menor que oito, portanto retorna False
print(bool('')) # Uma string vazia retorna False

'''
Utilizaremos os booleanos para realizar o controle de fluxo do nosso programa, através de estruturas condicionais.
'''