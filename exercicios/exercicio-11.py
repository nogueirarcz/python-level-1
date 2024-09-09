# Curso de Engenharia de Software - Algoritmos e Estruturas de Dados
# Professor Guilherme Nogueira

# Exercício 11

'''
Implemente um programa que permite ao usuário inserir quantos números 
desejar em uma lista e, em seguida, calcule e exiba a soma de todos os números inseridos.
'''
# .---------------------------.
# |         Resolução         |
# '---------------------------'

def soma_lista(numeros):
    soma = 0
    for numero in numeros:
        soma += numero
    return soma

# Criando a lista e recebendo os números do usuário
numeros = []
while True:
    entrada = input("Digite um número para adicionar à lista (ou 'sair' para encerrar): ")
    if entrada.lower() == 'sair':
        break
    try:
        numero = float(entrada)  # Convertendo a entrada para número (float para permitir decimais)
        numeros.append(numero)
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")

# Somando os números da lista
resultado = soma_lista(numeros)

# Exibindo o resultado
print(f"Você inseriu os números: {numeros}")
print(f"A soma dos números é: {resultado}")
