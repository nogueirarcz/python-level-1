# Estruturas Condicionais

'''
Estas estruturas são essenciais para controloar o fluxo de execução de um programa.
Estão relacionadas a expressões aritméticas e ou lógicas.
Servem para condicionar a execução de um determinado bloco de código

Podemos dizer que servem para que o programa tome uma decisão, conforme a seguinte senteça:
Se uma determinada condição for verdadeira, execute um código.
Se esta condição não for verdadeira, execute outro código ou nenhum código.

É possível criar várias condições para serem avaliadas uma a uma, de modo que o programa tome uma decisão com base nas condições.
'''

# Exemplo:
idade_do_usuario = int(input('Informe a sua idade: '))

# Agora que sabemos a idade do usuário, vamos verificar se ele tem 18 anos ou mais e informar se é 'maior de idade' ou 'menor de idade'
#Se a idade do usuário for maior ou igual (esta é nossa condição)
if (idade_do_usuario >= 18): 

    print('Você é maior de idade.')

else: 

    print('Você é menor de idade.')

# Veja que neste caso, se a idade não for maior ou igual dezoito, o bloco a ser executado sera o else.

# Observe também o uso da identação para determinar que o código só será executado caso atenda à condição.

# Caso tenhamos mais de duas possibilidades, devemos usar o elif. Observe:

opcao_do_usuario = int(input('Escolha uma opção entre 1 e 4: '))

if opcao_do_usuario == 1:

    print('Você escolheu a opção um.')

elif opcao_do_usuario == 2:

    print('Você escolheu a opção dois.')

elif opcao_do_usuario == 3:

    print('Você escolheu a opção três.')

elif opcao_do_usuario == 4:

    print('Você escolheu a opção quatro.')

else:

    print('Você escolheu uma opção inválida.') # Observe que este bloco será executado se nenhuma das outras alternativas for True
