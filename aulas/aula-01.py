# Hello Word!

# Módulos Python
'''
    Um módulo Python é um arquivo como este, que possui uma extensão .py e é um conjunto de instruções 
    executáveis (o código Python)
'''

# Função print para exibir strings no terminal
print('Hellow World!')

# Tamém é possível usar a função print para imprimir o conteúdo de variáveis
nome = 'Guilherme'
sobrenome = 'Nogueira'
print(nome, sobrenome)

# Podemos formatar a saída no terminal de diferentes formas:
# Por padrão o print utiliza o espaço como separador entre os elementos.
# Podemos alterar essa configuração através do parâmetro sep
print(nome, sobrenome, sep='-')

# Outro parâmetro que podemos configurar é o end, que altera o comportamento da função print
# que quebra a linha ao fim do comando (essa ação tem como padrão end=\n)
# Vamos alterar o valor de end
print(nome, sobrenome, end=';')
