# Mapeando dados com list comprehension

produtos = [
    {'nome': 'p1', 'preco': 20,},
    {'nome': 'p2', 'preco': 10,},
    {'nome': 'p3', 'preco': 30,},
]

# Vamos mapear a lista de produtos para uma nova lista
novos_produtos = [
    # Vamos desempacotar os dicionários para operar com seus valores dentro do for
    {**produto, 'preco': produto['preco'] * 1.05} # Aumentando o preço em 5% (se o preço for maior que 20)
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

# Vamos verificar o resultado
print(novos_produtos)
print()

# Agora desempacotar a lista e quebrar uma linha a cada produto
print(*novos_produtos, sep='\n')
