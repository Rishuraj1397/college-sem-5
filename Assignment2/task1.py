import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, poisson, geom

# Task 1: Binomial (1000, 0.3)

n1 = 1000
p1 = 0.3

mean1 = n1 * p1
var1 = n1 * p1 * (1 - p1)

print("Task 1 Mean:", mean1)
print("Task 1 Variance:", var1)

x1 = np.arange(250, 350)
y1 = binom.pmf(x1, n1, p1)

plt.figure()
plt.plot(x1, y1)
plt.title("Task 1 Binomial Distribution")
plt.show()


# Task 2: Binomial (50, 0.3)

n2 = 50
p2 = 0.3

mode2 = int((n2 + 1) * p2)

print("Task 2 Most Likely Outcome:", mode2)

x2 = np.arange(0, 51)
y2 = binom.pmf(x2, n2, p2)

plt.figure()
plt.bar(x2, y2)
plt.title("Task 2 Binomial Distribution")
plt.show()


# Task 3: Poisson (lambda = 10)

lam3 = 10

prob_8 = poisson.pmf(8, lam3)
prob_gt_15 = 1 - poisson.cdf(15, lam3)

print("Task 3 P(X=8):", prob_8)
print("Task 3 P(X>15):", prob_gt_15)


# Task 4: Geometric (p = 0.25)

p4 = 0.25

prob_4 = geom.pmf(4, p4)

print("Task 4 P(first success on 4th):", prob_4)


# Task 5: Poisson Approximation

n5 = 1000
p5 = 0.02
lam5 = n5 * p5

prob_5_defects = poisson.pmf(5, lam5)

print("Task 5 P(5 defects):", prob_5_defects)