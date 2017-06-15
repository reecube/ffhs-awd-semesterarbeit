# Verwendete Bibliotheken importieren
import sympy
import numpy
from sympy.parsing.sympy_parser import parse_expr
from sympy import lambdify
from scipy.integrate import quad


# Frage den Benutzer für eine Funktion mit x-Parameter
def read_user_function():
    x = sympy.Symbol('x')

    while True:
        try:
            user_input = input('Bitte geben Sie eine gültige X-Funktion an: ')

            if user_input == '':
                continue

            expr = parse_expr(user_input, evaluate=False)

            return lambdify(x, expr, modules=['numpy'])
        except SyntaxError:
            print('Ihre Eingabe ist ungültig! Bitte versuchen Sie es erneut oder beenden Sie das Programm.')
            continue


# Frage den Benutzer für eine Zahl
def read_user_number(msg):
    while True:
        try:
            user_input = input(msg)

            return int(user_input)
        except ValueError:
            print('Ihre Eingabe ist ungültig! Bitte versuchen Sie es erneut oder beenden Sie das Programm.')
            continue


# Berechne den Flächeninhalt zwischen Funktion fnc und der x-Achse zwischen start_x und end_x
#    auf die Genauigkeit n (je grösser desto genauer) mit der Trapezregel
def trapeze(fnc, start_x, end_x, n):
    result = 0

    delta_x = (end_x - start_x) / n

    i = 0

    xi = start_x + (i * delta_x)

    for i in range(i, n):
        xii = start_x + ((i + 1) * delta_x)

        result += ((fnc(xi) + fnc(xii)) * delta_x) / 2

        xi = xii

    return result


# Berechne den Flächeninhalt zwischen Funktion fnc und der x-Achse zwischen start_x und end_x
#    auf die Genauigkeit n (je grösser desto genauer) mit der Simpsonsche Regel
def simpson(fnc, start_x, end_x, n):
    result = fnc(start_x)

    delta_x = (end_x - start_x) / n

    last_x_value = end_x - delta_x

    x = start_x + delta_x

    while x < last_x_value:
        result += 4 * fnc(x)
        result += 2 * fnc(x + delta_x)
        x += 2 * delta_x

    result += 4 * fnc(last_x_value)

    result += fnc(end_x)

    result *= delta_x / 3

    return result


# Berechne das Volumen eines Torus mit r und R als Parameter
# Diese Funktion verwendet den Integral-Ansatz
def volume_torus_integral(r_lower, r_upper):
    def fnc(x):
        return sympy.sqrt(r_lower ** 2 - x ** 2)

    # Integral von fnc zwischen `-r` und `r`
    ans, err = quad(fnc, 0 - r_lower, r_lower)

    return 4.0 * numpy.pi * r_upper * ans


# Berechne das Volumen eines Torus mit r und R als Parameter
# Diese Funktion verwendet den einfachen mathematischen Ansatz ohne Integral
#    => gemäss Aufgabenstellung: von Hand
def volume_torus_simple(r_lower, r_upper):
    return 2 * (numpy.pi ** 2) * r_upper * (r_lower ** 2)
