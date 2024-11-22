import coeficientes as coef
import formulas as form
import grafico as graf
import os

# Loop para validar o coeficiente a
while True:

    termo_a = input('Informe o termo a: ')
    resultado_a = coef.validar_coeficiente_a(termo_a)
    
    # Caso a não seja um valor numérico
    if resultado_a[0] == 1:

        os.system('cls')
        print(resultado_a[1])
        continue

    # Caso a seja zero
    elif resultado_a[0] == 2:

        os.system('cls')
        print(resultado_a[1])
        continue
    
    # Caso esteja tudo certo
    else:

        termo_a = float(termo_a)
        os.system('cls')
        print(resultado_a[1])
        break

# Loop para validar o coeficiente b
while True:

    termo_b = input('Digite o termo b: ')
    resultado_b = coef.validar_coeficiente_b_e_c(termo_b)

    # Caso b não seja um número
    if resultado_b[0] == 1:

        os.system('cls')
        print(resultado_b[1])
        continue

    # Caso esteja tudo certo
    else:

        termo_b = float(termo_b)
        os.system('cls')
        print(resultado_b[1])
        break

# Loop para validar o coeficiente C
while True:

    termo_c = input('Informe o termo c: ')
    resultado_c = coef.validar_coeficiente_b_e_c(termo_c)

    # Caso c não seja um número
    if resultado_c[0] == 1:

        os.system('cls')
        print(resultado_c[1])
        continue

    # Caso esteja tudo certo
    else:

        termo_c = float(termo_c)
        os.system('cls')
        print(resultado_c[1])
        break

# Apresentar a lei de formação
print('\nA lei de formação da função é: ')
print(f'f(x) = {termo_a}x² + ({termo_b}x) + ({termo_c})')

# Apresentar o Delta
print('')
delta = form.delta(termo_a, termo_b, termo_c)
print(f'O Delta da função é {delta[0]}')
print(f'{delta[1]}')

# Apresenta a primeira raiz
if delta[0] >= 0:

    x1 = form.primeira_raiz(termo_a, termo_b, delta[0])

    print(f'A primeira raiz da função é {x1}')

# Apresenta a segunda raiz
if delta[0] > 0:

    x2 = form.segunda_raiz(termo_a, termo_b, delta[0])

    print(f'A segunda raiz da função é {x2}')

# Não há raízes
if delta[0] < 0:

    print('Esta função não possui raizes.')

# Apresenta o ponto máximo ou mínimo
xv = form.vertice_x(termo_a, termo_b)
yv = form.vertice_y(termo_a, delta)

if termo_a < 0:

    print(f'O ponto mínimo da função é ({xv}  , {yv})')

else:

    print(f'O ponto máximo da função é ({xv}  , {yv})')


# Gerar gráfico
while True:

    resposta = input('\nDeseja gerar o gráfico da função? [s/n]')

    if resposta == 'n':

        print('\nPrograma encerrado.')
        break

    if resposta == 's':

        valores_x_y = graf.gerar_valores(termo_a, termo_b, termo_c)

        graf.gerar_grafico(valores_x_y[0], valores_x_y[1])
