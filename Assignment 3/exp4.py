import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

N = 100
balls = 5000

positions = []

for _ in range(balls):
    steps = np.random.binomial(1, 0.5, N)
    positions.append(np.sum(steps))

positions = np.array(positions)

plt.figure(figsize=(8,5))
plt.hist(positions, bins=30, density=True)

# Overlay normal approximation
mu = N * 0.5
sigma = np.sqrt(N * 0.5 * 0.5)

x = np.linspace(min(positions), max(positions), 100)
normal_curve = stats.norm.pdf(x, mu, sigma)

plt.plot(x, normal_curve)

plt.xlabel("Final Position")
plt.ylabel("Density")
plt.title("Digital Galton Board (Normal Approximation)")
plt.show()