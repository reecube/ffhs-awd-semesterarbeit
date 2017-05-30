import sympy

x = sympy.Symbol('x')

def newtons_method(x0, function, derivation, decimals, calls=1000):
    x1 = x0 - (function.evalf(subs={x: x0}) / derivation.evalf(subs={x: x0}))

    diff_delta_x = abs(x0 - x1)
    diff_max_decimals = 1 / (10 ** decimals)

    if diff_delta_x < diff_max_decimals:
        return x1

    if calls > 0:
        return newtons_method(x1, function, derivation, decimals, calls - 1)
    else:
        return None
