# Empacotamento e desempacotamento

'''
Imagine que temos uma lista de nomes de convidados... Podemos considerar essa lista como um pacote, onde cada
nome é um item que está empacotado. Podemos desempacotar os nomes da lista, realocando cada nome para uma variável.
Observe:
'''

lista_de_convidados = ['Thiago', 'Silvana', 'Katarina', 'Evandro']
convidado1, convidado2, convidado3, convidado4 = lista_de_convidados

# Desse modo, cada convidado foi adicionado à variável correspondente ao seu índice, na ordem em que foram declaradas.

print(convidado1)
print(convidado4)

# Mas o que será que acontece se eu não tiver variáveis suficientes para alocar todos os valores empacotados na lista?
item1, item2 = ['Notebook', 'Tablet', 'Smartphone', 'Smartwatch'] # Comente essa linha para avançar no código

# Neste caso o Python irá apresentar um ValueError: too many values to unpack
# Ou sejá, há mais valores no pacote do que espaço para desempacotá-los.

# Caso a situação seja de um número maior de variáveis para alocar os itens do pacote e um número menor de itens no pacote,
# teremos um novo erro: ValueError: not enough values to unpack. Seria este caso:
item1, item2, item3, item4 = ['Notebook', 'Tablet'] # Comente essa linha para avançar no código

'''
No caso de mais valores a serem desempacotados do que variáveis disponíveis, podemos desempacotar apenas o valor que queremos
e reempacotar o restante em uma nova variável:
'''
convidado1, *demais_convidados = ['Thiago', 'Silvana', 'Katarina', 'Evandro']
print(convidado1)
print(demais_convidados)
