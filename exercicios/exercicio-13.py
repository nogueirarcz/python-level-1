# Faça um jogo de perguntas e respostas utilizando dicionários

perguntas = [
    {
        'pergunta': 'Quanto é 10 por cento de uma hora em minutos?',
        'opções': ['10', '6', '12', '1'],
        'resposta': '6',
    },

    {
        'pergunta': 'Quanto é 5 * 5?',
        'opções': ['10', '15', '5', '25'],
        'resposta': '25',
    },

    {
        'pergunta': 'Quanto é raiz quadrada de 81?',
        'opções': ['3', '9', '7', '11'],
        'resposta': '9',
    },
]

acertos = 0

for pergunta in perguntas:

    print(pergunta['pergunta'], '\n')

    for opcao in pergunta['opções']:

        print(f'{opcao}')

    resposta = (input('Informe o resposta: '))
    if resposta == pergunta['resposta']:

        print('Você acertou!')
        acertos += 1

    else: 
        print('Você errou!')

print(f'Seu total de acertos foi {acertos}')
