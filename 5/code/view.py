import tools


def showSurface(fnc=None, start_x=None, end_x=None, n=None):
    if fnc is None:
        fnc = tools.read_user_function()

    if start_x is None:
        start_x = tools.read_user_number('Bitte geben Sie einen Wert ein für `start_x`: ')

    if end_x is None:
        end_x = tools.read_user_number('Bitte geben Sie einen Wert ein für `end_x`: ')

    if n is None:
        n = tools.read_user_number('Bitte geben Sie einen Wert ein für `n`: ')

    print('')
    print('')

    val_trapeze = tools.trapeze(fnc, start_x, end_x, n)
    val_simpson = tools.simpson(fnc, start_x, end_x, n)
    val_diff = abs(val_trapeze - val_simpson)

    print('Flächeninhalt gemäss Trapezregel: ')
    print(val_trapeze)
    print('')

    print('Flächeninhalt gemäss Simpsonsche Regel: ')
    print(val_simpson)
    print('')

    print('Differenz (Approximation) zwischen den beiden Regeln: ')
    print(val_diff)
    print('')


def showTorusVolume(r_lower, r_upper):
    v_simple = tools.volume_torus_simple(r_lower, r_upper)
    v_integral = tools.volume_torus_integral(r_lower, r_upper)
    v_diff = abs(v_simple - v_integral)

    print('')
    print('Berechnetes Volumen für einen Torus mit r=`' + str(r_lower) + '` und R=`' + str(r_upper) + '`: ')
    print('- Einfache Berechnung:          `' + str(v_simple) + '`')
    print('- Integrale Berechnung:         `' + str(v_integral) + '`')
    print('- Differenz (Approximation):    `' + str(v_diff) + '`')
    print('')
    print('')
