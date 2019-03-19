import numpy as np

# a2 = np.array([1, 2, 3, 4, 5], dtype=np.int16)
# print(a2)
# print(a2.dtype)
#
# a1 = np.array([1, 2, 3, 4, 5, 'test1', 'test2'])
# print(a1)
# print(a1.dtype)


def function1():
    a1 = np.array(np.arange(6))
    print(a1.shape)
    print(a1.ndim)
    print(a1)
    print(a1[0])
    print(a1[:])
    print(a1[0:3])
    print(a1[0:5])
    print(a1[:2])
    print(a1[0:])

# function1()

def function2():
    a1 = np.array([1, 2, 3, 4])

    a2 = a1.reshape((2, 2))
    print(a2)

    a3 = a1.reshape((2, 2), order='F')
    print(a3)

    a4 = np.array([1, 2, 3, 4, 5, 6])
    print(a4.reshape((2, 3), order='C'))    # row-major
    print(a4.reshape((2, 3), order='F'))    # column-major

# function2()


def function3():
    a2 = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
    print(a2)
    print(a2.shape)
    print(a2.ndim)
    print(a2[:])
    print(a2[:2])
    print(a2[1:])
    print(a2[:])

# function3()
