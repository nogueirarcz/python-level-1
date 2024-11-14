def delta(a, b, c):

    delta = (b ** 2) - 4 * a * c

    
    # Análise do delta
    if delta < 0:

        print('')
        msg = ('Delta é maior que zero e, portanto, não há raízes nesta função.\n')

    elif delta == 0:

        print('')
        msg = ('Delta é igual a zero e, portanto, há uma única raíz nesta função.\n')

    else:

        print('')
        msg = ('Delta é maior que zero e, portanto, há duas raízes nesta função\n')


    return delta, msg

def primeira_raiz(a, b, delta):

    x1 = ((b * -1) + (delta ** (1/2))) / (2 * a)
    
    return x1

def segunda_raiz(a, b, delta):

    x2 = ((b * -1) - (delta ** (1/2))) / (2 * a)

    return x2


