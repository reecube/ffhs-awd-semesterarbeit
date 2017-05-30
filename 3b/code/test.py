##################################################
#
# Aufgabenstellung
#
# Um eine moeglichst glatte Kurve durch eine bestimmte Anzahl von Punkten zu zeichnen, koennen Splints verwendet werden.
# Splints sind Kurvenstuecke aus kubischen Kurven, die so "zusammengeklebt" werden, dass an den Klebestellen die ersten beiden Ableitungen uebereinstimmen.
#
# Lesen Sie zuerst http://docs.scipy.org/doc/scipy/reference/tutorial/interpolate.html (nur bis zum Abschnitt ueber eindimensionale Splines).
#
# Approximieren Sie eine Kurve mit Splines. Zeichnen Sie die Stuetzpunkte, die Splines und die exakte Kurve in einer Graphik mit Matplotlib.
# Splines koennen mit https://docs.scipy.org/doc/scipy/reference/tutorial/interpolate.html erstellt werden.
#
##################################################

import numpy as np
import matplotlib.pyplot as plt

from scipy.interpolate import interp1d

# Config

waveCount = 2

xMin = 0
xMax = (waveCount * 2) * np.pi

xStepCount = 4

splineAccuracy = 4

# Code

x = np.linspace(xMin, xMax, num=(xStepCount * (waveCount * 2)))
y = np.sin(x)

f = interp1d(x, y, kind='cubic')

xnew = np.linspace(xMin, xMax, num=(xStepCount * (waveCount * 2) * splineAccuracy))

plt.plot(x, y, 'bx-', xnew, f(xnew), 'g--')

plt.legend(['Linie', 'Spline'], loc='best')

plt.title('Semesterarbeit Teil 3b: Splines')

plt.show()
