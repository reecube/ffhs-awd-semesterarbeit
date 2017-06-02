# Libraries importieren
import sympy
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sympy import lambdify
from scipy.interpolate import griddata

# Symbole für die Funktionen erstellen
x = sympy.Symbol('x')
y = sympy.Symbol('y')


def default_value(fnc, key, val):
    if key in fnc:
        return fnc[key]
    else:
        return val


def show_imagemap(lam_fnc, vcount):
    # Die X- und Y-Daten generieren
    grid_x, grid_y = np.mgrid[0:1:100j, 0:1:200j]

    # Zufallswerte mit der Anzahl vcount generieren
    random_values = np.random.rand(vcount, 2)

    # Werte durch die Funktion aus den Zufallswerten generieren
    values = lam_fnc(random_values[:, 0], random_values[:, 1])

    # Die Z-Daten generieren
    grid_z_nearest = griddata(random_values, values, (grid_x, grid_y), method='nearest')
    grid_z_linear = griddata(random_values, values, (grid_x, grid_y), method='linear')
    grid_z_cubic = griddata(random_values, values, (grid_x, grid_y), method='cubic')

    # Neuer Subplot, im Grid 2x2 auf der Position 1
    plt.subplot(221)
    plt.imshow(lam_fnc(grid_x, grid_y).T, extent=(0, 1, 0, 1), origin='lower')
    plt.plot(random_values[:, 0], random_values[:, 1], 'k.', ms=1)
    plt.title('Original')

    # Neuer Subplot, im Grid 2x2 auf der Position 2
    plt.subplot(222)
    plt.imshow(grid_z_nearest.T, extent=(0, 1, 0, 1), origin='lower')
    plt.title('Nächste (nearest)')

    # Neuer Subplot, im Grid 2x2 auf der Position 3
    plt.subplot(223)
    plt.imshow(grid_z_linear.T, extent=(0, 1, 0, 1), origin='lower')
    plt.title('Linear (linear)')

    # Neuer Subplot, im Grid 2x2 auf der Position 4
    plt.subplot(224)
    plt.imshow(grid_z_cubic.T, extent=(0, 1, 0, 1), origin='lower')
    plt.title('Kubisch (cubic)')

    # Korrigiert einen Fehler bei der Darstellung der Texte
    plt.gcf().set_size_inches(8, 8)

    # Den Graphen anzeigen
    plt.show()


def show_surface(lam_fnc, vmin, vmax, vstep):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    val_x = val_y = np.arange(vmin, vmax, vstep)
    val_big_x, val_big_y = np.meshgrid(val_x, val_y)
    zs = np.array([lam_fnc(val_x, val_y) for val_x, val_y in zip(np.ravel(val_big_x), np.ravel(val_big_y))])
    val_big_z = zs.reshape(val_big_x.shape)

    ax.plot_surface(val_big_x, val_big_y, val_big_z)

    ax.set_xlabel('X Achse')
    ax.set_ylabel('Y Achse')
    ax.set_zlabel('Z Achse')

    plt.show()


def show(fnc, graph_type):
    # Die Funktion ausführbar machen mit lambdify
    lam_fnc = lambdify((x, y), fnc['fnc'], modules=['numpy'])

    if graph_type == 'imagemap':
        # Den vcount-Wert auslesen oder 100 als Standardwert verwenden
        vcount = default_value(fnc, 'vcount', 100)

        show_imagemap(lam_fnc, vcount)
    elif graph_type == 'surface':
        # Den vmin-Wert auslesen oder -3.0 als Standardwert verwenden
        vmin = default_value(fnc, 'vmin', -3.0)

        # Den vmax-Wert auslesen oder 3.0 als Standardwert verwenden
        vmax = default_value(fnc, 'vmax', 3.0)

        # Den vstep-Wert auslesen oder 0.05 als Standardwert verwenden
        vstep = default_value(fnc, 'vstep', 0.05)

        show_surface(lam_fnc, vmin, vmax, vstep)
    else:
        print('Bye!')
