import sympy

# X-Symbol für die Funktionen erstellen
x = sympy.Symbol('x')


# Berechnet die Fakultät, also n! wenn n <= 0 dann wird 1 zurückgegeben.
def factor(n):
    if n <= 0:
        return 1
    else:
        return n * factor(n - 1)


# Berechnet die Taylor-Polynome1
#   fnc:  Ist die Funktion für das Taylor-Polynom
#   x0:   Ist der Startwert
#   n:    Ist der Grad für das Taylor-Polynom
def taylor_series(fnc, x0, n):
    # Standardwert und Startwert für p ist 0
    p = 0

    for i in range(0, n + 1):
        print('for  ', i, p)
        p = p + (fnc.diff(x, i).subs(x, x0)) / (factor(i)) * (x - x0) ** i

    # Nun wird p zurückgegeben, falls n >= 0 wird p eine Funktion sein
    return p
