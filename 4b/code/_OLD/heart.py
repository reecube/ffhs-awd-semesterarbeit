# Libraries importieren
import sympy
from sympy import lambdify
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Symbole für die Funktionen erstellen
x = sympy.Symbol('x')
y = sympy.Symbol('y')
z = sympy.Symbol('z')

# Funktionen zur Anzeige
fncx = 16 * ((sympy.sin(x)) ** 3)
fncy = 13 * sympy.cos(y) - 5 * sympy.cos(2 * y) - 2 * sympy.cos(3 * y) - sympy.cos(4 * y)
fncz = z


def show():
    vals = np.linspace(0, 2 * np.pi, 100)

    lamx = lambdify(x, fncx, modules=['numpy'])
    lamy = lambdify(y, fncy, modules=['numpy'])
    lamz = lambdify((x, y, z), fncz, modules=['numpy'])

    xnew = lamx(vals)
    ynew = lamy(vals)
    znew = lamz(xnew, ynew, vals)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for i in range(0, 10 + 1):
        ax.plot(xnew * ((15 - i) / 5), ynew * ((15 - i) / 5), i)

    plt.show()
