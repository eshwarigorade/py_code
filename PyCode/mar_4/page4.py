import numpy as np
from functools import reduce

l1 = [1, 2, 3, 4, 5]
l2 = list(map(lambda x: x * 10, l1))
print(l2)
l3 = list(filter(lambda x: x <= 3, l1))
print(l3)
print(reduce(lambda x, y: x + y, l1))

a1 = np.array([1, 2, 3, 4, 5])
# broadcasting operators

# map
print(a1 + 10)
print(a1 * 10)
print(a1 / 5)
print(a1 - 10)

print(a1 < 3)
print(a1 <= 3)
print(a1 > 3)
print(a1 >= 4)
print(a1 != 3)
print(a1 == 3)

a2 = np.array([1, 2, 3, 4, 5])
print(a2[:])
print(a2 < 3)

# filter the array
print(a2[a2 < 3])
print(a2[a2 >= 4])
