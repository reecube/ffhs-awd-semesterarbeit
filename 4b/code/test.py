##################################################
#
# Aufgabenstellung
#
# Geben Sie einige Beispiele, wie Funktionen mit Matplotlib visualisiert werden können.
#
# Schauen Sie sich dazu z.B. folgende Tutorials an:
# - multidimensionale Splines:
#     http://docs.scipy.org/doc/scipy/reference/tutorial/interpolate.html
# - 3D Grafiken von 2-dimensionalen Funktionen
#     http://matplotlib.org/examples/mplot3d/surface3d_demo3.html
#
##################################################

# Libraries importieren
import sympy
import numpy as np
import view

# Symbole für die Funktionen erstellen
x = sympy.Symbol('x')
y = sympy.Symbol('y')

# Die Demo-Funktionen welche angezeigt werden können
demoFunctions = [
    {
        'fnc': x + y,
    },
    {
        'fnc': x ** 3 * y ** 2,
    },
    {
        'fnc': x ** 2 / (y ** 3 + 1),
    },
    {
        'fnc': sympy.sin(x) - sympy.tan(y),
    },
    {
        'fnc': sympy.sqrt(x) * sympy.cos(y),
        'vmin': 0,
        'vmax': 6.0,
    },
    {
        'fnc': sympy.log(10 * x) * sympy.sin(3 ** y),
        'vmin': 0.1,
        'vmax': 6.0,
    },
    {
        'fnc': sympy.sin(x * 2) - sympy.cos(y * 2),
        'vmin': 0.1,
        'vmax': 6.0,
    },
]

# Die Demo-Graphtypen welche angezeigt werden können
demoTypes = [
    'imagemap',
    'surface',
]


def ask_for_function():
    # Zeigt die verfügbaren Funktionen welche angezeigt werden können
    print('')
    print('Funktionen:')
    print('-------------')
    for (i, demo_function) in enumerate(demoFunctions):
        print('`' + str(i) + '`:', demo_function['fnc'])
    print('')

    # Frag den Benutzer welche Funktion er anzeigen möchte
    user_input = input('Bitte wählen Sie eine Funktion: ')

    print('')

    # Versucht die Benutzereingabe in eine Zahl umzuwandeln
    try:
        selected_function_idx = int(user_input)
    except ValueError:
        selected_function_idx = -1

    # Zeigt einen Fehler an, falls die Benutzereingabe ungültig ist
    if not (0 <= selected_function_idx < len(demoFunctions)):
        print('Die Eingabe `' + user_input + '` ist ungültig!')
        exit(1)

    return demoFunctions[selected_function_idx]


def ask_for_graphtype():
    # Zeigt die verfügbaren Graphtypen welche angezeigt werden können
    print('')
    print('Graphtypen:')
    print('-----------')
    for (i, demo_type) in enumerate(demoTypes):
        print('`' + str(i) + '`:', demo_type)
    print('')

    # Frag den Benutzer welcher Graphtyp er anzeigen möchte
    user_input = input('Bitte wählen Sie einen Graphtypen: ')

    print('')

    # Versucht die Benutzereingabe in eine Zahl umzuwandeln
    try:
        selected_type_idx = int(user_input)
    except ValueError:
        selected_type_idx = -1

    # Zeigt einen Fehler an, falls die Benutzereingabe ungültig ist
    if not (0 <= selected_type_idx < len(demoFunctions)):
        print('Die Eingabe `' + user_input + '` ist ungültig!')
        exit(1)

    return demoTypes[selected_type_idx]


# Frage den Benutzer was er sehen möchte
demoType = ask_for_graphtype()
demoFunction = ask_for_function()

# Zeige seine Auswahl an
view.show(demoFunction, demoType)
