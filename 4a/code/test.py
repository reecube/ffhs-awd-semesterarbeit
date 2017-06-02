##################################################
#
# Aufgabenstellung
#
# Visualisieren Sie die Approximation einer Funktion durch Taylorpolynome (z.B. von sin(x)
#   oder von ln(x+1). Schreibem Sie eine Python-Funktion, die die Graphen der Ursprungsfunktion
#   sowie der Taylorpolynome bis zu einem bestimmten Grad mit Matplotlib visualisiert.
#
##################################################

# Libraries importieren
import sympy
from sympy import lambdify
import tools
import numpy as np
import matplotlib.pyplot as plt

# X-Symbol für die Funktionen erstellen
x = sympy.Symbol('x')


# Zeigt eine Funktion mit Anzahl Taylor-Polynomen an auf der angegebenen Feldgrösse
def show_taylor_graph(fnc, depth, grid_min, grid_max):
    print('Die Taylorpolynome für', fnc, 'werden berechnet und angezeigt:')

    # Definiert die Feldgrösse für den Graphen
    x_lims = [grid_min, grid_max]
    y_lims = [grid_min, grid_max]
    plt.xlim(x_lims)
    plt.ylim(y_lims)

    # Erstellt 800 regelmässige x1-Werte zwischen Feldgrösse-Minimum und Feldgrösse-Maximum
    x1 = np.linspace(x_lims[0], x_lims[1], 800)
    y1 = []

    #
    print('')
    print('berechnen...')
    for n in range(1, depth + 1, 1):
        func = tools.taylor_series(fnc, 0, n)

        for k in x1:
            y1.append(func.subs(x, k))

        plt.plot(x1, y1, label='n=' + str(n))

        y1 = []

        print('n=' + str(n), func)

    # Erstellt die Werte für die Basis-Funktion
    lam_base = lambdify(x, fnc, modules=['numpy'])
    plt.plot(x1, lam_base(x1), label=str(fnc))

    # Benennt die x und y Etiketten des Grpahen
    plt.xlabel('x')
    plt.ylabel('y')

    # Zeigt im Graphen eine Legende an
    plt.legend()

    # Zeigt im Graphen die Gitterlinien an
    plt.grid(True)

    # Zeigt im Graphen einen Titel an
    plt.title('Approximation einer Funktion durch Taylorpolynome')

    # Zeigt den Graphen an
    print('')
    print('anzeigen...')
    plt.show()


# Die Demo-Funktionen welche angezeigt werden können
demoFunctions = [
    sympy.sin(x),
    sympy.ln(x + 1),
]

# Zeigt die verfügbaren Funktionen welche angezeigt werden können
print('')
print('Funktionen:')
print('-------------')
for (i, demoFunction) in enumerate(demoFunctions):
    print('`' + str(i) + '`:', demoFunction)
print('')

# Frag den Benutzer welche Funktion er anzeigen möchte
userInput = input('Bitte wählen Sie einen Ausgabetypen: ')

print('')

# Versucht die Benutzereingabe in eine Zahl umzuwandeln
try:
    selectedFunctionIdx = int(userInput)
except ValueError:
    selectedFunctionIdx = -1

# Zeigt die ausgewählte Funktion an, falls diese gültig ist
if 0 <= selectedFunctionIdx < len(demoFunctions):
    val_depth = 5
    val_grid_min = -5
    val_grid_max = 5

    if selectedFunctionIdx == 1:
        val_grid_min = 0

    show_taylor_graph(demoFunctions[selectedFunctionIdx], val_depth, val_grid_min, val_grid_max)
else:
    print('Die Eingabe `' + userInput + '` ist ungültig!')
