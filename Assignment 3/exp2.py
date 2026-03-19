import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

m = 1000
k_values = [1, 2, 5, 30]

mu = 3.5
sigma = np.sqrt(35/12)

plt.figure(figsize=(12,8))

for i, k in enumerate(k_values):
    sample_means = []

    for _ in range(m):
        dice = np.random.randint(1, 7, k)
        sample_means.append(np.mean(dice))

    sample_means = np.array(sample_means)

    plt.subplot(2, 2, i+1)
    plt.hist(sample_means, bins=30, density=True)

    # Overlay ONLY for k = 30
    if k == 30:
        x = np.linspace(min(sample_means), max(sample_means), 100)
        normal_pdf = stats.norm.pdf(x, mu, sigma/np.sqrt(k))
        plt.plot(x, normal_pdf)

    plt.title("k = " + str(k))

plt.tight_layout()
plt.show()