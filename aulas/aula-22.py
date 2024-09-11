# Funções em Python

'''
Uma função é um bloco de código que realiza uma tarefa específica, é um pequeno programa dentro de um
programa maior, um algoritmo que pode ser acionado quando necessário e pode receber parâmetros para
sua execução.
'''

# Para declarar uma função no Python, usamos a palavra chave def e depois o nome da função e por fim ()

def saudacao():

    print('Olá, bom dia!')

# Uma vez declarada, podemos invocar essa função da seguinte maneira:
saudacao()

# Agora vamos utilizar um parâmetro para essa função. Faremos o usuário informar seu nome e
# depois usaremos a função de saldação com o nome do usuário.

nome = input('Informe o seu nome: ')

# Redeclarando a função, agora pedindo que tenha um parâmetro
def saudacao(nome):

    print(f'Olá, {nome}. Bom dia!')

# Agora vamos chamar a função, passando o nome que o usuário digitou como parâmetro
saudacao(nome)

# Uma função também pode ter um retorno, que é algum tipo de dado. Usamos a palavra return para declarar o retorno
def soma():

    return 8 + 7

print(soma())

'''
É necessário analisar o escopo das variáveis que usaremos em funções.
Variáveis criadas dentro de funções, possuem um escopo local e só existem enquanto a função
está sendo executada. Por isso, não podem ser utilizadas fora da função.

Já as variáveis criadas fora de funções, possuem escopo global e podem ser utilizadas a qualquer
momento no programa.
'''

'''
O Python possui diversas funções nativas e já utilizamos várias delas:
print()
len()
int()
input()
Entre outras...
'''
