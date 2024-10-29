# Estruturas de repetição aninhadas

'''
É possível executar um loop dentro de outro loop. Formando assim, uma estrutura de repetição aninhada.
Veja um exemplo simulando uma tabela, formando linhas e colunas:
'''

qtd_linhas = 5 # Declaramos o total de linhas que queremos, semelhante a uma planilha Excel
qtd_colunas = 5 # Aqui o total de colunas
linha = 1 # Este será nosso iterador para percorrer as linhas

while linha <= qtd_linhas: # Aqui começamos o loop de linhas

    coluna = 1 # Este é nosso iterador para percorrer as colunas
    while coluna <= qtd_colunas: # Para cada linha, devo percorrer 5 colunas

        print(f'{linha=}, {coluna=}') # Exibindo as linhas e colunas
        coluna += 1 # Incrementando cada coluna

    linha += 1 # Incrementando cada linha

print('Fim...') # Um print para mostrar quando os dois loops encerraram
