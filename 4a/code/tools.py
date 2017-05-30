import sympy

x = sympy.Symbol('x')


def factor(n):
    if n <= 0:
        return 1
    else:
        return n * factor(n - 1)


def taylor_series(fnc, x0, n):
    i = 0
    p = 0
    while i <= n:
        p = p + (fnc.diff(x, i).subs(x, x0)) / (factor(i)) * (x - x0) ** i
        i += 1
    return p
