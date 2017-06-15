##################################################
#
# Aufgabenstellung
#
# Implementieren Sie die Trapezregel und die Simpsonsche Regel zur numerischen Bestimmung von bestimmten Integralen.
#
# Wenden Sie diese Algorithmen auf die Berechnung des Volumens eines Kreisrings an.
#   (Ein Kreisring kann als Rotationskörper eines Kreises aufgefasst werden,
#   wenn der Kreis sich vollständig oberhalb der xx-Achse befindet und wenn er um die xx-Achse rotiert wird.
#
# Vergleichen Sie die Genauigkeit dieser Approximationen miteinander und
#   vergleichen Sie die Resultate mit den exakten Werten, die sie von Hand und mit mit Sympy bestimmen.
#
# Schließen Sie Ihre Semesterarbeit mit einer Diskussion des Einsatzes von Python für praxisbezogene Anwendungen ab.
#
##################################################

import tools


def demo_function_simple(x):
    return 2


def demo_function_linear(x):
    return x / 2


def demo_function_exp(x):
    return x ** 2


start_x = 2
end_x = 4
n = 100

print('Von Hand: ')
print((end_x - start_x) * demo_function_simple(10))
print('')

print('Trapezregel: ')
print(tools.trapeze(demo_function_exp, start_x, end_x, n))
print('')

print('Simpsonsche Regel: ')
print(tools.simpson(demo_function_exp, start_x, end_x, n))
print('')
