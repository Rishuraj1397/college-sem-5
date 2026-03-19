import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

lam = 0.5
n = 50
m = 500

sample_means = []

for _ in range(m):
    sample = np.random.exponential(scale=1/lam, size=n)
    sample_means.append(np.mean(sample))

sample_means = np.array(sample_means)

# Q-Q Plot
plt.figure(figsize=(6,6))
stats.probplot(sample_means, dist="norm", plot=plt)
plt.title("Q-Q Plot (Exponential -> Normal via CLT)")
plt.show()