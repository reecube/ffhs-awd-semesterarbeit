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

import view

# Berechne das Torus-Volumen und zeige das Resultat an
view.showTorusVolume(5, 20)

# Frage den Benutzer nach einer Funktion und stelle entsprechende Berechnungen an
view.showSurface()
