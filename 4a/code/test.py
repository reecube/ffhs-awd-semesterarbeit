##################################################
#
# Aufgabenstellung
#
# Visualisieren Sie die Approximation einer Funktion durch Taylorpolynome (z.B. von sin(x)
#   oder von ln(x+1). Schreibem Sie eine Python-Funktion, die die Graphen der Ursprungsfunktion
#   sowie der Taylorpolynome bis zu einem bestimmten Grad mit Matplotlib visualisiert.
#
##################################################

import sympy
from sympy import lambdify
import tools
import numpy as np
import matplotlib.pyplot as plt

x = sympy.Symbol('x')


def show_taylor_graph(fnc, depth, grid_min, grid_max):
    print('Die Taylorpolynome für', fnc, 'werden berechnet und angezeigt:')

    x_lims = [grid_min, grid_max]
    x1 = np.linspace(x_lims[0], x_lims[1], 800)
    y1 = []

    print('')
    print('berechnen...')
    for i in range(1, depth + 1, 1):
        func = tools.taylor_series(fnc, 0, i * 2)

        for k in x1:
            y1.append(func.subs(x, k))

        plt.plot(x1, y1, label='n=' + str(i))

        y1 = []

        print('n=' + str(i), func)

    lam_base = lambdify(x, fnc, modules=['numpy'])
    plt.plot(x1, lam_base(x1), label=str(fnc))

    plt.xlim(x_lims)
    plt.ylim([grid_min, grid_max])
    plt.xlabel('x')
    plt.ylabel('y')

    plt.legend()

    plt.grid(True)

    plt.title('Approximation einer Funktion durch Taylorpolynome')

    print('')
    print('anzeigen...')
    plt.show()


demoFunctions = [
    sympy.sin(x),
    sympy.ln(x + 1),
]

# Show valid functions
print('')
print('Funktionen:')
print('-------------')
for (i, demoFunction) in enumerate(demoFunctions):
    print('`' + str(i) + '`:', demoFunction)
print('')

# Ask the user for a function
userInput = input('Bitte wählen Sie einen Ausgabetypen: ')

print('')

try:
    selectedFunctionIdx = int(userInput)
except ValueError:
    selectedFunctionIdx = -1

if 0 <= selectedFunctionIdx < len(demoFunctions):
    depth = 5
    grid_min = -5
    grid_max = 5

    if selectedFunctionIdx == 1:
        grid_min = 0

    show_taylor_graph(demoFunctions[selectedFunctionIdx], depth, grid_min, grid_max)
else:
    print('Die Eingabe `' + userInput + '` ist ungültig!')
