import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

# Definir los puntos de la función original
x = np.arange(0, 11, 1)
y = x**2

# Definir los puntos donde se hará la interpolación
x_new = np.linspace(0, 10, num=1000, endpoint=True)

# Realizar la interpolación
f = interp1d(x, y, kind='cubic')

# Graficar la función original y la interpolada
plt.plot(x, y, 'o', label='Original')
plt.plot(x_new, f(x_new), '-', label='Interpolada')
plt.legend()
plt.show()