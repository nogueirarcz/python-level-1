# Métodos Úteis em dicionários

contato = {
    'nome': 'Guilherme',
    'sobrenome': 'Nogueira',
    'telefone': '99 99999-9999',
    'email': 'nogueira@email.com'
}

# Podemos utilizar a função len() para contar o número de chaves de um dicionário
print(len(contato))

# Para conferir as chaves que existem, usamos o método keys()
print(contato.keys())

# Caso seja preciso conferir apenas os valores, usamos o método values()
print(contato.values())

# Usamos setdefault para determinar o valor padrão para uma chave
contato.setdefault('idade', None)
print(contato)

# Com o método popitem() iremos eliminar a última chave do dicionário
contato.popitem()
print(contato)

# Com o método update() podemos alterar os itens
contato.update({'email': 'guilherme@email.com'})
print(contato)
