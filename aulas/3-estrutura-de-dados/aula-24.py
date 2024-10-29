# Utilizando dicionário na prática

# Vamos simular uma agenda telefônica com dicionário
contato = {
    'nome': 'Guilherme',
    'sobrenome': 'Nogueira',
    'telefone': '99 99999-9999',
    'email': 'nogueira@email.com'
}

# Podemos usar a chave para escrever um determinado valor
print(contato['nome'])

# Se tentarmos solicitar o valor de uma chave inexistente, teremos KeyError
# print(contato['profissao']) # A chave profissão não existe no contato

# Podemos apagar o valor relacionado a uma chave
del contato['email']
print(contato)

# Para evitar exceções, podemos usar o método get e caso a chave não exista, retornará None
print(contato.get('sobrenome'))
print(contato.get('email'))
