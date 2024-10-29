def validar_coeficiente_a(coeficiente_a):
    
    # 0 se tudo correto
    # 1 para ValueError
    # 2 para a == 0

    try:

        coeficiente_a = (float(coeficiente_a))

    except ValueError as error:

        msg = 'Certifique-se de informar um valor numérico \n Tente novamente.'
        return 1, msg
    
    if coeficiente_a == 0:

        msg = 'O Termo A deve ser diferente de zero. \n Tente novamente.'
        return 2, msg
    
    msg = 'Tudo certo, vamos para o próximo.'
    return 0, msg
    
def validar_coeficiente_b_e_c(coeficiente_b_e_c):

    try:

        coeficiente_b = float(coeficiente_b_e_c)

    except ValueError as error:

        msg = 'Certifique-se de informar um valor numérico \n Tente novamente.'
        return 1, msg
    
    msg = 'Tudo certo, vamos continuar'
    return 0, msg
