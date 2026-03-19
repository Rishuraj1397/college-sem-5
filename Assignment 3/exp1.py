import numpy as np
import matplotlib.pyplot as plt

n = 10000
p = 0.7

trials = np.random.binomial(1, p, n)

cumulative_avg = np.cumsum(trials) / np.arange(1, n + 1)

plt.figure(figsize=(10,5))
plt.plot(cumulative_avg)
plt.axhline(y=p, linestyle='--')
plt.xlabel("Number of Trials (n)")
plt.ylabel("Running Average")
plt.title("Law of Large Numbers")
plt.show()