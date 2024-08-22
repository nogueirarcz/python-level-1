# Curso de Engenharia de Software - Algoritmos e Estruturas de Dados
# Professor Guilherme Nogueira

# Exercício 01

'''
Desenvolva um algoritmo que pergunte o nome, idade, peso (em kg) e altura (em m) de uma pessoa.
Este algoritmo deve utilizar essas informações para calcular o IMC (Índice de Massa Corpórea) desta pessoa.
Depois, faça o algoritmo apresentar no terminal o IMC da pessoa de acordo com sua categoria.

Atente-se para as seguintes categorias (medidas em kg/m²):

IMC < 18, 5                   -->         baixo peso;
IMC >= 18,5 e <= 24,9         -->         peso adequado;
IMC >= 25 e <= 29,9           -->         sobrepeso;
IMC >= 30 e <=34,9            -->         obesidade grau 1;
IMC >= 35 e <= 39,9           -->         obesidade grau 2;
IMC >= 40                     -->         obesidade extrema
'''

# .---------------------------.
# |         Resolução         |
# '---------------------------'

nome_do_usuario = input('Informe o seu nome: ')

# Não está no escopo deste exercício o tratamento de erros. Portanto, consideraremos que o usuário informará corretamente os dados.

print(f'Olá, {nome_do_usuario}. Vamos calcular o seu IMC.')

peso_do_usuario = float(input(f'\n{nome_do_usuario}, por favor, informe o seu peso em kg: '))

altura_do_usuario = float(input('\nMuito bem! Por fim, informe a sua altura em metros: '))

# Agora vamos calcular o IMC = (peso / altura ** 2) 
imc_do_usuario = (peso_do_usuario / (altura_do_usuario ** 2))

# Em seguida, é necessário categoriar o IMC obtido
categoria_do_imc = ... # Utilizaremos ellipses para não atribuir nenhum valor à categoria ainda.

if (imc_do_usuario < 18.5):                                     # Caso 1

    categoria_do_imc = 'baixo peso'

elif (imc_do_usuario >= 18.5 and imc_do_usuario <= 24.9):       # Caso 2

    categoria_do_imc = 'peso adequado'

elif (imc_do_usuario >= 25 and imc_do_usuario <= 29.9):         # Caso 3

    categoria_do_imc = 'sobrepeso'

elif (imc_do_usuario >= 30 and imc_do_usuario <= 34.9):         # Caso 4

    categoria_do_imc = 'obesidade grau I'

elif (imc_do_usuario >= 35 and imc_do_usuario <= 39.9):         # Caso 5

    categoria_do_imc = 'obesidade grau II'

else:                                                           # Caso 6

    categoria_do_imc = 'obesidade extrema'

# É hora de apresentar o resultado para o usuário
print(f'\n\nExcelente, {nome_do_usuario}.')
print(f'Verificamos suas informações e identificamos que seu IMC é {imc_do_usuario:.2f} kg/m²') 
print(f'Este Índice de Massa Corpórea te caracteriza como categoria de {categoria_do_imc}.')
