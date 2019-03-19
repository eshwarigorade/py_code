import numpy as np

a1 = np.zeros((2, 3), dtype=np.int16)
print(a1)
print(a1.itemsize)
print(a1.itemsize * a1.size)

print(np.empty(10))
print(np.ones(10))

a2 = np.random.randn(5)
print(a2)
