##################################################
#
# Aufgabenstellung
#
# Implementieren Sie das Newton-Verfahren zur Bestimmung von Nullstellen von Funktionen.
# (Dabei soll die Funktion als Sympy-Objekt eingegeben werden, so dass Sie mit Sympy die Ableitung davon bestimmen koennen.)
#
# Newtonverfahren und Taylorentwicklung
# 1. Mit Hilfe des Newtonverfahrens bestimme man ausgehend von x0 = 1
#    die Nullstelle der Gleichung 3 cos(x) - x = 0 mit einer Genauigkeit von 5 Nachkommastellen.
#
##################################################

import sympy
import tools

x = sympy.Symbol('x')

demoFunction = 3 * sympy.cos(x) - x
demoDerivation = sympy.diff(demoFunction)

demoX0 = 1

demoZero = tools.newtons_method(demoX0, demoFunction, demoDerivation, 5)

print('Die Nullstelle fuer `' + str(demoFunction) + '=0` bei `x0=' + str(demoX0)
      + '` liegt bei `' + str(demoZero) + '`.')
