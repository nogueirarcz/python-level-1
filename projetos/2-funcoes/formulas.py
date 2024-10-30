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
