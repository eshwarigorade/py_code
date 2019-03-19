import numpy as np
import sys

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('----- python collection -------')
print(type(l1))
print(l1)
print('memory required for every item in list: {}'.format(sys.getsizeof(l1[0])))
print('count: {}'.format(len(l1)))
print('total memory: {}'.format(sys.getsizeof(l1[0]) * len(l1)))

a1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print('----- numpy array -------')
print(type(a1))
print(a1)
print('memory required for every item in array: {}'.format(a1.itemsize))
print('count: {}'.format(a1.size))
print('total memory: {}'.format(a1.itemsize * a1.size))
print('dtype: {}'.format(a1.dtype))


a2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=np.int16)
print('----- numpy array -------')
print(type(a2))
print(a2)
print('memory required for every item in array: {}'.format(a2.itemsize))
print('count: {}'.format(a2.size))
print('total memory: {}'.format(a2.itemsize * a2.size))
print('dtype: {}'.format(a2.dtype))