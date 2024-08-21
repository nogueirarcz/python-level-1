# Coerção de dados
# É possível converter um dado de um tipo em outro tipo, através de uma função

numero_inteiro = 10
numero_decimal = 8.8

print(type(numero_inteiro)) # Aqui podemos conferir que trata-se de um número inteiro
print(numero_inteiro)

numero_inteiro = float(numero_inteiro) # Aqui iremos conerter para float (decimal)
print(type(numero_inteiro))
print(numero_inteiro)

# Agora faremos o mesmo processo para converter o número decimal para inteiro
print(type(numero_decimal))
print(numero_decimal)

numero_decimal = int(numero_decimal) # Aqui faremos a conversão com a função int()

# Vamos conferir
print(type(numero_decimal))
print(numero_decimal)
