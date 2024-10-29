aniversarios = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:

    print('Informe o nome [ou deixe em branco para sair]')

    nome = input()

    if nome == '':

        print('Programa encerrado!')
        break

    if nome in aniversarios:

        print(aniversarios[nome] + ' é o aniversário de ' + nome)

    else:

        print('Não temos a informação do aniversário de ' + nome)
        
        aniversario = input('Informe o aniversário: ')
        aniversarios[nome] = aniversario

        print('Base de dados atualizada!')
