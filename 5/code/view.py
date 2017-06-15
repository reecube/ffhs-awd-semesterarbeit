import tools
import sympy


def showSurface(fnc=None, start_x=None, end_x=None, n=None):
    # Frage den Benutzer falls die Variable nicht bereits definiert wurde
    if fnc is None:
        fnc = tools.read_user_function()

    # Frage den Benutzer falls die Variable nicht bereits definiert wurde
    if start_x is None:
        start_x = tools.read_user_number('Bitte geben Sie einen Wert ein für `start_x`: ')

    # Frage den Benutzer falls die Variable nicht bereits definiert wurde
    if end_x is None:
        end_x = tools.read_user_number('Bitte geben Sie einen Wert ein für `end_x`: ')

    # Frage den Benutzer falls die Variable nicht bereits definiert wurde
    if n is None:
        n = tools.read_user_number('Bitte geben Sie einen Wert ein für `n`: ')

    print('')
    print('')

    # Berechne die Flächen
    val_trapeze = tools.trapeze(fnc, start_x, end_x, n)
    val_simpson = tools.simpson(fnc, start_x, end_x, n)
    val_diff = abs(val_trapeze - val_simpson)

    # Zeige die Flächen an
    print('')
    print('Berechnete Flächeninhalte zwischen der x-Achse und `' + str(fnc(sympy.Symbol('x'))) + '`: ')
    print('- Trapezregel:                  `' + str(val_trapeze) + '`')
    print('- Simpsonsche Regel:            `' + str(val_simpson) + '`')
    print('- Differenz (Approximation):    `' + str(val_diff) + '`')
    print('')
    print('')


def showTorusVolume(r_lower, r_upper):
    # Berechne die Volumen
    v_simple = tools.volume_torus_simple(r_lower, r_upper)
    v_integral = tools.volume_torus_integral(r_lower, r_upper)
    v_diff = abs(v_simple - v_integral)

    # Zeige die Folumen an
    print('')
    print('Berechnetes Volumen für einen Torus mit r=`' + str(r_lower) + '` und R=`' + str(r_upper) + '`: ')
    print('- Einfache Berechnung:          `' + str(v_simple) + '`')
    print('- Integrale Berechnung:         `' + str(v_integral) + '`')
    print('- Differenz (Approximation):    `' + str(v_diff) + '`')
    print('')
    print('')
