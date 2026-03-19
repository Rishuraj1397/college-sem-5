import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)

X = np.random.randint(800, 5001, 100)
e = np.random.normal(0, 50000, 100)
y = 150 * X + e

df = pd.DataFrame({'SqFt': X, 'Price': y})

nan_indices = np.random.choice(df.index, 5, replace=False)
df.loc[nan_indices, 'Price'] = np.nan
df['Price'].fillna(df['Price'].median(), inplace=True)

locations = np.random.choice(['Urban', 'Suburban', 'Rural'], 100)
df['Location'] = locations

df = pd.get_dummies(df, columns=['Location'])

corr_matrix = df.corr()

plt.figure()
sns.heatmap(corr_matrix, annot=True)
plt.show()

fig, axes = plt.subplots(1, 2)

axes[0].hist(df['Price'])
axes[0].set_title('Price Histogram')

axes[1].scatter(df['SqFt'], df['Price'])
axes[1].set_title('SqFt vs Price')

plt.show()