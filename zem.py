import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 30)
y = np.cos(x)

plt.plot(x, y)

plt.show() # affiche la figure à l'écran
