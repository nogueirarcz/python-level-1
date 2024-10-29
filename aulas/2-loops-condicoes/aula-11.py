# Operadores Lógicos AND e OR

'''
Ainda sobre operações lógicas, podemos encontrar situações com mais de uma condição verdadeira ou
ter na necessidade de avaliar entre muitas opções, uma única verdadeira. Ou, ainda, inverter o resultado lógico de uma expressão.
'''

# No caso do AND, podemos utilizar para validar 2 condições como verdadeiras

# Vamos coletar a idade e o sexo de um usuário e determinar se ele está apto a se aposentar.
# Consideraremos a idade de 60 anos para homens e 55 para mulheres (apenas como situação exemplo).

idade = int(input('Informe a sua idade: '))

sexo = input('Informe o seu sexo [m] ou [f]: ')

# Vamos ignorar o tratamento de erros e considerar que o usuário inseriu corretamente as informações, conforme esperado.

# Agora, verificaremos ambas as condições, observe:
if (idade >= 60 and sexo == 'm'):

    print('Você é homem e possui 60 anos ou mais, portanto, pode se aposentar.')

elif (idade >= 55 and sexo == 'f'):

    print('Você é mulher e possui 55 anos ou mais, portanto, pode se aposentar.')

else:

    print('As condições não satisfazem nenhum caso para aposentadoria.')


# Veja o que aconteceria caso trocassemos o operador and por or
# Nessa situação, o programa entederá que para aposentar basta ter ou 60 ou + anos de idade OU ser do sexo masculino
# Neste caso, trata-se de um erro de lógica, uma vez que para a aposentadoria, ambas as condições devem ser verdadeiras
# Portanto, ao utilizar o and validaremos ambas as opções como True
# Ao utilizar o or, validaremos apenas uma condição como True

if (idade >= 60 or sexo == 'm'):

    print('Você é homem e possui 60 anos ou mais, portanto, pode se aposentar.')

    # Para que este bloco execute, a idade deverá estar entre 55 e 59 ou o sexo ser diferente de m
elif (idade >= 55 or sexo == 'f'):

    print('Você é mulher e possui 55 anos ou mais, portanto, pode se aposentar.')

else:

    print('As condições não satisfazem nenhum caso para aposentadoria.')