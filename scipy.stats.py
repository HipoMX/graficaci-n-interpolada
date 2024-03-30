import numpy as np
from scipy.stats import norm

mu, sigma = 0, 0.1
s = np.random.normal(mu, sigma, 1000)
print(f"La media de la muestra es: {np.mean(s)}")
print(f"La desviación estándar de la muestra es: {np.std(s)}")