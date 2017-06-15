import sympy
from sympy.parsing.sympy_parser import parse_expr
from sympy import lambdify


def read_user_function():
    x = sympy.Symbol('x')

    while True:
        try:
            user_input = input('Bitte geben Sie eine gültige X-Funktion an: ')

            expr = parse_expr(user_input, evaluate=False)

            return lambdify(x, expr, modules=['numpy'])
        except SyntaxError:
            print('Ihre Eingabe ist ungültig! Bitte versuchen Sie es erneut oder beenden Sie das Programm.')
            continue


def read_user_number(msg):
    while True:
        try:
            user_input = input(msg)

            return int(user_input)
        except ValueError:
            print('Ihre Eingabe ist ungültig! Bitte versuchen Sie es erneut oder beenden Sie das Programm.')
            continue


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
