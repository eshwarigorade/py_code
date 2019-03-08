import numpy as np
import pandas as pd

# a1 = np.array([1, 2, 3, 4, 5])
# print('mean: {}'.format(a1.mean()))

s1 = pd.Series([2, 1, 5, 4, 3])
print('mean: {}'.format(s1.mean()))
print('median: {}'.format(s1.median()))
print('mode: {}'.format(s1.mode()))
print('var: {}'.format(s1.var()))
print('std: {}'.format(s1.std()))


print(s1.head(2))
print(s1.tail(2))
print(s1.describe())
print(s1.sort_values())
print(s1.sort_values(ascending=False))

print(s1.apply(lambda x: x * x))
print(s1.apply(lambda x: x ** 3))

# max(s1)
# min(s1)
# list(s1)