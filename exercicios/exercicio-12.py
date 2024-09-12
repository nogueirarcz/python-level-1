# Validando dígitos de um CPF

cpf = '74682489070'
nove_digitos = cpf[0:9]

contador = 10
multiplicao_digito_contador = 0
soma_das_multiplicacoes = 0

# Validando o primeiro dígito
print('Validando o primeiro dígito')
for digito in nove_digitos:

    print(digito, contador, ' = ', int(digito) * contador)
    multiplicao_digito_contador = int(digito) * contador
    soma_das_multiplicacoes += multiplicao_digito_contador
    contador -= 1

print(f'Soma: {soma_das_multiplicacoes}')
digito_um = ((soma_das_multiplicacoes * 10) % 11)

print(f'Soma * 10 % 11 = {digito_um}')

digito_um = digito_um if digito_um <= 9 else 0
print(f'Primeiro dígito: {digito_um}')

print('\n\n')

# Validando o segundo dígito
print('Validando o segundo dígito')
dez_digitos = nove_digitos + str(digito_um)
contador = 11
multiplicao_digito_contador = 0
soma_das_multiplicacoes = 0

for digito in dez_digitos:

    print(digito, contador, ' = ', int(digito) * contador)
    multiplicao_digito_contador = (int(digito) * contador)
    soma_das_multiplicacoes += multiplicao_digito_contador
    contador -= 1

print(f'Soma: {soma_das_multiplicacoes}')

digito_dois = ((soma_das_multiplicacoes * 10) % 11)
print(f'Segundo dígito: {digito_dois}')
