import numpy as np

def function1():
    l1 = [1, 2, 3, 4, 5]
    print(l1)

    # ndarray
    # a1 = np.array([1, 2, 3, 4, 5, 6])
    a1 = np.array(l1)
    print(a1)
    print(a1.dtype)
    print(a1.itemsize)
    print(a1.size)
    print(a1.shape)
    print(type(a1))

# function1()


def function2():
    l1 = [
        [1, 2],
        [3, 4],
        [5, 6],
        [7, 8]
    ]
    print(l1)

    a1 = np.array(l1)
    print(a1)
    print(a1.dtype)
    print(a1.shape)
    print(a1[0][0])
    print(a1[2][1])

# function2()

def function3():
    l1 = list(range(1, 9))
    print(l1)

    a1 = np.arange(1, 9)
    print('----- a1 ------')
    print(a1)
    print(a1.shape)
    print('----- a1 ------')

    a2 = a1.reshape((4, 2))
    print('----- a2 ------')
    print(a2)
    print(a2.shape)
    print('----- a2 ------')

    a3 = a1.reshape([2, 4])
    print('----- a3 ------')
    print(a3)
    print(a3.shape)
    print('----- a3 ------')

    # a4 = a3.reshape([8])

    a5 = np.arange(12)
    print(a5.shape)

    # print(a5.reshape((3, 3)))
    # print(a5.reshape((4, 4)))
    print(a5.reshape((2, 6)))
    print(a5.reshape((6, 2)))
    print(a5.reshape((3, 4)))
    print(a5.reshape((4, 3)))
    print(a5.reshape((12, 1)))
    print(a5.reshape((1, 12)))


# function3()

