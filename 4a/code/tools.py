import sympy

# X-Symbol für die Funktionen erstellen
x = sympy.Symbol('x')


# Berechnet die Fakultät, also n! wenn n <= 0 dann wird 1 zurückgegeben.
def factor(n):
    if n <= 0:
        return 1
    else:
        return n * factor(n - 1)


# Berechnet die Taylor-Polynome
#   fnc:  Ist die Funktion für das Taylor-Polynom
#   x0:   Ist der Startwert
#   n:    Ist der Grad für das Taylor-Polynom
def taylor_series(fnc, x0, n):
    # Standardwert und Startwert für p ist 0
    p = 0

    # Die Taylor-Polynome basieren auf der Summenformel von i=0 bis i=n, dafür wird ein for-Loop verwendet
    for i in range(0, n + 1):
        # Hierbei andelt es sich um die Taylor-Polynom-Formel:
        # (i-te x-Ableitung von fnc, berechnet mit x=x0) geteilt durch (die Fakultät von i) multipliziert mit (x hoch i)
        p += (fnc.diff(x, i).subs(x, x0)) / (factor(i)) * (x - x0) ** i

    # Nun wird p zurückgegeben, falls n >= 0 wird p eine Funktion sein
    return p
