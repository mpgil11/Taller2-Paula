import numpy as np
import matplotlib.pyplot as plt

mu = 5
sigma = 0.6
n=1000
vals = np.random.normal(loc=mu, scale=sigma, size=n)

plt.hist(vals, bins=30, color='skyblue', edgecolor='black')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.title('Histograma de datos')
plt.grid(axis='y', alpha=0.75)
