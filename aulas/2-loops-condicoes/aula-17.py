# Try e Except

'''
Vamos falar sobre exceções em Python. Uma exceção será um desvio que planejaremos, para quando
um determinado bloco de código resultar em algum erro. Como exemplo, quando um usuário informa
um tipo de dados diferente do que estávamos esperando. 
O interpretador do Python irá apresentar algum tipo de erro, com informações específicas para o
desenvolvedor. De modo que, o usuário do programa não compreenderá.
'''

'''
Nesse caso, usaremos o except para criar um bloco de código personalizado, que será executado
somente se o caso de erro no programa acontecer. O bloco try irá tentar executar o programa
padrão, já o bloco except será executado somente quando o bloco try resultar em algum erro.
'''

# Vamos pedir que um usuário informe sua idade e criar uma exceção para o caso de ele informar
# um tipo de dado incoerente.

# Vamos mostrar que idade o usuário teria em 10 anos
# É claro que, se ele informar um tipo de dados diferente de int, essa operação não será possível.

try:

    idade = int(input('Informe sua idade: ')) # Estamos esperando um dado do tipo int
    print(f'Em dez anos você terá {idade + 10} ')

except:

    print('O tipo de dado que você informou não é válido. Tente novamente!')

'''
Imagine que nosso usuário informe uma string, um caractere ou algo assim, teremos um erro do tipo
ValueError. Para que o usuário não recebe o conjunto de mensagens Traceback, iremos personalizar
a mensagem de erro com o bloco except.
'''
