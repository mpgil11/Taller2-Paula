import numpy as np

mu = 3
sigma = 0.3
n=1000
vals = np.random.normal(loc=mu, scale=sigma, size=n)
print(vals)