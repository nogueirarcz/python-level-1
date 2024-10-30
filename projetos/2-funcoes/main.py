import coeficientes as coef
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

        os.system('cls')
        print(resultado_c[1])
        break


# Apresentar a lei de formação
print('\nA lei de formação da função é: ')
print(f'f(x) = {termo_a}x² + ({termo_b}x) + ({termo_c})')
