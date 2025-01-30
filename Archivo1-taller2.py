import numpy as np

mu = 5
sigma = 0.6
n=1000
vals = np.random.normal(loc=mu, scale=sigma, size=n)
print(vals)